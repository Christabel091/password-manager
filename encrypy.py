def generate_vigenere_key(text, keyword):
    key = list(keyword)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(text, keyword):
    key = generate_vigenere_key(text, keyword)
    encrypted_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            shift_amount = ord(key[i].lower()) - ord('a')
            char_code = ord(text[i]) + shift_amount
            if text[i].isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                encrypted_text.append(chr(char_code))
            elif text[i].islower():
                if char_code > ord('z'):
                    char_code -= 26
                encrypted_text.append(chr(char_code))
        else:
            encrypted_text.append(text[i])
    return "".join(encrypted_text)


def decrypt_vigenere(text, keyword):
    key = generate_vigenere_key(text, keyword)
    decrypted_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            shift_amount = ord(key[i].lower()) - ord('a')
            char_code = ord(text[i]) - shift_amount
            if text[i].isupper():
                if char_code < ord('A'):
                    char_code += 26
                decrypted_text.append(chr(char_code))
            elif text[i].islower():
                if char_code < ord('a'):
                    char_code += 26
                decrypted_text.append(chr(char_code))
        else:
            decrypted_text.append(text[i])
    return "".join(decrypted_text)
