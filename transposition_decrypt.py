from math import ceil


def transposition_decrypt(encrypted_message, key):
    num_columns = ceil(len(encrypted_message) / key)
    null_boxes = num_columns * key - len(encrypted_message)
    null_row_start = key - null_boxes
    matrix = [[] for _ in range(key)]
    index = 0
    letterIndex = 0

    while index < num_columns * key:
        print(encrypted_message[letterIndex])
        letter = encrypted_message[letterIndex]

        row_number = index // num_columns
        if row_number >= null_row_start and ((index + 1) % num_columns) == 0:
            matrix[row_number].append(None)
        else:
            matrix[index // num_columns].append(letter)
            letterIndex += 1
        index += 1
    print(matrix)
    unecrypted_string = ''
    for column_number in range(num_columns):
        for row in matrix:
            letter = row[column_number]
            if letter:
                unecrypted_string += letter
    print(unecrypted_string)


def main():
    transposition_decrypt('Cenoonommstmme oo snnio. s s c', 8)


if __name__ == "__main__":
    main()
