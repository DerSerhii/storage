"""
First custom metaclass
"""


class Meta(type):
    def __init__(cls, name, bases, namespace):
        super(Meta, cls).__init__(name, bases, namespace)
        print("Creating new class: {}".format(cls))

    def __call__(cls):
        new_instance = super(Meta, cls).__call__()
        print("Class {} new instance: {}".format(cls, new_instance))
        return new_instance


class C(metaclass=Meta):
    pass
# Creating new class: <class '__main__.C'>


c = C()
# Class <class '__main__.C'> new instance: <__main__.C object at 0x10e99ae48>

print(c)
# <__main__.C object at 0x10e99ae48>


