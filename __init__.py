from xspf import *
from xspf import Xspf as XspfBase
from xspfparser import parse as _xspf_parse

class Xspf(XspfBase):
    def __init__(self, *args, **kargs):
        super(Xspf, self).__init__(*args, **kargs)

    @classmethod
    def loads(cls, file_path):
        res = _xspf_parse(file_path)
        return cls(res)
