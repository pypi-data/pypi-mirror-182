from .repr_pyhandle import PyReprHandle
from google.protobuf.internal.enum_type_wrapper import EnumTypeWrapper


class PyEnumReprHandle(PyReprHandle):
    def __init__(self, **enum_infos):
        self._enum_infos = {enum_attr: enum_type for enum_attr, enum_type in enum_infos.items() if
                            isinstance(enum_type, EnumTypeWrapper)}
        super().__init__()

    def _init_pyattr_map(self):
        super(PyEnumReprHandle, self)._init_pyattr_map()
        for enum_attr in self._enum_infos:
            self._get_pyattr_map[enum_attr] = self._get_enum_name

    def _get_enum_name(self, obj, attr):
        enum_val = getattr(obj, attr)
        if enum_val is None:
            return enum_val
        enum_type = self._enum_infos.get(attr, None)
        if enum_type:
            return enum_type.Name(enum_val)
        return enum_val
