from .base_handle import ConfigHandleBase
from ..protobuf_wrapper import ProtoMapWrapper


class MapConfigHandle(ConfigHandleBase):
    def __init__(self, **attrs_map):
        self._attrs_map = attrs_map

    def PreToProto(self, pyobj, pbobj):
        return pyobj, ProtoMapWrapper(pbobj, self._attrs_map)

    def PostToProto(self, pbobj):
        if hasattr(pbobj, "getproto"):
            return pbobj.getproto()
        return pbobj

    def PreToPyobj(self, pbobj, pyobj):
        return ProtoMapWrapper(pbobj, self._attrs_map), pyobj

    def PostToPyobj(self, pyobj):
        return pyobj
