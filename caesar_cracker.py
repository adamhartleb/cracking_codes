from string import ascii_lowercase


def brute_force(message):
    for key in range(len(ascii_lowercase)):
        iteration = []
        for letter in message:
            # check if letter is a space
            isUppercase = letter.isupper()
            letter = letter.lower()
            index = ascii_lowercase.find(letter)
            if index == -1:
                raise ValueError("Message can only contain letters")
            translation = index - key
            if translation < 0:
                translation += 26
            letter = ascii_lowercase[translation].upper(
            ) if isUppercase else ascii_lowercase[translation]
            iteration.append(letter)
        print(''.join(iteration))


brute_force("ab")
