# Create a list of pizza orders with additional pizzas
pizza_orders = [
    "Margherita", 
    "Pepperoni", 
    "Hawaiian", 
    "Veggie", 
    "BBQ Chicken", 
    "Supreme", 
    "Meat Lovers", 
    "Four Cheese", 
    "Buffalo Chicken"
]

# empty list to hold finished pizzas
finished_pizzas = []

# Process each pizza order
while pizza_orders:
    # Remove the first pizza from the list
    current_pizza = pizza_orders.pop(0)
    # Print a message indicating the pizza is finished
    print("Your pizza pie is finished!")
    # Add the finished pizza to the finished_pizzas list
    finished_pizzas.append(current_pizza)

# Print a message for each finished pizza
for pizza in finished_pizzas:
    print(f"The pizza {pizza} was made.")
