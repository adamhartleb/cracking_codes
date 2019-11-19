from math import ceil
from sys import argv


def transposition_decrypt(encrypted_message, key):
    num_matrix_columns = ceil(len(encrypted_message) / key)
    num_matrix_rows = key
    num_matrix_elements = num_matrix_columns * num_matrix_rows
    num_null_boxes = num_matrix_columns * key - len(encrypted_message)
    null_row_start = num_matrix_rows - num_null_boxes
    matrix = [[] for _ in range(key)]

    matrix_index = 0
    letter_index = 0
    while matrix_index < num_matrix_elements:
        row_number = matrix_index // num_matrix_columns

        is_start_of_null_row = row_number >= null_row_start
        is_last_element_in_row = (matrix_index + 1) % num_matrix_columns == 0

        if is_start_of_null_row and is_last_element_in_row:
            matrix[row_number].append(None)
        else:
            letter = encrypted_message[letter_index]
            matrix[row_number].append(letter)
            letter_index += 1
        matrix_index += 1

    decrypted_message = ''
    for column_number in range(num_matrix_columns):
        for row_number in range(num_matrix_rows):
            letter = matrix[row_number][column_number]
            if letter:
                decrypted_message += letter
    return decrypted_message


def main():
    message, key = argv[1:]

    decrypted_message = transposition_decrypt(message, int(key))

    print(decrypted_message)


if __name__ == "__main__":
    main()
