# cmdwrapper

[![CircleCI](https://circleci.com/gh/ograycode/cmdwrapper/tree/master.svg?style=svg)](https://circleci.com/gh/ograycode/cmdwrapper/tree/master)

cmdwrapper aims to establish a pattern for working with CLI tools that is inspired by the requests library.

## Why

There is a plethora of CLI tooling out there but it can be really hard to work with in a progromatic way. Most tools use stdout to communicate with the user and exit codes to communicate if there was an error -- but some programs use exit codes to also communicate, or don't use exit codes properly.

So by providing a pattern, all CLI tooling has the potential to have easy to use interfaces from your python code.

## Extending

The `cmdwrapper.response.BaseResponse` is intended to be inherited from to create your own response types. See `PythonVersion` as example of using it.

## Sample Usage

```python
from cmdwrapper import run, response

r = run(['python', '--version'], response.PythonVersion)
r.check_returncode()
assert r.major == 3
```

Also see `response.py` and `test_response.py`