# Create a Pizza type for representing pizzas in Python. Think about some basic properties that would define a pizza's values; things like size, crust type, and toppings would help. Define those in the __init__ method so each instance can have its own specific values for those properties.

class Pizza:
    def __init__(self, size, crust, toppings):
        self.size = size
        self.crust = crust
        self.toppings = toppings

# Add a method for interacting with a pizza's toppings, called add_topping.
    def add_topping(self, new_topping):
        self.toppings.append(new_topping) 

# Add a method for outputting a description of the pizza (sample output below).
    def describe_pizza(self):
        toppers = " ".join(self.toppings)
        print(f"I would like a {self.size} {self.crust} pizza with {toppers}")

# Make two different instances of a pizza. If you have properly defined the class, you should be able to do something like the following code with your Pizza type.

pizza_one = Pizza("small", "deep dish", ["fish n' chips", "mac n' cheese"])
pizza_one.cook_method = "bake"
print(pizza_one.cook_method, pizza_one.size, pizza_one.crust, pizza_one.toppings)
pizza_one.describe_pizza()
# meat_lovers = Pizza()
# meat_lovers.size = 16
# meat_lovers.style = "Deep dish"
# meat_lovers.add_topping("Pepperoni")
# meat_lovers.add_topping("Olives")
# meat_lovers.print_order()
# You should produce output in the terminal similiar to the following string.

# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."