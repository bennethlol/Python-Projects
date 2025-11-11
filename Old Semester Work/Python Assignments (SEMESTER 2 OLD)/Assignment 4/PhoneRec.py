import json

# Phonebook dictionary
phonebook = {  
    'John': ('209 Trafalgar Road', '905-666-7777'),  
    'Rosie': ('1439 Trafalgar Road', '487-423-7721')  
}

# Convert into json file
with open("SpeedDial2.json", "w") as file:
    json.dump(phonebook, file)

# Open file "SpeedDial2.json"
with open("SpeedDial2.json", "r") as file:
    load = json.load(file)
    # Print details
    for name, (add,phone) in load.items():
        print(f"{name}'s Address: {add}, Phone Number: {phone}")