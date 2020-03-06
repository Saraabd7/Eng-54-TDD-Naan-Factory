# Factory functions
# define our function  here
from Run_Naan_Factory import *

def make_dough(arg1, arg2):
    # if argument is water and argument 2 is flour
        # return dough
    # else return
        # not dough

    if arg1 == 'water' and arg2 == 'flour':
        return 'dough'
    else:
        return 'not dough'


def bake_dough(arg1):
    if arg1 == 'dough':
        return 'naan'
    else:
        return 'not naan'

def run_factory(water, flour):
    return bake_dough(make_dough(water, flour))