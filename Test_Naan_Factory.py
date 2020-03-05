# import naan factory functions
# define and run tests
#
# from Naan_factory_functions import *
#
# #1
# # As a user, I can use the make_dough with water and flour to make dough.
# print("calling make_dough with water and flour, expect 'dough' as a result")
# print(make_dough('water', 'flour') == 'dough')
# print('got:', make_dough('water', 'flour'))
#
# print("calling make_dough with water and cement, expect 'not dough' as a result")
# print(make_dough('water', 'cement') == 'not dough')
# print('got:', make_dough('water', 'cement'))

# Exercise:
# 1
# As a user, I can use the make_dough with water and flour to make dough.

# 2
# As a user, I can use the bake_dough with dough to get naan.

# 3
# As a user, I can user the run_factory with water and flour and get naan

from Naan_factory_functions import *

print(make_dough('water', 'flour') == 'dough')

print(bake_dough('dough') == 'naan')

print(run_factory('water', 'flour') == 'naan')