__version__ = '0.0.1'

my_secret = 'you_will_never_guess'
my_list = [1, 2, 3, 4]
my_tuple = ('a', 'b', 'c')

def double_me(x):
    return 2*x

class Multiplier:
    def __init__(self, i):
        self.i = i
    def get_result(self, x):
        return self.i*x

mult2 = Multiplier(2)
mult3 = Multiplier(3)

print('my_module imported')

if __name__ == '__main__':
    # this code is not executed when importing this module, but only if the module is executed
    print('executing main block')
