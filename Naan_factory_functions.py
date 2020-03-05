# Factory functions
# define our function  here
from Run_Naan_Factory import *

def make_dough(arg1, arg2):
    # if argument is water and argument 2 is flour
        # return doght
    # else return
        # not dough
    return 'dough'

def make_dough(ingredient1,ingredient2):
    if (ingredient1 == 'water') and (ingredient2 == 'flour'):
        return 'dough'
    elif (ingredient1 == 'flour') and (ingredient2 == 'water'):
        return 'dough'
    else:
        return 'Not dough'

def bake_dough(ingredient):
    if ingredient == 'dough':
        return 'naan'
    else:
        return 'not naan'

def run_factory(ing1,ing2):
    return bake_dough(make_dough(ing1, ing2))