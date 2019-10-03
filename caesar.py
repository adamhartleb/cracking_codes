from string import ascii_letters


def encode(word, key, mode):
    key = key % 26
    letters = list(word)
    encrypted_letters = []
    for letter in letters:
        encrypted_letter = ''
        if letter == ' ':
            encrypted_letter = ' '
        elif not(letter in ascii_letters):
            raise ValueError("Word must consist of only letters.")
        else:
            encrypted_letter = shift_letter(letter, key, mode)
        encrypted_letters.append(encrypted_letter)

    return ''.join(encrypted_letters)


def shift_letter(letter, key, mode):
    isUppercase = letter.isupper()
    letter = letter.lower()
    encrypted_letter = ''
    if mode == "encrypting":
        if ord(letter) + key > ord('z'):
            encrypted_letter = chr(ord(letter) - 26 + key)
        else:
            encrypted_letter = chr(ord(letter) + key)
    else:
        if ord(letter) - key < ord('a'):
            encrypted_letter = chr(ord(letter) + 26 - key)
        else:
            encrypted_letter = chr(ord(letter) - key)

    return encrypted_letter.upper() if isUppercase else encrypted_letter


def main():
    plain_text = input("Please enter a word: ")
    key = input("Enter a shift: ")
    mode = input("Are we encrypting or decrypting?: ")
    if mode != "encrypting" and mode != "decrypting":
        raise ValueError("Unknown mode.")
    encrypted_text = encode(plain_text, int(key), mode)
    print(encrypted_text)


main()
