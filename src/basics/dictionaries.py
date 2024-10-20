build = {}
build['age'] = 434
build['height'] = 433
build['color'] = 'pink'

print(build)

new_build = {
    'age': 2,
    'height': 20,
    'color': 'Orange'
}

print(new_build)


# Iterate over items in a dictionary by using items to get results
for feature, value in new_build.items():
    print('For this feature (%s), the value is %s' %(feature, value))


new_build['hobby'] = 'nothing'

print(new_build['hobby'])

# Delete field 
del new_build['hobby']
# Alternatively, could have done with .pop('hobby')

print(new_build)