# Similar to other languages, sets help you reduce duplications.. And other things


lee_high_students = set(['John', 'Paul', 'Jordan', 'Ryan', 'John'])

henry_high_students = set(['James', 'Paul', 'Ron', 'Tallen', "Paul", 'Ron'])




# Includes 4 items instead of 5 (removed duplicates)
print(lee_high_students)

# Includes 4 items instead of 6 (removed duplicates)
print(henry_high_students)


# Can get overlapping values between sets
print(lee_high_students.intersection(henry_high_students))

# Can find difference values between sets
print(lee_high_students.difference(henry_high_students))

# Can join results of both sets into one 
print(lee_high_students.union(henry_high_students))
