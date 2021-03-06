# Extendable JSON

Extendable JSON is an extendable drop in replacement of Python’s JSON library.
By using @json_serialize and @json_deserialize decorators to enable custom objects
not normally serializable by default.

This library includes the ability to serialize Exceptions, Objects, and Datetime objects by default.


---

Usage:

```
import extendable_json as json
json.dumps({"Key": "Value"})
```

outputs: “{“Key”: “Value”}” as string

```
import extendable_json as json
json.loads('"{"Key": "Value"}"')
```

outputs: {“Key”: “Value”} as dict


---

To extend serialization to objects not normally serializable or customize serialization of an object,
decorate a function accepting a single value with @json_serialize.register giving the object to serialize
with this function.
Return a dict containing keys and values  of the object.

```
@json_serialize.register(MyObject)
def serialize_my_object(val):
    return {"Attrib": str(val.attrib)}
```

Reverse this by decorating a function accepting a single value with @json_deserialize.register.
Using val as a dictionary, extract the serialized data into a new object loading with data from val.
Return the newly created object.

```
@json_deserialize.register(MyObject)
def deserialize_my_object(val):
    myObject = MyObject()
    myObject.attrib = val['Attrib']
    return myObject
```

## Exceptions

Exceptions may be serialized or deserialized.

Exceptions may be serialized within try/except block

```
try:
    # Exception thrown
except Exception as e:
    import extendable_json as json
    json.dumps(e)
```

Once deserialized exceptions may be raised and/or the Traceback
is available with the traceback attr.

```
e = json.loads(exeption_json)
raise e #To raise exception
print(e.traceback) #To print traceback
```

## API Reference

> 
> ### extendable_json.dump(obj, fp, \*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=_JSONDecoder, indent=None, separators=None, default=None, sort_keys=False, \*\*kw)
> Use exactly as [Python’s JSON](https://docs.python.org/3/library/json.html).

> Please note that using the cls kwarg will disable this library’s functionality


> ### extendable_json.dumps(obj, \*, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=_JSONDecoder, indent=None, separators=None, default=None, sort_keys=False, \*\*kw)
> Use exactly as [Python’s JSON](https://docs.python.org/3/library/json.html).

> Please note that using the cls kwarg will disable this library’s functionality


> ### extendable_json.load(fp, \*, cls=_JSONEncoder, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, \*\*kw)
> Use exactly as [Python’s JSON](https://docs.python.org/3/library/json.html).

> Please note that using the cls kwarg will disable this library’s functionality


> ### extendable_json.loads(s, \*, cls=_JSONEncoder, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, \*\*kw)
> Use exactly as [Python’s JSON](https://docs.python.org/3/library/json.html).

> Please note that using the cls kwarg will disable this library’s functionality


> ### @extendable_json.json_serialize(object)
> Decorator used to add objects to serialization registry.
> Please see above documentation on how to use.


> ### @extendable_json.json_deserialize(object)
> Decorator used to add objects to deserialization registry.
> Please see above documentation on how to use.

# Indices and tables


* Index


* Module Index


* Search Page
