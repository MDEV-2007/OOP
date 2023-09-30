import csv

# parent class
class Product:
    pay_rate = 0.8 # The pay rate after 20% discount | 20% chegirmadan keyin to'lov stavkasi
    all = []
    def __init__(self, name: str, price: float, quantity=0):
        # Run Validations to the recived argiments
        
        assert price >= 0, f"Price {price} is not greator than or equal to zero"
        assert quantity >= 0 ,f"Quantity {quantity} is not greator or equal to than zero"
        
        
        # Assign to self object | O'z-o'zini ob'ektga tayinlash

        self._name  = name
        self.price = price
        self.quantity = quantity
        
        # Actions to execute | Amalga oshirish uchun harakatlar
        
        Product.all.append(self)
    
    @property
    # Property Decorator  = Read_Only Atribute
    def name(self):
        print("You are trying to get name")
        return self.__name

    @name.setter
    def name(self, vaule):
        self.__name = vaule
    
        
    def calculate_price_total(self):
        return self.price * self.quantity
    
    def apply_discount(self):
        self.price = self.price * self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            products = list(reader)
            
            for product in products:
                Product(
                    name=product.get('name'),
                    price=float(product.get('price')),
                    quantity=int(product.get('quantity')),
                )
    # number int float detect
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e : 5.0, 10.0
        
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num ,int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

# print(Product.is_integer(20.0))
# Product.instantiate_from_csv()
# print(Product.all)