import os
import sys

from uvbump import PythonInfo, uvbump
from uvbump._core import format_python_info


def test_uvbump():
    result = uvbump()
    assert isinstance(result, PythonInfo)
    assert result.version == sys.version
    assert result.executable_path == sys.executable
    assert os.path.isabs(result.script_path)


def test_format_python_info():
    info = PythonInfo(
        version="3.9.0",
        executable_path="/usr/bin/python3",
        script_path="/path/to/script.py",
    )
    formatted = format_python_info(info)
    assert "Python Version: 3.9.0" in formatted
    assert "Executable Path: /usr/bin/python3" in formatted
    assert "Script Path: /path/to/script.py" in formatted
