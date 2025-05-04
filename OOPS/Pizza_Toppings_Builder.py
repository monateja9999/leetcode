# Product class: Pizza
class Pizza:
    def __init__(self, base: str):
        self.base = base
        self.toppings = []

    def add_topping(self, topping: str, cost: float):
        self.toppings.append((topping, cost))

    def get_description(self) -> str:
        desc = self.base
        if self.toppings:
            desc += " with " + ", ".join(t[0] for t in self.toppings)
        return desc

    def get_cost(self) -> float:
        base_prices = {
            "Margherita": 5.0,
            "Farmhouse": 7.0,
            "Peppy Paneer": 6.5,
        }
        base_cost = base_prices.get(self.base, 5.0)
        toppings_cost = sum(t[1] for t in self.toppings)
        return base_cost + toppings_cost

# Builder class
class PizzaBuilder:
    def __init__(self, base: str):
        self.pizza = Pizza(base)

    def add_cheese(self):
        self.pizza.add_topping("Cheese", 1.0)
        return self

    def add_tomato(self):
        self.pizza.add_topping("Tomato", 0.5)
        return self

    def add_jalapeno(self):
        self.pizza.add_topping("Jalapeno", 0.75)
        return self

    def add_mushroom(self):
        self.pizza.add_topping("Mushroom", 0.85)
        return self

    def build(self) -> Pizza:
        return self.pizza

# Example Usage
if __name__ == "__main__":
    builder = PizzaBuilder("Farmhouse")
    my_pizza = builder.add_cheese().add_jalapeno().add_mushroom().build()

    print("Order:", my_pizza.get_description())
    print("Total Cost: $", my_pizza.get_cost())