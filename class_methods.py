class ClassTest:
    class_property = "Hello from class property"
    def instance_method(self):
        print(f"Called instance_method of {self}")

    @classmethod
    def class_method(cls):
        print(f"Called class_method {cls}")

    @staticmethod
    def static_method():
        print(f"Static method called ")

ClassTest.class_method()
ClassTest.static_method()
print(ClassTest.class_property)
