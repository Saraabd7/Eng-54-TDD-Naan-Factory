# import naan factory functions
# define and run tests
#

import Run_Naan_Factory
from Naan_factory_functions import *

# 1
# As a user, I can use the make_dough with water and flour to make dough.
print("calling make_dough with water and flour, expect 'dough' as a result")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

# print("calling make_dough with water and cement, expect 'not dough' as a result")
# print(make_dough('water', 'cement') == 'not dough')
# print('got:', make_dough('water', 'cement'))


# 2
# As a user, i can use the bake_dough with dough to get naan.
print("calling bake_dough with dough, expect 'naan' as a result")
print(((bake_dough('dough')) == 'naan'))
print('got:', bake_dough('dough'))

# 3
# As a user, i can use the run_factory with water and flour and get naan
print("calling make dough with water and flour, calling bake_dough with make_dough and bread_maker. "
      "expecting naan as a result")
print((run_factory('water', 'flour')) == 'naan')
print('got', run_factory('water', 'flour') == 'naan')
