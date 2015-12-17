from storable_class import container
from storable_class import attribute 

class TestNestedClass(container.Container):

    test = attribute.GenericAttr()
    testNest = attribute.GenericAttr()
    test2 = attribute.GenericAttr()
    test3 = attribute.GenericAttr()
    test4 = attribute.TypedAttr(["float"],10.0)

    def __init__(self):
        container.Container.__init__(self)


def get_instance():
    return TestNestedClass()