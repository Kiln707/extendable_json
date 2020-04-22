Welcome to Extendable JSON's documentation!
===========================================

.. automodule:: extendable_json
    :members:

===========================================
API Reference
===========================================

    .. autofunction:: dump(obj, fp, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=_JSONDecoder, indent=None, separators=None, default=None, sort_keys=False, **kw)

    .. autofunction:: dumps(obj, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=_JSONDecoder, indent=None, separators=None, default=None, sort_keys=False, **kw)

    .. autofunction:: load(fp, *, cls=_JSONEncoder, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

    .. autofunction:: loads(s, *, cls=_JSONEncoder, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw)

    .. autodecorator:: json_serialize(object)

    .. autodecorator:: json_deserialize(object)

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
