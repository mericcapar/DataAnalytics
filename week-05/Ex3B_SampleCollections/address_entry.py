contact_info = {
    "name": "Jane Smith",
    "address": "123 Main Street",
    "city": "Mountain View",
    "state": "CA",
    "zip": "94043",
}

print(f"""{contact_info['name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")

# Remove the name key
del contact_info["name"]

# A new dictionary for the full name
full_name = {"first name": "Jane", "last name": "Smith"}
full_name.update({"honorific": "Ms."})

# Add full_name to contact_info
contact_info.update({"full_name": full_name})

name = contact_info["full_name"]
print(f"""
{name['honorific']} {name['first name']} {name['last name']}
{contact_info['address']}
{contact_info['city']}, {contact_info['state']} {contact_info['zip']}""")