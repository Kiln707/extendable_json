from functools import singledispatch
from datetime import datetime

@singledispatch
def json_serialize(val):
    """Used by default."""
    return str(val)

@json_serialize.register(datetime)
def json_datetime(val):
    if not val.tzinfo:
        from tzlocal import get_localzone
        tz = get_localzone()
        tz.localize(val)
    return { 'datetime': val.isoformat(), 'tz': val.tzinfo }

@json_serialize.register(Exception)
def json_exception(val):
    data = {}
    data['type'] = val.__class__
    data['val'] = val
    attributes = {}
    for attr, val in val.dict().items():
        attributes[attr] = val
    data['attributes'] = attributes
    return data

@json_serialize.register(object)
def json_object(val):
    data = {}
    data['type'] = val.__class__
    data['val'] = val
    attributes = {}
    for attr, val in val.dict().items():
        attributes[attr] = val
    data['attributes'] = attributes
    return data

@singledispatch
def json_deserialize(val):
    """Used by default."""
    return val

@json_deserialize.register(datetime)
def json_datetime(val):
    from datetime import datetime
    import pytz
    dt = datetime.fromisoformat(val['datetime'])
    tz = pytz.timezone(val['tzinfo'])
    tz.localize(dt)
    return dt

@json_deserialize.register(Exception)
def json_exception(val):
    obj = object()
    obj.__class__ = val['type']
    for attr, val in val['attributes'].items():
        setattr(obj, attr, val)
    return obj

@json_deserialize.register(object)
def json_object(val):
    obj = object()
    obj.__class__ = val['type']
    for attr, val in val['attributes'].items():
        setattr(obj, attr, val)
    return obj
