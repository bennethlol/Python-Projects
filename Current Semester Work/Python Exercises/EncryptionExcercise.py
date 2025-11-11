from cryptography.fernet import Fernet
# Generate a random key
key = Fernet.generate_key()
# Initialize the Fernet cipher with the key
cipher_suite = Fernet(key)
# Encrypt a message
plaintext = b"Hello, World!"
cipher_text = cipher_suite.encrypt(plaintext)
# Decrypt the message
decrypted_text = cipher_suite.decrypt(cipher_text)
print("Plaintext:", plaintext.decode())
print("Decrypted:", decrypted_text.decode())
