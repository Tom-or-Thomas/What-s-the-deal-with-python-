# Import entire package under random namespace
import random as entropy # can reference import as anything (similar to js)

# Import specific variable or function from package
from math import ceil # Could also use * to import everything

print (entropy.random())


# Imports are only initialized once. Meaning, that when it's first imported, it's instantiated. If it's imported again, 
# we will just use the previously created version (as they said, acts like a singleton)


# Can use PYTHONPATH to tell python where to look for modules

# List of built in libraries can be found here https://docs.python.org/3/library/