from typing import List


REQUISITES_TO_UPDATE_FOR_SLS_RUN = [
    "require",
    "require_in",
    "require_any",
    "listen",
    "arg_bind",
]


async def run(
    hub,
    ctx,
    name: str,
    sls_sources: List[str],
    params: List[str] = None,
    **kwargs,
):
    """
    State module to structure a group of SLS files into an independent construct that
    can be invoked from SLS code multiple times with different set of arguments and parameters

    Args:
        name(string):
            An idem name of the resource.

        sls_sources(list):
            List of sls files to run

        params(list, Optional):
            List of params files. All the params provided in these files will be consolidated and these consolidated params
            will override the params passed in Idem run. These consolidated params along with params passed to Idem run
            will be used to run the sls files provided in sls_sources. Defaults to None.

        kwargs(Dict[str, Any], Optional):
            parameters passed in kwargs are used as parameters to resolve parameters in sls_sources files.

        Request Syntax:
           .. code-block:: sls

              [sls-run-name]:
                sls.run:
                  - sls_sources:
                      - 'string'
                  - params:
                      - 'string'

        Returns:
            Dict[str, Any]

        Examples:
           .. code-block:: sls

               service4:
                sls.run:
                  - sls_sources:
                      - sls.service_file1
                      - sls.service_file2
                  - params:
                      - params.file1
    """

    result = dict(comment=[], name=name, old_state=None, new_state=None, result=True)

    # The sls_sources and params provided to this state are paths to files.
    # To resolve the location of files and parse them we use this hub.OPT.idem.tree which gives us the base path.
    sls_sources_path = list()
    param_sources_path = list()
    if hub.OPT.idem.tree:
        tree = f"file://{hub.OPT.idem.tree}"
        hub.log.debug(f"Added tree to sls and param sources: {tree}")
        sls_sources_path.append(tree)
        param_sources_path.append(tree)

    main_run_name = ctx.run_name
    # Create a temporary run name to use while compiling the sls_sources passed to this state
    temporary_run_name = main_run_name + "." + name

    # Create a temporary run to process the new sls block
    await hub.idem.state.create(
        name=temporary_run_name,
        sls_sources=sls_sources_path,
        # Allow a different render pipe to be used for the new render block
        # Default to the renderer of the main run
        render=hub.idem.RUNS[main_run_name].get("render"),
        # Copy state.apply parameters from the main run
        **{
            k: hub.idem.RUNS[main_run_name].get(k)
            for k in (
                "runtime",
                "subs",
                "cache_dir",
                "test",
                "acct_file",
                "acct_key",
                "acct_profile",
                "acct_blob",
                "managed_state",
                "param_sources",
                "acct_data",
                "invert_state",
            )
        },
    )

    # Gather params files provided to this file and combine with idem run params
    # we gather params from idem run, params files provided to this state and inline params provided to this state.
    # will combine the params from all the three sources. If there are common params, Inline params takes precedence
    # followed by params files provided to this state.
    run_params_ret = await _gather_params(
        hub, main_run_name, temporary_run_name, params, param_sources_path, kwargs
    )
    if "errors" in run_params_ret:
        result["comment"] = [
            f"Error in gathering params files for sls.run {name}"
        ] + run_params_ret["errors"]
        result["result"] = False
        hub.idem.RUNS.pop(temporary_run_name, None)
        return result

    # parse the sls_sources provided to this state with the consolidated params and get high data
    src = hub.idem.sls_source.init.get_refs(
        sources=sls_sources_path, refs=hub.OPT.idem.sls
    )

    # Resolve the new sls_sources with the main run
    gather_data = await hub.idem.resolve.init.gather(
        temporary_run_name,
        *sls_sources,
        sources=src["sls_sources"],
    )
    # Add the newly resolved blocks to the temporary run
    await hub.idem.sls_source.init.update(temporary_run_name, gather_data)

    if hub.idem.RUNS[temporary_run_name]["errors"]:
        result["comment"] = [
            f"Error in gathering sls_sources for sls.run {name}"
        ] + hub.idem.RUNS[temporary_run_name]["errors"]
        result["result"] = False
        hub.idem.RUNS.pop(temporary_run_name, None)
        return result

    # loop through high data and append sls.run name to all the states to make them unique
    # if the sls.run state is run on same set of files with different parameters adding sls.run name to all included
    # states makes them unique in idem run.
    modified_high_data = {}
    high_data = hub.idem.RUNS[temporary_run_name]["high"]
    for resource_name, resource_state in high_data.items():
        # append sls.run state name to all states in high data
        modified_high_data[f"{name}.{resource_name}"] = resource_state

    hub.idem.RUNS[temporary_run_name]["high"] = modified_high_data

    # compile the high data to low data
    await hub.idem.state.compile(temporary_run_name)

    _format_requisites_in_low_data(hub, name, temporary_run_name)

    low_data = hub.idem.RUNS[temporary_run_name]["low"]

    # Iterate over the states passed to this sls.run and add the extra attributes __sls_run_idm, sls_run_id
    # to identify these states from other states that are running in main idem run.
    for chunk in low_data:
        # Add the low data gathered from sls_sources passed to this state to main run
        hub.idem.RUNS[main_run_name].get("add_low").append(chunk)

    result["new_state"] = {
        "Status": f"Added {len(low_data)} states to be run.",
        "is_sls_run": True,
    }
    hub.idem.RUNS.pop(temporary_run_name, None)
    return result


def is_pending(hub, ret):
    """
    Always skip reconciliation for sls.run because is_pending will be called for individual states
    """
    return False


# Utility methods to extract params and sls_sources passed to sls.run and update requisites


async def _gather_params(
    hub, main_run_name, temporary_run_name, params, param_sources_path, kwargs
):
    """Gather params passed to main Idem run, params files passed to the sls.run
       and inline parameters passed to sls.run
       will combine the params from all the three sources. If there are common params, Inline params takes precedence
       followed by params files provided to this state.

    Args:
        main_run_name(string):
            Name of the Idem run

        params(Dict[str, List[str]]):
            params sources and params files to get params from.

        param_sources_path(list):
            List of file paths of provided params

        kwargs(Dict[str, Any]):
            Inline params provided to the sls.run
    """
    run_params = {}
    # params given during Idem main run.
    run_params.update(hub.idem.RUNS[main_run_name]["params"] or {})

    # parse params files provide to this state.
    if params:
        params = hub.idem.sls_source.param.get_refs(
            sources=param_sources_path, refs=params
        )
        resolved_params_ret = await _gather_params_from_included_files(
            hub, temporary_run_name, params
        )
        if not resolved_params_ret or "errors" in resolved_params_ret:
            return {"errors": resolved_params_ret["errors"]}
        # combining the params provided to this file and idem run params.
        # if there is overlapping of params, params provided to this file will take precedence over idem run params.
        if "params" in resolved_params_ret:
            run_params.update(resolved_params_ret["params"])

    # update the params with inline params if provided.
    if kwargs:
        run_params.update(kwargs)
    hub.idem.RUNS[temporary_run_name]["params"] = run_params
    return {"params": run_params}


async def _gather_params_from_included_files(hub, temporary_run_name, params):
    """Gather parameters from the params files.

    Args:
        temporary_run_name(string):
            Name of the Idem run

        params(Dict[str, List[str]]):
            params sources and params files to get params from.
    """

    param_sources = params["param_sources"]
    params = params["params"]
    gather_data = await hub.idem.resolve.init.gather(
        temporary_run_name, *params, sources=param_sources
    )
    if gather_data["errors"]:
        return {"errors": gather_data["errors"]}
    hub.idem.sls_source.param.process_params(temporary_run_name, gather_data)

    return {"params": hub.idem.RUNS[temporary_run_name]["params"]}


def _format_requisites_in_low_data(hub, name, run_name):
    """
    In this function we add sls.run state name to the requisites.
    we loop through the low data find the requisites and add sls.run state name to
    identify the exact state we are referring
    """
    low_data = hub.idem.RUNS[run_name]["low"]
    # loop through low data
    for state in low_data:
        # loop through resource attributes
        for attribute_key, attribute_val in state.items():
            # check if the requisite is present
            if attribute_key in REQUISITES_TO_UPDATE_FOR_SLS_RUN:
                for require_state in attribute_val:
                    updated_requisites = []
                    state_func = next(iter(require_state))
                    require_arg_value = require_state[state_func]

                    for requisite in require_arg_value:
                        state_name = next(iter(requisite))
                        args = requisite[state_name]
                        # check if the referred requisite is part of this current run
                        # if chunk is part of this sls.run add sls.run name else do not add sls.run name
                        r_chunks = hub.idem.tools.get_chunks(
                            low_data, state_func, f"{name}.{state_name}"
                        )
                        if r_chunks:
                            updated_requisites.append({f"{name}.{state_name}": args})
                        else:
                            updated_requisites.append({f"{state_name}": args})
                    require_state[state_func] = updated_requisites

    hub.idem.RUNS[run_name]["low"] = low_data
