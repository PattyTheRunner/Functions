
def name(f_name, m_name, l_name):
    """This asks you for your first and last name"""
    print(f'Welcome {f_name} {m_name} {l_name} ')

name(f_name="Stephen", m_name="Olu", l_name="Ade")

def animal(type, p_name="Whiskers"):
    """This tells you what pet you own, and their name."""
    return f"This is my pet {type}. Their name is {p_name}."

an = animal("Rabbit")
print(an)

def hobbies(one,four, two="" ,three="baking"):
    """This names some hobbies"""
    return f'I enjoy {one},{two} {three} and {four}.'

hob = hobbies(one="eating", four="reading")
print(hob)

def pet_names(s, c, m, w):
    """This returns a list and dictionary of pet names"""
    pets_list = [s, c, m, w]
    pets_dic = {'first':s, 'second':c, 'third':m, 'final':w}
    return pets_list, pets_dic

pet = pet_names(s='Star', c='Choco', m='Max', w='Whiskers')
print(pet)

pet_v = pet_names("Star", 'Choco', 'Max', 'Whiskers')
print(pet_v)

"""A function that takes in the first and last name of the user, and returns them in Title Case. 

After the function has been defined, while loop.
It will ask the user for their first and last name. """


def full_Name(f, l):
    """This will return their fist and last name in title case."""
    return f'You are {f.title()}, {l.title()}.'

while True:
    print("Enter q to stop the program.")
    first = input("\nWhat is your first name?")
    last = input("What is your last name?")
    print(full_Name(f = first, l = last))
    if first == "q":
        break
    elif last == "q":
        break


def city_Country(city, country):
    """This will return tp you a country and a city in title case."""
    return f'\n\t{city.title()} is in {country.title()}.'

x = 1
while x < 4:
    ci = input("\nWhat is the city?")
    co = input(f"What country is {ci} in?")
    print(city_Country(city = ci, country = co))
    x += 1

def make_Album(name, title):
    album_dic = {'Name of artist': name.title(), 'Name of album': title.title()}
    return album_dic


while True:
    print("\tEnter 1 to end program\n")
    n = input("What is the name of the artist.")
    a = input("What is the name of the album.")
    print(make_Album(name=n, title=a))
    if n == "1":
        break
    elif a == "1":
        break

def greeting(s):
    """This function while take in the list, and print a simple greeting to each user in the list."""
    for name in s:
        greet = f"\nNice to meet you, {name}."
        print(greet)
names = ["steve", "eve", "bob", "hunter", "jim", "daniel"]
print(greeting(names))
items = ["iPhone", "purse", "Ipad"]
i_Tems = []

def transfer (D, m):
    """Will transfer items from one list to another."""
    while D:
        it = D.pop()
        m.append(it)
    return m

print(transfer(D=items, m=i_Tems))

foods = ["chicken", "pizza", "mushroom", "pasta"]
food = []

def trans (f, g):
    while f:
        p = f.pop()
        g.append(p)
    return g

print(trans(f=foods, g=food))

def pizza(**stuff):
    return stuff
print(pizza(toppings="pepperoni", size="large"))
