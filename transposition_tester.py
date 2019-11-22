import random
import sys
import transposition_cipher
import transposition_decrypt
import string


def main():
    random.seed(42)
    for i in range(20):
        message = list(string.ascii_uppercase * random.randint(4, 40))
        random.shuffle(message)
        message = ''.join(message)
        for key in range(1, int(len(message) / 2)):
            encrypted = transposition_cipher.encrypt_message(message, key)
            decrypted = transposition_decrypt.transposition_decrypt(
                encrypted, key)
            if message != decrypted:
                print(f'Mismatch with key {key} and message {message}')
                print(f'Decrypted as {decrypted}')
                sys.exit()
    print('Transposition Cipher tests passed.')


if __name__ == '__main__':
    main()
