import dataclasses


def get_dataclass_attrs(dataclass):
    datacls_fields = getattr(dataclass, "__dataclass_fields__", None)
    if datacls_fields:
        return tuple(f.name for f in datacls_fields.values() if f._field_type is dataclasses._FIELD and f.repr)
    all_attrs = dir(dataclass)
    return tuple(filter(lambda x: not x.startswith("_") and not callable(getattr(dataclass, x)), all_attrs))


def get_protoclass_attrs(protoclass, wrap=False):
    if wrap:
        return [field.name for field in protoclass.getattr("DESCRIPTOR", _raise=True).fields]
    return [field.name for field in getattr(protoclass, "DESCRIPTOR").fields]
