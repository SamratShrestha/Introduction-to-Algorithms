from typing import Any
from warnings import warn

def ci_lookup(d:dict[str,Any],key:str)->Any:
    ...

def __getattr__(name:str):
    if name == "get_ci":
        warn(f'{name} is deprecated',DeprecationWarning)
        return ci_lookup
    raise AttributeError("f{__name__} does not have attribute {name}")

