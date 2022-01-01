from collections import UserDict
from typing import Any

class CaseInsensitiveDict(UserDict):
    def __setitem__(self,key:str,value:Any):
        return super().__setitem__(key.lower(),value)

    def __getitem__(self,key:str):
        return super().__getitem__(key.lower())

    def __delitem__(self,key:str):
        return super().__delitem__(key.lower())



headers = CaseInsensitiveDict({
    'Content-Type': 'application/json',
    'Content-Length': 10
})

print(headers['CONTENT-TYPE'])
print(headers['content-length'])
