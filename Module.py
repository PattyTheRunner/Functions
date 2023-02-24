def greet(f_name):
    """This function greets."""
    print(f'Hello {f_name}.')

def toppings(*pizza):
    """Takes in toppings that the user requires."""
    for i in pizza:
        print(f"Adding {i}.")

def food(*foods2):
    """Takes in food that the user requires."""
    for x in foods2:
        print(f"Serving {x}.")
