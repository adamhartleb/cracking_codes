import transposition_cipher
import transposition_decrypt
from time import perf_counter


def timer(fn):
    def inner(*args):
        start = perf_counter()
        fn(*args)
        elapsed = perf_counter() - start
        print(f'{fn.__name__} took {elapsed:.2f} seconds to execute.')
    return inner


def encrypt_text(text, key):
    return transposition_cipher.encrypt_message(text, key)


def decrypt_text(encrypted_text, key):
    return transposition_decrypt.transposition_decrypt(encrypted_text, key)


def fetch_file_content(file_name):
    file = open(file_name, 'r')
    return file.read()


def write_to_disk(file_name, content):
    file = open(file_name, 'w+')
    file.write(content)


@timer
def encrypt_file(source_file_name, dest_file_name):
    content = fetch_file_content(source_file_name)
    encrypted_content = encrypt_text(content, 8)
    write_to_disk(dest_file_name, encrypted_content)


@timer
def decrypt_file(source_file_name, dest_file_name):
    content = fetch_file_content(source_file_name)
    decrypted_content = decrypt_text(content, 8)
    write_to_disk(dest_file_name, decrypted_content)


def main():
    encrypt_file('frankenstein.txt', 'encrypted_frankenstein.txt')
    decrypt_file('encrypted_frankenstein.txt', 'decrypted_frankenstein.txt')


if __name__ == "__main__":
    main()
