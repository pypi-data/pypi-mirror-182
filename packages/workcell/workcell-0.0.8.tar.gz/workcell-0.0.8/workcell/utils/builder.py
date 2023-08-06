import argparse
import subprocess
import hmac
import json
import os
import sys
import shutil
import tarfile
import click
import docker
from docker import APIClient


def clear_builder(dest) -> None:
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(dest)


def copy_builder(src: str, dest: str, clear_before_copy: bool=True) -> None:
    """Wrap user function in template

    Args:
        src (str): a folder to user defined function.
            e.g. src = "./examples/hello-workcell"
        dest (str): path to wrap user function into build folder.
            e.g. dest = "./build/function"

    Returns:
        None: mkdir for builder folder.    
    """

    if not os.path.exists(dest):
        os.makedirs(dest)
    else:
        if clear_before_copy:
            shutil.rmtree(dest)
            os.makedirs(dest)
    
    try:
        if os.path.isfile(src):
            # copy file
            shutil.copy(src, dest)
        else:
            # copy folder
            #filename = src.split('/')[-1] # TODO: validation
            #shutil.copytree(src, os.path.join(dest, filename), symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
            shutil.copytree(src, dest, symlinks=False, ignore=None, ignore_dangling_symlinks=False, dirs_exist_ok=True)
    except Exception as e:
        raise Exception("Copy builder failed! {}".format(e))


def zip_builder(src: str, dest: str) -> None:
    """Wrap user function in template

    Args:
        src (str): path to wrap user function into build folder.
            e.g. build_dir = "./build"
        dest (str): path to a tmp tar file.
            e.g. tar_file = "./build/tmp", will convert to "./build/tmp.zip"
    Returns:
        None: _description_
    """
    shutil.make_archive(dest, 'zip', src)


def env_builder(src: str, dest: str) -> None:
    """Creates a Lambda deployment package, by pip or pyenv. 
    This file should be zipped and passed directly to Lambda when creating the function.

    Args:
        src (str): path to wrap user function into build folder.
            e.g. src = "./build/{workcell_foldername}"
        dest (str): path to a tmp zip file.
            e.g. dest = "./build/package" | os.path.join(src, 'package')
    Returns:
        None: _description_
    """
    # requirements path
    function_dir = src
    package_dir = dest
    requirements_file = os.path.join(function_dir, 'requirements.txt')
    # running pip3 for dependencies.
    cmd = [
        'pip3', 'install', 
        '-r', requirements_file, 
        '--target', package_dir
    ]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    with process.stdout:
        log_subprocess_output(process.stdout)
    exitcode = process.wait() # 0 means success
    if exitcode != 0:
        raise Exception(f"Build function failed! {process.stdout}")
    return None


def image_builder(src: str, tags: str, client: APIClient = None) -> None:
    """Wrap user function in template

    Args:
        src (str): path contains Dockerfile to wrap user function into build folder.
            e.g. build_path = "./build/hello-workcell"
        tags (str): image tag.
            e.g. tags = "workcell:latest"

    Returns:
        None: docker images.
    """
    # check docker client
    if client is None:
        # client = docker.from_env()
        client = docker.APIClient()
    # docker build path
    click.echo("Building docker path: {}".format(src))
    log_generator = client.build(path=src, tag=tags, decode=True)
    log_docker_output(log_generator, "Build workcell docker image: {}".format(tags))


def image_pusher(repository: str, client: APIClient = None) -> None:
    """Push docker image to docker hub
    """
    # check docker client
    if client is None:
        # client = docker.from_env()
        client = docker.APIClient()
    # docker push
    log_generator = client.push(repository=repository, stream=True, decode=True)
    log_docker_output(log_generator, "Pushing workcell docker image to docker hub: {}".format(repository))


def log_subprocess_output(pipe):
    """
    Log output to console from a generator returned from subprocess
    :param pipe: The pipe to log the output of (e.g. subprocess.PIPE)
    """    
    for line in iter(pipe.readline, b''): # b'\n'-separated lines
        click.echo(f'Running subprocess command: {line.decode("utf-8").strip()}. ')


def log_docker_output(generator, task_name: str = 'docker command execution') -> None:
    """
    Log output to console from a generator returned from docker client
    :param Any generator: The generator to log the output of
    :param str task_name: A name to give the task, i.e. 'Build database image', used for logging
    """
    while True:
        try:
            output = generator.__next__()
            if 'stream' in output:
                if output['stream'] != '\n':
                    output_str = output['stream'].strip('\r\n').strip('\n')
                    click.echo(output_str)
        except StopIteration:
            click.echo(f'{task_name} complete.')
            break
        except ValueError:
            click.echo(f'Error parsing output from {task_name}: {output}')