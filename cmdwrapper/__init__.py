import subprocess
from cmdwrapper import response


def run(command: list, parser: response.ResponseBase, **run_kwargs) -> response.ResponseBase:
    """
        r = cmdwrapper.run(['python', '--version'], PythonVersion)
        r.major  # 3
    """
    if 'capture_output' not in run_kwargs:
        run_kwargs['capture_output'] = True
    completed = subprocess.run(command, **run_kwargs)
    return parser(completed)


__all__ = ['run', 'response']