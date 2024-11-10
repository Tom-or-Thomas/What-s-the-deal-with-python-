# Seems like I could have also used urllib (which is built on top of this library)
import http.client

host = 'meowfacts.herokuapp.com'

connection = http.client.HTTPSConnection(host)

connection.request('GET', "/")


response = connection.getresponse()

raw_data = response.read()

print('raw data is ', raw_data)

data = response.read().decode()

print('data is ', data)

print(response.getcode())

print(response.status)
