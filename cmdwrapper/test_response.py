import pytest
from cmdwrapper import run, response
from unittest.mock import MagicMock


def test_run():
    r = run(['python', '--version'], response.PythonVersion)
    assert r.returncode == 0
    assert r.major == 3


@pytest.mark.parametrize(
    "version,expected",
    [
        (b'Python 3.7.8\n', {'major': 3, 'minor': 7, 'micro': 8, 'qualifier': None, 'qualifier_version': None}),
        (b'Python 3.7.9b1\n', {'major': 3, 'minor': 7, 'micro': 9, 'qualifier': 'b', 'qualifier_version': 1}),
        (b'Python 3.7.10rc2\n', {'major': 3, 'minor': 7, 'micro': 10, 'qualifier': 'rc', 'qualifier_version': 2}),
        (b'Python 3.7.11a3\n', {'major': 3, 'minor': 7, 'micro': 11, 'qualifier': 'a', 'qualifier_version': 3})
    ]
)
def test_python_version(version, expected):
    mocked = MagicMock()
    mocked.stdout = version
    p = response.PythonVersion(mocked)
    for key, value in expected.items():
        assert getattr(p, key) == value