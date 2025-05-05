# Create exception
class IPException(Exception):
    def __init__(self, ip):
        super().__init__(f"Invalid IP Address: {ip}")

# Checks if the ip inputted is valid
def is_valid_ip(ip):
    return (part.isdigit() for part in ip.split('.')) and ip.replace('.', '').isdigit()

# Create dictionary
credentials = []

# Loop
while True:
    # Ask user to input username, password, and ip
    try:
        user = input("Enter username: ")
        password = input("Enter password: ")
        ip = input("Enter IP address: ")

        # if ip inputted is not valid, raise the exception made above
        if not is_valid_ip(ip):
            raise IPException(ip)

        # Append to dictionary
        credentials.append([user, password, ip])

        # Break loop if user chooses to
        cont = input("Add another? (Yes/No): ")
        if cont == 'No':
            break

    except IPException as i:
        print(i)
        
# Add valid credentials to "SessionLogger.txt"
with open("SessionLogger.txt", "w") as file:
    for creds in credentials:
        file.write(str(creds) + "\n")
