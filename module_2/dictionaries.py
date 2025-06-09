contact_info = {
    "Alice":"5555-1234",
    "Bob":"1234-4444"
}
print(contact_info)

Alice_phone = contact_info["Alice"]
print(Alice_phone)

#Update Alice's phone number
contact_info["Alice"] = "1234-5678"
print(contact_info)

#add new key to dictionary
contact_info["Eve"] = "8765-4321"
print(contact_info)

#delete key
del contact_info["Bob"]
print(contact_info)

#.keys()
keys = contact_info.keys()
print(keys)

#get values
values = contact_info.values()
print(values)

#get items
items = contact_info.items()
print(items)














