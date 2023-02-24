"""
import Module
Module.greet("Dan")
Module.toppings("pepperoni", "olives", "ham")
Module.food("fish 'n' chips", "sandwiches", "spaghetti")

from Module import *
greet("TJ")
toppings("pepperoni", "olives", "ham")
food("fish 'n' chips", "sandwiches", "spaghetti")

from Module import greet, toppings, food
greet("Debbie")
toppings("pepperoni", "olives", "ham")
food("fish 'n' chips", "sandwiches", "spaghetti")

import Module as m
m.greet("Dan")
m.toppings("pepperoni", "olives", "ham")
m.food("fish 'n' chips", "sandwiches", "spaghetti")

from Module import greet as g, toppings as t, food as f
g("Steve")
t("pepperoni", "olives", "ham")
f("fish 'n' chips", "sandwiches", "spaghetti")
"""
