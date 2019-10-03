from string import ascii_letters


def encode(word, key):
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
            encrypted_letter = shift_letter(letter, key)
        encrypted_letters.append(encrypted_letter)

    return ''.join(encrypted_letters)


def shift_letter(letter, key):
    isUppercase = letter.isupper()
    letter = letter.lower()
    encrypted_letter = ''
    if ord(letter) + key > ord('z'):
        encrypted_letter = chr(ord(letter) - 26 + key)
    else:
        encrypted_letter = chr(ord(letter) + key)
    return encrypted_letter.upper() if isUppercase else encrypted_letter


def main():
    print("Please enter a word:", end=" ")
    plain_text = input()
    print("Enter a shift:", end=" ")
    key = input()
    encrypted_text = encode(plain_text, int(key))
    print(encrypted_text)


main()
