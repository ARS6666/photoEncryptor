from cryptography.fernet import Fernet

FIXED_KEY = b'_23n4LQbJ4F4-86IMn4N3bJghK4-nOgb4kgB0fGnhF8='  # A fixed key for encrypting the message key

def generate_key():
    return Fernet.generate_key()

def save_key(key, filename):
    with open(filename, 'wb') as key_file:
        key_file.write(key)

def load_key(filename):
    with open(filename, 'rb') as key_file:
        return key_file.read()

def encrypt_message(key, message):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(key, encrypted_message):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message

def encrypt_key_with_fixed_key(key):
    f = Fernet(FIXED_KEY)
    encrypted_key = f.encrypt(key)
    return encrypted_key

def decrypt_key_with_fixed_key(encrypted_key):
    f = Fernet(FIXED_KEY)
    decrypted_key = f.decrypt(encrypted_key)
    return decrypted_key

def embed_message_in_image(image_path, message, output_image_path):
    message_key = generate_key()

    encrypted_message = encrypt_message(message_key, message)
    encrypted_message_key = encrypt_key_with_fixed_key(message_key)

    with open(image_path, 'rb') as img_file:
        image_data = img_file.read()

    with open(output_image_path, 'wb') as out_img_file:
        out_img_file.write(image_data)
        out_img_file.write(b'\xff\xd9')  # JPEG end of file marker
        out_img_file.write(encrypted_message_key)
        out_img_file.write(encrypted_message)

def extract_message_from_image(image_path, output_message_path):
    with open(image_path, 'rb') as img_file:
        image_data = img_file.read()

    # Find the marker indicating the start of the message key
    marker_index = image_data.rfind(b'\xff\xd9')
    if marker_index == -1:
        print("No message found in the image.")
        return

    encrypted_message_key = image_data[marker_index+2:marker_index+2+44]  # Encrypted message key length
    encrypted_message = image_data[marker_index+2+44:]  # Rest is the encrypted message

    message_key = decrypt_key_with_fixed_key(encrypted_message_key)
    decrypted_message = decrypt_message(message_key, encrypted_message)

    with open(output_message_path, 'a') as msg_file:
        msg_file.write(decrypted_message + '\n')

# Example usage:
if __name__ == '__main__':
    option = int(input("1. Embed Message\n2. Extract Message\n"))

    if option == 1:
        image_path = input("Path to your image: ")
        message = input("Enter the message: ")
        output_image_path = input("Path to save the new image: ")

        embed_message_in_image(image_path, message, output_image_path)
        print("Message embedded successfully!")

    elif option == 2:
        image_path = input("Path to the image with hidden message: ")
        output_message_path = 'extracted_message.txt'

        extract_message_from_image(image_path, output_message_path)
        print("Message extracted successfully!")

    else:
        print("Invalid option! Please choose 1 or 2.")
