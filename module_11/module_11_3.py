# Домашнее задание по теме "Интроспекция"


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr))],
        'methods': [attr for attr in dir(obj) if callable(getattr(obj, attr))],
        'module': __name__,
        'hash': getattr(obj, "__hash__", "None")
    }

class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value

number_info = introspection_info(42)
print(number_info)

my_object = MyClass(42)
number_info = introspection_info(my_object)
print(number_info)