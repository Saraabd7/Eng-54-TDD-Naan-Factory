# import naan factory functions
# define and run tests

from naan_factory_functions import *

#1
# As a user, I can use the make_dough with water and flour to make dough.
print("calling make_dough with water and flour, expect 'dough' as a result")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

print("calling make_dough with water and cement, expect 'not dough' as a result")
print(make_dough('water', 'cement') == 'not dough')
print('got:', make_dough('water', 'cement'))