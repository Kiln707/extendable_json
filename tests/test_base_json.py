import extendable_json as json

"""
This file is to ensure that base json functionality is preserved.
"""
def test_dump_str():
    assert json.dumps('test') == '"test"'

def test_load_str():
    assert json.loads('"test"') == "test"

def test_dump_int():
    assert json.dumps(1) == '1'

def test_load_int():
    assert json.loads('1') == 1

def test_dump_float():
    assert json.dumps(1.1) == '1.1'

def test_load_float():
    assert json.loads('1.1') == 1.1

def test_dump_boolean_true():
    assert json.dumps(True) == 'true'

def test_load_boolean_true():
    assert json.loads('true') == True

def test_dump_boolean_false():
    assert json.dumps(False) == 'false'

def test_load_boolean_false():
    assert json.loads('false') == False

def test_dump_none():
    assert json.dumps(None) == 'null'

def test_load_none():
    assert json.loads('null') == None

def test_dump_list():
    assert json.dumps([1,2,3]) == '[1, 2, 3]'

def test_load_list():
    assert json.loads('[1,2,3]') == [1,2,3]

def test_dump_tuple():
    assert json.dumps((1,2,3)) == '[1, 2, 3]'

def test_load_tuple():
    assert tuple(json.loads('[1,2,3]')) == (1,2,3)

def test_dump_dict():
    assert json.dumps({'test':'test'}) == '{"test": "test"}'

def test_load_dict():
    assert json.loads('{"test":"test"}') == {'test':'test'}
