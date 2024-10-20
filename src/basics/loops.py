# For loops

foods = ['apple', 'orange', 'banana', 'strawberries', 'pineapple']

for fruit in foods: 
    print('This is the current food %s' % fruit)


# Can specify a 'range' of values to loop through
for number in range(0, 20, 5): 
    print('This is the number I got %d' % number)


count = 0

while count < 5: 
    print('We are still counting up')
    count += 1
    #  Can use 'break' and 'continue' as you would usually
# Cool thing here is we can add an else block to the loop that will run when the condition fails (i.e. when it's finished, but not when it's done by a 'break' statement)
else: 
    print('Condition failed for some reason... . %d' % count)


