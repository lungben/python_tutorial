"""example file for module imports"""

__version__ = '0.0.1'

my_secret = 'you_will_never_guess'
my_list = [1, 2, 3, 4]
my_tuple = ('a', 'b', 'c')

def double_me(x):
    """doubles input value"""
    return 2*x

def power_me(x, i: int, times_two=False):
    """useless example function"""
    mult = 2 if times_two else 1
    return mult*x**i

class Multiplier:
    """class that creates multiplier objects with a given factor"""
    def __init__(self, i):
        self.i = i
    def get_result(self, x):
        """returns factor specified with initialization multiplied by input value"""
        return self.i*x

mult2 = Multiplier(2)
mult3 = Multiplier(3)

print('my_module imported')

if __name__ == '__main__':
    # this code is not executed when importing this module, but only if the module is executed
    print('executing main block')
