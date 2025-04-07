# Phonebook dictionary
phonebook = {  
    'John': ('209 Trafalgar Road', '905-666-7777'),  
    'Rosie': ('1439 Trafalgar Road', '487-423-7721')  
}

# Open file "SpeedDial1.txt"
with open("SpeedDial1.txt", "w") as file:
    # Write each phone number on a new line
    for name, (add,phone) in phonebook.items():
        file.write(phone + "\n")