# 1.  Create two dictionaries, Jane and John, to store contact information for Jane and John, respectively.
# 2.  Each contact dictionary contains keys for 'name,' 'phone,' and 'email' with corresponding values.
# 3.  Create a contacts dictionary and use the names 'Jane' and 'John' as keys, associating them with their respective contact dictionaries.
# 4.  Print Jane's contact information.
# 5.  Update Jane's phone number.
# 6.  Print Jane's updated contact information.

Jane = {
    'name': 'Jane',
    'phone': '1234567890',
    'email': 'jane@gmail.com'
}

John = {
    'name': 'John Smith',
    'phone': '987-654-3210',
    'email': 'john@gmail.com'
}

contacts = {
    'Jane': Jane,
    'John': John
}

print("Jane's contact information:")
print(contacts['Jane'])

contacts['Jane']['phone'] = '555-555-5555'

print("Updated contact information")
print(contacts['Jane'])
