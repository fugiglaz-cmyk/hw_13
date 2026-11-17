import inspect


class ObjectAnalyzer:
    """Universal Python object analyzer.
    Attributes:
        obj: The object being analyzed.
    """

    def __init__(self, obj):
        """Stores the object for further analysis.
        Args: Any Python object
        """
        self.obj = obj

    def get_type(self):
        """Returns the name of the object's type.
        Returns: The class name of the object
        """
        return type(self.obj).__name__

    def get_attributes(self):
        """Returns a list of the object's attributes.
        Returns: Names of regular attributes
        """
        return [n for n in dir(self.obj)
                if not (n.startswith("__") and n.endswith("__"))
                and not callable(getattr(self.obj, n))]

    def get_methods(self):
        """Returns a list of the object's method names.
        Returns:: Method names
        """
        result = []
        methods = inspect.getmembers(
            self.obj,
            predicate=inspect.ismethod)
        for name, method in methods:
            result.append(name)
        return result

    def get_inheritance(self):
        """Returns the object's inheritance hierarchy.
        Returns: Class names from the class itself up to object
        """
        cls = self.obj if inspect.isclass(self.obj) else type(self.obj)
        return [c.__name__ for c in cls.__mro__]

    def get_documentation(self):
        """Returns the object's documentation (docstring).
        Returns:The cleaned documentation text
        """
        return inspect.getdoc(self.obj)

    def get_attribute(self):
        """Asks the user for an attribute name and returns its value.
        Returns:
            Any: The attribute value, if it exists.
            str: The string 'Attribute not found' if the attribute is missing.
        """
        attribute = input("Enter attribute name you want to have: ")
        if hasattr(self.obj, attribute):
            return getattr(self.obj, attribute)
        return "Attribute not found"

    def set_attribute(self):
        """Asks the user for a name and value and sets the attribute.
        Returns: The message 'Attribute set successfully'.
        """
        name = input("Enter attribute name you want to set: ")
        value = input("Enter new attribute value: ")
        setattr(self.obj, name, value)
        return f"Attribute set successfully"

    def analyze(self):
        """Builds and prints a report about the object.

        Prints the type, attributes, methods, inheritance and documentation
        with labeled sections. Returns nothing.
        """
        print("Type: ", self.get_type())
        print("Attributes: ", self.get_attributes())
        print("Methods: ", self.get_methods())
        print("Inheritance:", self.get_inheritance())
        print("Documentary: ", self.get_documentation())


class TestObject:
    """Test class for demonstrating how ObjectAnalyzer works.
    Attributes:
        name: The name.
        age: The age.
    """

    def __init__(self, name, age):
        """Creates an object with a name and an age.
        Args:
            name: The name.
            age: The age.
        """
        self.name = name
        self.age = age

    def say_hello(self):
        """Returns a greeting.
        Returns:
            str: The string 'Hello World'.
        """
        return "Hello World"


object1 = TestObject("Alex", 18)

analyzer = ObjectAnalyzer(object1)
analyzer.analyze()
# print(analyzer.get_attribute())
# print(analyzer.set_attribute())