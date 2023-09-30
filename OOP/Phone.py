from Product import Product

class Phone(Product):

    # super class
    def __init__(self, name: str, price: float, quantity=0,broken_phones=0):
        # Call super function to have access to all attributes / methods
        
        super().__init__(
            name, price, quantity
        )
        # Run Validations to the recived argiments
        assert broken_phones >= 0 ,f"Broken_phones {quantity} is not greator or equal to than zero"
        
        
        # Assign to self object | O'z-o'zini ob'ektga tayinlash

        self.broken_phones = broken_phones
        
        # Actions to execute | Amalga oshirish uchun harakatlar
              
# phone1 = Phone('jjdPhone20', 500, 5,1)
# # print(phone1.calculate_price_total())
# print(Product.all)
# print(Phone.all)








