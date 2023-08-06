from .pyintenc import bpeEncode, bpeDecode, neEncode, neDecode 
from dataclasses import dataclass
from typing import Any, List

class IntecExecption(Exception):
    pass
class IntecTypeError(IntecExecption):
    pass
class IntecKindError(IntecExecption):
    pass

def ensureType(obj: Any, t: type) -> None:
    if type(obj) != t:
        raise IntecTypeError(
            f"Invalid type \"{type(obj)}\" for object, expected \"{t}\""
        )

@dataclass
class EncodedBytes:
    data: bytes
    length: int
    etype: str
    def decode(self) -> List[int]:
        ensureType(self.data, bytes)
        ensureType(self.length, int)
        if self.etype == "bpe":
            return bpeDecode(self.data, self.length)
        elif self.etype == "ne":
            return neDecode(self.data, self.length)
        else:
            raise IntecKindError(f"Unrecognized encoding type \"{etype}\"")
    

def encode(ints: List[int], etype: str = "ne") -> EncodedBytes:
    ensureType(ints, list)
    for i in ints:
        
        ensureType(i, int)
        assert i >= 0
    if etype == "bpe":
        return EncodedBytes(*bpeEncode(ints), etype)
    elif etype == "ne":
        return EncodedBytes(*(neEncode(ints)), etype)
    else:
        raise IntecKindError(f"Unrecognized encoding type \"{etype}\"")
        
def decode(data: bytes, length: int, etype: str = "ne") -> List[int]:
    obj = EncodedBytes(data, length, etype)
    return obj.decode()


