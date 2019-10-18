from sys import argv
from math import ceil


def encrypt_message(message, key):
    matrix = []
    num_of_rows = ceil(len(message) / int(key))
    num_of_boxes = num_of_rows * int(key)
    for box_number in range(num_of_boxes):
        try:
            matrix.append(message[box_number])
        except IndexError:
            matrix.append(None)
        encrypted_string = ''
    for i in range(int(key)):
        for j in range(num_of_rows):
            letter = matrix[i + j * int(key)]
            if letter:
                encrypted_string += letter
    return encrypted_string


def main():
    message, key = argv[1:]

    encrypted_message = encrypt_message(message, key)

    print(encrypted_message)


if __name__ == '__main__':
    main()
