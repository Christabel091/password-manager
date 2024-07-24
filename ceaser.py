# Author: Christabel Obi-Nwosu
# Date: Monday 27, 2023
# Program to create a Caesar cipher to encode and decode a message.

import math

ALPHABET = list("_-aA1bB2cC3dD4eE5fFg6Gh7@#$%HiI8jJk9KlLmMnNo0OpPqQrRsStTuUvVwWxXyYzZ (!^&*<>?=/)")

def generate_cipher(key):
    return ALPHABET[key:] + ALPHABET[:key]

def encode_message(message, cipher):
    encoded_message = ''
    for char in message:
        if char in ALPHABET:
            encoded_message += cipher[ALPHABET.index(char)]
    return encoded_message

def decode_message(encoded_message, cipher):
    decoded_message = ''
    for char in encoded_message:
        if char in cipher:
            decoded_message += ALPHABET[cipher.index(char)]
    return decoded_message

