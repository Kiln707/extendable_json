import extendable_json as json

def test_serializing_exception():
    try:
        raise Exception("This is a test")
    except Exception as e:
        assert json.dumps(e) == "{\"type\": [\"builtins\", \"Exception\"], \"args\": [\"\\\"This is a test\\\"\"], \"attrs\": [], \"traceback\": \"Traceback (most recent call last):\\n  File \\\"D:\\\\Development\\\\extendable_json\\\\tests\\\\test_exceptions_json.py\\\", line 5, in test_serializing_exception\\n    raise Exception(\\\"This is a test\\\")\\nException: This is a test\\n\", \"kwargs\": {}}"

def test_deserializing_exception():
    try:
        raise Exception("This is a test")
    except Exception as e:
        import sys, traceback
        t, v, tb = sys.exc_info()
        tb = "".join(traceback.format_exception(t, v, tb))
        ex_j = json.dumps(e)
        ex = json.loads(ex_j)
        try:
            raise ex
        except Exception as f:
            assert type(e) is type(f)
            assert e.args == f.args
            assert tb == f.traceback
