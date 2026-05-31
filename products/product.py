from products import food_package as fp
from abc import ABC, abstractmethod
#Write your code here

class Product(ABC):
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self):
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        pass
    @abstractmethod
    def foodPackage(self)->FoodPackage:
        pass  

class Hamburger(Product):
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburguesa"
    def foodPackage(self) -> FoodPackage:
        return fp.Wrapping()
        
class Soda(Product):
    def __init__(self, id, name, price):
        super().__init__(id, name, price)
    def type(self):
        return "Soda"
    def foodPackage(self):
        return fp.Bottle()


class Drink(Product):
    def __init__(self, id, name, price):
        super().__init__(id, name, price)
    def type(self):
        return "Drink"
    def foodPackage(self):
        return fp.Glass()
   

class HappyMeal(Product):
    def __init__(self, id, name, price):
        super().__init__(id, name, price)
    def type(self):
        return "Happy Meal"
    def foodPackage(self):
        return fp.Box()
    