# Use double equals for checks 
isTrue = 1 == 1

print(isTrue)

name = 'Tom'

if name == 'Tom':
    print('Name is Tom')

# use 'or' instead of || and 'and' instead of &&
if name == 'Joe' or name == 'Tom':
    print('Name is either Joe or Tom')


# Using 'in' operator to see if string is one of the array values
if name in ['Jacob', 'Joey', 'Tim', 'Joe']: 
    print('Name is either Jacob, Joey, Tim, or Joe')


# 'is' operator matches instances of object
x = [1,2,3]
y = [1,2,3]

print("Checking results of '=='")
print(x == y)
print("Checking results of 'is'")
print(x is y)
