import extendable_json as json

serialization_key = 'VALUE'
serialization_value = "This is a Test"
serialized_test = "{\"%s\": \"%s\"}"%(serialization_key, serialization_value)

class TestObject():
    pass

@json.json_serialize.register(TestObject)
def serialize_test(val):
    return {serialization_key: serialization_value}

@json.json_deserialize.register(TestObject)
def deserialize_test(val):
    print(val)
    if serialization_key in val:
        return TestObject()
    return None

def test_decorator_serialize_registers():
    assert TestObject in json.json_serialize.registry.keys()
    assert json.json_serialize.registry[TestObject] == serialize_test

def test_decorator_deserialize_registers():
    assert TestObject in json.json_deserialize.registry.keys()
    assert json.json_deserialize.registry[TestObject] == deserialize_test

def test_serialization():
    obj = TestObject()
    assert json.dumps(obj) == serialized_test

def test_deserialization():
    obj = json.loads(serialized_test)
    assert isinstance(obj, TestObject)

def test_exception_serialization():
    try:
        raise Exception("Test")
    except Exception as e:
        #print(json.dumps(e))
        print(e.__dict__)
        assert False
