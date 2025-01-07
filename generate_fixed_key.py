from cryptography.fernet import Fernet

def generate_fixed_key():
    key = Fernet.generate_key()
    with open('fixed_key.key', 'wb') as key_file:
        key_file.write(key)
    print("Fixed key generated and saved to 'fixed_key.key'")

if __name__ == '__main__':
    generate_fixed_key()
