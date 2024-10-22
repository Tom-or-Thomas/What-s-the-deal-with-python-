# Numpy arrays are faster (?), easy to work with, and allows for calculations across entire arrays.
attack = [12, 4, 2, 25, 5]
defense = [1, 2, 4, 5, 6]

import numpy as np

np_attack = np.array(attack)
np_defense = np.array(defense)

print(type(np_attack))


power_scale = np_attack * np_defense

print(power_scale)

# Only return values greater than 8
print(power_scale[power_scale > 8])