from abc import ABC, abstractmethod

# Base Pizza Interface
class Pizza(ABC):
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass

# Concrete Base Pizzas
class Margherita(Pizza):
    def get_description(self) -> str:
        return "Margherita"

    def get_cost(self) -> float:
        return 5.0

class Farmhouse(Pizza):
    def get_description(self) -> str:
        return "Farmhouse"

    def get_cost(self) -> float:
        return 7.0

# Topping Decorator
class ToppingDecorator(Pizza, ABC):
    def __init__(self, pizza: Pizza):
        self.pizza = pizza

# Concrete Toppings
class Cheese(ToppingDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Cheese"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 1.0

class Tomato(ToppingDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Tomato"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 0.5

class Jalapeno(ToppingDecorator):
    def get_description(self) -> str:
        return self.pizza.get_description() + ", Jalapeno"

    def get_cost(self) -> float:
        return self.pizza.get_cost() + 0.75

# Example Usage
if __name__ == "__main__":
    # Customer wants a Farmhouse with Cheese and Jalapeno
    my_pizza = Farmhouse()
    my_pizza = Cheese(my_pizza)
    my_pizza = Jalapeno(my_pizza)

    print("Order:", my_pizza.get_description())
    print("Total Cost: $", my_pizza.get_cost())