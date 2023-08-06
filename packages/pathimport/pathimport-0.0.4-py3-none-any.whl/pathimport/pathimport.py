import sys
import inspect
from pathlib import Path


def set_module_root(relative_path: str, prefix: bool = True) -> None:
    """
    Add a module to a path to enable relative imports.

    Parameters
    ----------
    relative_path : Path
        Relative path to the root of the module
    prefix : bool
        If True the name of the module/project should
        be prepended for each internal import, by default True.
    """
    # checking the function stack to obtain the
    # caller Path
    caller_path = Path((inspect.stack()[1])[1]).resolve()

    # calculating module path
    relative_path = caller_path.parent / Path(relative_path)
    
    if prefix:
        relative_path = relative_path.resolve().parent

    # prepending the module to PATH
    sys.path = [str(relative_path)] + sys.path
