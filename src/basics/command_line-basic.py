# CLI lessons are from https://www.geeksforgeeks.org/command-line-interface-programming-python/


import argparse 

# Create parser object
parser = argparse.ArgumentParser(description = "An addition program")

# Setup argument name
parser.add_argument('add', nargs = '*', metavar = 'num', type = int, help = "All the numbers separated by space will be added.")

# Check arguments passed to the command
args = parser.parse_args()

# 
if len(args.Add) != 0: 
    print(sum(args.Add))