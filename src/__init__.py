# Copyright (c) 2021 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from typing import List

import click
from absolute_control import (get_all_processes, get_process_by_id,
                              get_processes_by_name, kill_all_processes,
                              kill_process_by_id, kill_processes_by_name,
                              open_process_using_command)


@click.group()
def cli():
    """
    A command line interface for controlling processes.
    """
    pass

@cli.group()
def processes():
    """
    Commands for controlling processes.
    """
    pass

@processes.command()
@click.option('--name', '-n', help='Filter processes by name.')
@click.option('--id', '-i', help='Filter processes by id.')
def get(name: str, id: int):
    """
    Get all processes.

    Args:
        name (str): Filter processes by name.
        id (int): Filter processes by pid.
    """
    processes = []

    if name:
        processes.extend(get_processes_by_name(name))
    
    if id:
        process = get_process_by_id(id)

        if process:
            processes.append(process)

    if not name and not id:
        processes = get_all_processes()

    for process in processes:
        click.echo(process)

@processes.command()
@click.option('--name', '-n', help='Filter processes by name.')
@click.option('--id', '-i', help='Filter processes by id.')
def kill(name: str, id: int):
    """
    Kill all processes.

    Args:
        name (str): Filter processes by name.
        id (int): Filter processes by pid.
    """
    if name:
        kill_processes_by_name(name)
    
    if id:
        kill_process_by_id(id)

    if not name and not id:
        kill_all_processes()

@processes.command()
@click.argument('command')
def open(command: str):
    """
    Open a process.
    """
    click.echo(open_process_using_command(command))
