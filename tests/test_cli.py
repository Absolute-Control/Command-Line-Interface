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
import re

from click.testing import CliRunner
from pytest import fixture
from src import get, kill, open


@fixture
def runner() -> CliRunner:
    """
    Fixture for click.testing.CliRunner

    Returns:
        CliRunner: A click.testing.CliRunner instance
    """
    return CliRunner()

def test_get_processes(runner: CliRunner) -> None:
    """
    Test the get command

    Args:
        runner (CliRunner): A click.testing.CliRunner instance
    """
    result = runner.invoke(get)

    assert result.exit_code == 0

def test_get_processes_with_pid(runner: CliRunner) -> None:
    """
    Test the get command with a pid

    Args:
        runner (CliRunner): A click.testing.CliRunner instance
    """
    result = runner.invoke(open, ['python3'])
    target_pid = (re
        .search(r'pid=\d+', result.output)
        .group()
        .replace('pid=', '')
    )

    result = runner.invoke(get, ['--id', target_pid])

    assert result.exit_code == 0

def test_get_process_with_name(runner: CliRunner) -> None:
    """
    Test the get command with a name

    Args:
        runner (CliRunner): A click.testing.CliRunner instance
    """
    result = runner.invoke(get, ['--name', 'python3'])

    assert result.exit_code == 0

def test_open_and_kill_process(runner: CliRunner) -> None:
    """
    Test the open and kill commands

    Args:
        runner (CliRunner): A click.testing.CliRunner instance
    """
    result = runner.invoke(open, ['python3'])
    target_pid = (re
        .search(r'pid=\d+', result.output)
        .group()
        .replace('pid=', '')
    )
    assert result.exit_code == 0

    result = runner.invoke(kill, ['--id', target_pid])

    assert result.exit_code == 0

def test_kill_all_processes(runner: CliRunner) -> None:
    """
    Test the kill command with no arguments

    Args:
        runner (CliRunner): A click.testing.CliRunner instance
    """
    result = runner.invoke(kill)

    assert result.exit_code == 0

def test_kill_process_by_name(runner: CliRunner) -> None:
    """
    Test the kill command with a name

    Args:
        runner (CliRunner): A click.testing.CliRunner instance
    """
    result = runner.invoke(open, ['python3'])

    assert result.exit_code == 0

    result = runner.invoke(kill, ['--name', 'python3'])

    assert result.exit_code == 0

    result = runner.invoke(get, ['--name', 'python3'])

    assert 'bash' not in result.output

def test_open_process_by_name(runner: CliRunner) -> None:
    """
    Test the open command with a name

    Args:
        runner (CliRunner): A click.testing.CliRunner instance
    """
    result = runner.invoke(open, ['python3'])

    assert result.exit_code == 0
    assert 'python3' in result.output

    result = runner.invoke(get, ['--name', 'python3'])

    assert 'python3' in result.output