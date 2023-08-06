"""Command line interface."""

import os
import sys
import json
import requests
import dotenv
import typer
from pydantic.error_wrappers import ValidationError
from workcell.utils.export import ExportFormat
from workcell.core import Workcell


# Init weanalyze config directory
weanalyze_config_dir = os.path.join(os.path.expanduser("~"), ".weanalyze")
if not os.path.exists(weanalyze_config_dir):
    os.mkdir(weanalyze_config_dir)
# Init environment variables
weanalyze_dotenv =  os.path.join(os.path.expanduser("~"), ".weanalyze", "env")
if not os.path.exists(weanalyze_dotenv):
    with open(weanalyze_dotenv, "w") as f:
        f.write("WORKCELL_GATEWAY='http://fun.weanalyze.co'" + "\n")
        f.write("WORKCELL_USERNAME=''" + "\n")
        f.write("WORKCELL_TOKEN=''" + "\n")
dotenv.load_dotenv(weanalyze_dotenv)
# Typer command
cli = typer.Typer()


@cli.command()
def new(
    workcell_name: str,
    workcell_runtime: str = typer.Option("python3", "--runtime", "-r")
) -> None:
    """Init a new workcell template.

    This will create a template dir for workcell deployment.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path
    sys.path.append(os.getcwd())
    return None


@cli.command()
def serve(
    workcell_path: str,
    port: int = typer.Option(8080, "--port", "-p"),
    host: str = typer.Option("0.0.0.0", "--host", "-h"),
) -> None:
    """Start a HTTP API server for the workcell.

    This will launch a FastAPI server based on the OpenAPI standard and with a automatic interactive documentation.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path
    sys.path.append(os.getcwd())
    from workcell.api.fastapi_app import launch_api  # type: ignore
    launch_api(workcell_path, port, host)
    return None


@cli.command()
def serve_ui(
    workcell_path: str,
    port: int = typer.Option(8080, "--port", "-p"),
    host: str = typer.Option("0.0.0.0", "--host", "-h"),
) -> None:
    """Start a UI server for the workcell.

    This will launch a Streamlit server based on the Pydantic standard.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path
    sys.path.append(os.getcwd())
    from workcell.ui.streamlit_ui import launch_ui  # type: ignore
    launch_ui(workcell_path, port, host)
    return None


@cli.command()
def login(
    username: str = typer.Option("", "--username", "-u"),
    password: str = typer.Option("", "--password", "-p"),
) -> None:
    """Login into fun.weanalyze.co."""
    
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path

    # Verification
    try:    
        if ('WORKCELL_TOKEN' in os.environ) and (os.getenv("WORKCELL_TOKEN") != ""):
            typer.secho("Already logged in ! (username: {})".format(os.environ['WORKCELL_USERNAME']), fg=typer.colors.GREEN, err=False)
            return None
        else:
            if (username == "") and (password == ""):
                typer.secho("Please provide username and password.", fg=typer.colors.RED, err=True)
                return None
            elif password == "":
                password = typer.prompt("Password", hide_input=True)
                # login params
                headers = {'Content-Type': 'application/x-www-form-urlencoded'}            
                data = {
                    'username': username,
                    'password': password
                } 
                # login url
                url = os.getenv("WORKCELL_GATEWAY") + "/user/token"
                # login request   
                response = requests.post(url=url, data=data, headers=headers)
                if response.status_code == 200:
                    # extract token
                    token_value = response.json()["access_token"]
                    dotenv.set_key(weanalyze_dotenv, "WORKCELL_USERNAME", username)
                    dotenv.set_key(weanalyze_dotenv, "WORKCELL_TOKEN", token_value)
                    typer.echo("Login successful! (username: {}).".format(username))
                else:
                    typer.echo("Login failed! ({}).".format(response.text), fg=typer.colors.RED, err=True) 
            else:
                pass
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)
    return None


@cli.command()
def pack(
    workcell_path: str,
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_runtime: str = typer.Option("python3.8", "--runtime", "-r")
) -> str:
    """Prepare deployment package for workcell.
    This will create a deployment folder and package in build_path.
    Args:
        workcell_path (str): path to workcell.
            e.g. workcell_path = "./examples/hello_workcell/app.py"
        workcell_version (str): workcell version.
            e.g. workcell_version = "latest"
        workcell_runtime (str): workcell template.
            e.g. workcell_runtime = "python3.8"
    Return:
        build_dir (str): path to build_dir.
        workcell_config (dict): dict of build config.
    """
    from workcell.utils.builder import clear_builder, copy_builder, env_builder, zip_builder
    from workcell.utils.gen_config import gen_workcell_config, save_workcell_config
    workcell_config = gen_workcell_config(
        workcell_path,
        workcell_version,
        workcell_runtime
    )
    # copy from template and function
    files_path = os.path.join(os.getcwd(), *workcell_config['workcell_fqdn'].split(":")[0].split(".")[:-1]) # "./examples/hello_world"
    template_file = os.path.join(os.getcwd(), "workcell", "templates", "aws", "app.py")
    build_dir = os.path.join(os.getcwd(), "build") # "./build"
    function_dir = os.path.join(build_dir, "function") # "./build/function
    package_dir = os.path.join(build_dir, "package") # "./build/package"
    workcell_config_file = os.path.join(package_dir, "workcell_config.json") # "./build/package/workcell_config.json"
    # clear build dir
    clear_builder(
        dest = build_dir
    )
    # copy function file in function_dir
    copy_builder(
        src = files_path, 
        dest = function_dir,
        clear_before_copy = True
    )
    # call env builder to build lambda function dependencies.
    env_builder(
        src = function_dir, 
        dest = package_dir
    )
    # copy function file into package_dir/function
    copy_builder(
        src = function_dir,
        dest = os.path.join(package_dir, "function"), 
        clear_before_copy = False
    )
    # copy template file into package_dir
    copy_builder(
        src = template_file,
        dest = package_dir, 
        clear_before_copy = False
    ) 
    # save workcell_config into package_dir
    save_workcell_config(workcell_config, workcell_config_file)
    # zip package files
    zip_builder(
        src = package_dir,
        dest = package_dir
    )
    typer.secho("Workcell buil env complete!", fg=typer.colors.GREEN)
    return package_dir


@cli.command()
def deploy(
    workcell_path: str,
    workcell_version: str = typer.Option("latest", "--version", "-v"),
    workcell_runtime: str = typer.Option("python3", "--template", "-t"), 
) -> None:
    """Deploy a workcell to weanalyze cloud.
    This will deploy a workcell to weanalyze cloud.
    Args:
        workcell_path (str): path to workcell.
            e.g. workcell_path = "./examples/hello_workcell"
        workcell_version (str): workcell version.
            e.g. workcell_version = "latest"
        workcell_runtime (str): workcell template.
            e.g. workcell_runtime = "python3"
    Return:
        None.
    """
    # Add the current working directory to the sys path
    # This is required to resolve the workcell path
    sys.path.append(os.getcwd())
    # Verification
    try:    
        if ('WORKCELL_TOKEN' in os.environ) and (os.getenv("WORKCELL_TOKEN") != ""):
            # build 
            build_dir, workcell_config = pack(
                workcell_path,
                workcell_version,
                workcell_runtime
            )
            # auth params
            headers = {
                "Authorization": "Bearer {}".format(os.getenv("WORKCELL_TOKEN")),
            } 
            # auth url 
            url = os.getenv("WORKCELL_GATEWAY") + "/{}/deploy".format(os.getenv("WORKCELL_USERNAME"))            
            # post package to weanalyze cloud
            tar_file = os.path.join(build_dir,'tmp.tar.gz')
            with open(tar_file, "rb") as f:
                # request    
                response = requests.post(
                    url=url, 
                    headers=headers, 
                    data={'workcell_config':json.dumps(workcell_config)},
                    files={"workcell_tarfile": f}
                )
            # parse 
            # try:
            #     result = response.json()
            #     typer.echo("Workcell status: {}".format(response.text))
            # except:
            #     result = {"status": "error", "message": response.text}
            #     typer.echo("Workcell deploy failed! {}".format(result))
            result = response.text
            typer.echo("Workcell status: {}".format(response.text))            
        else:
            typer.secho("Login required!", fg=typer.colors.RED, err=True)
    except ValidationError as ex:
        typer.secho(str(ex), fg=typer.colors.RED, err=True)
    

@cli.command()
def export(
    workcell_path: str, export_name: str, format: ExportFormat = ExportFormat.ZIP
) -> None:
    """Package and export a workcell."""
    if format == ExportFormat.ZIP:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.DOCKER:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )
    elif format == ExportFormat.WE:
        typer.secho(
            "[WIP] This feature is not finalized yet. You can track the progress and vote for the feature here: ",
            fg=typer.colors.BRIGHT_YELLOW,
        )


if __name__ == "__main__":
    cli()