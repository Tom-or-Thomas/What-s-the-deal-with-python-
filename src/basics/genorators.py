import random


def random_number_generator(): 
    for i in range(6): 
        yield random.randint(1, 40)

    yield random.randint(1,15)

for random_number in random_number_generator(): 
    print('And the next number is %d' % random_number)

