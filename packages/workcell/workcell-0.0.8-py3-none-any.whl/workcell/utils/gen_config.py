import os
import json
from workcell.core import format_workcell_fqdn


def gen_workcell_config(
    workcell_path: str,
    workcell_version: str,
    workcell_runtime: str
) -> str:
    """Prepare template folder for workcell.
    This will create a folder and package template in build_path.
    Args:
        workcell_path (str): path to workcell.
            e.g. workcell_path = "examples.hello_workcell.app" or "examples/hello_workcell/app.py"
        workcell_version (str): workcell version, equals to serverless function stage.
            e.g. workcell_version = "latest"
        workcell_runtime (str): workcell template.
            e.g. workcell_runtime = "python3.8"
    Return:
        workcell_config (dict): build config for workcell.
    """
    # extract workcell_config
    try:
        username = os.environ["WORKCELL_USERNAME"]
        workcell_fqdn = format_workcell_fqdn(workcell_path) # format workcell_fqdn from workcell_path, e.g. examples.hello_workcell.app:hello_workcell
        workcell_name = workcell_fqdn.split(":")[-1] # also function_name, "hello_workcell"
        workcell_version = workcell_version # "latest" | "v1.0.0" | "dev" | "prod"
        workcell_runtime = workcell_runtime # "python3.8" | "python3.9" 
        workcell_tags = "{}/{}:{}".format(username, workcell_name, workcell_version) # default build tag: {username}/{workcell_name}:{workcell_version}
    except:
        raise ValueError("The provided workcell_fqdn is not callable.")
    # pack config
    workcell_config = {
        "workcell_fqdn": workcell_fqdn,
        "workcell_name": workcell_name,
        "workcell_version": workcell_version,
        "workcell_runtime": workcell_runtime,
        "workcell_tags": workcell_tags,
        "workcell_env": "",
    }     
    return workcell_config


def save_workcell_config(workcell_config: dict, dest: str) -> None:
    """Save workcell config to a file.
    Args:
        workcell_config (dict): build config for workcell.
        dest (str): path to save workcell config.
            e.g. dest = "./build/workcell_config.json"
    Returns:
        None
    """
    with open(dest, "w") as f:
        json.dump(workcell_config, f, indent=4)
    return None