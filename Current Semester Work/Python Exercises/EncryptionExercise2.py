from cryptography.fernet import Fernet
Key = Fernet.generate_key()
cipher_suite = Fernet(Key)
