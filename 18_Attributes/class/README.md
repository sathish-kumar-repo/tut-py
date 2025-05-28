# Class Attributes

Class attributes belong to the class itself they will be shared by all the instances. Such attributes are defined in the class body parts usually at the top, for legibility.

## getattr ( object , name [ , default ] )

- object => object whose named attribute's value is to be returned.
- name => string that contains the attribute's name.
- default ( Optional ) => The value is returned when the named attribute is not found

## setattr( object , name , value )

- object => object whose named attribute value is to be assigning.
- name => The assigned variable name
- default => The assigned variable value.

## delattr( object , name )

- object => object whose named attribute value is to be removed.
- name => The attribute which is to be removed.

> MappingProxyType . This type is a read-only proxy for a dict or other mapping. Python uses this type internally for important dictionaries, which is why you can't monkey-patch built-in types willy-nilly. The only change in Python 3.3 was to expose this type for user code.05
