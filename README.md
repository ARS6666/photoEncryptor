# Image Message Embedder

This project allows you to embed a secret message in an image without affecting the image preview. The message is encrypted and hidden within the image. You can then decrypt the image to retrieve the hidden message and save it to a text file.

## Features

- Embed a secret message in an image
- Encrypt the message and hide it within the image
- Decrypt the image to extract the hidden message
- Save the extracted message to a text file
- Use a fixed key for encrypting and decrypting the message key

## Requirements

- Python 3.x
- `cryptography` library

## Installation

First, ensure you have Python 3.x installed. Then, install the `cryptography` library:

```bash
pip install cryptography
Usage
Step 1: Generate the Fixed Key
Run the generate_fixed_key.py script to generate and save the fixed key:

bash
python generate_fixed_key.py
This will create a file named fixed_key.key that contains the fixed key.

Step 2: Embed a Message in an Image
Run the main program and choose the option to embed a message:

bash
python main.py
When prompted, provide the following inputs:

The absolute path to the image you want to use.

The message you want to embed.

The path to save the new image with the embedded message.

The path to the fixed key file (fixed_key.key).

The program will embed the message in the image and save it to the specified output path.

Step 3: Extract the Message from the Image
Run the main program again and choose the option to extract the message:

bash
python main.py
When prompted, provide the following inputs:

The absolute path to the image with the hidden message.

The path to the fixed key file (fixed_key.key).

The program will extract the hidden message and save it to extracted_message.txt.

Example
Generate the fixed key:

bash
python generate_fixed_key.py
Embed the message:

bash
python main.py
Enter the following when prompted:

Absolute path to your image: /path/to/image.jpg

Enter the message: Secret message

Path to save the new image: /path/to/output_image.jpg

Enter the path to the fixed key file: fixed_key.key

Extract the message:

bash
python main.py
Enter the following when prompted:

Enter the absolute path to the image with hidden message: /path/to/output_image.jpg

Enter the path to the fixed key file: fixed_key.key

The hidden message will be extracted and saved to extracted_message.txt.
```
