
class Pizza():

	def __init__(self, base: str):
		self.base = base
		self.toppings = []

	def add_toppings(self, topping: str, cost: float) -> None:
		self.toppings.append((topping,cost))

	def get_description(self) -> str:
		desc = self.base + " with " + ", ".join([topping[0] for topping in self.toppings])
		return desc

	def get_price(self) -> float:
		base_price = {"Margherita": 6.0, "ChickenDelight": 9.0, "FarmHouse" : 7.5}
		price = base_price.get(self.base, 6.0)
		for topping, cost in self.toppings:
			price += cost
		return price

class PizzaBuilder():

	def __init__(self, base: str):
		self.pizza = Pizza(base)

	def add_cheese(self):
		self.pizza.add_toppings("Cheese", 1.5)
		return self

	def add_Mushrooms(self):
		self.pizza.add_toppings("Mushrooms", 2.5)
		return self

	def add_Tomatoes(self):
		self.pizza.add_toppings("Tomatoes", 0.5)
		return self

	def build(self):
		return self.pizza


if __name__ == "__main__":
	my_pizza = PizzaBuilder("Margherita")
	my_pizza = my_pizza.add_cheese().add_Mushrooms().build()

	print(f'ORDER: '+ my_pizza.get_description())
	print(f'TOTAL BILL AMOUNT: $ {str(my_pizza.get_price())}')

