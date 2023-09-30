# When to use class methods and when to use static methods ?


class Product:
    
    @staticmethod
    def is_integer(num):
        pass
    
    @classmethod
    def instantiate_from_something(cls):
        pass
    
product1 = Product
product1.is_integer(5)
product1.instantiate_from_something()