# Abstract Base Class

An Abstract Base Class (ABC) in Python is a special type of class that provides an interface to define the expected behaviors of its subclasses, but cannot be instantiated on its own.

An ABC is created using the abc module, which is part of the Python Standard Library. To create an ABC, a class is derived from ABC and one or more abstract methods are declared using the @abstractmethod decorator. Subclasses of an ABC must override these abstract methods, or they too will be treated as abstract and cannot be instantiated.

ABCs are used to define a common interface for related classes, so that it is easier to write generic code that works with objects of different types, as long as they adhere to the expected interface. This can help enforce modularity and reduce code duplication, and make it easier to maintain code and add new features.

> Note: In Simple, set of rules to create, then this rules are follow or implemention all other class
