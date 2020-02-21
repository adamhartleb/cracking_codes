from timer import timer


def load_dictionary(filename):
    with open(filename) as file:
        words = file.read().splitlines()
        return {k: None for k in words}


def english_count(sentence: str):
    dictionary = load_dictionary('dictionary.txt')
    split_sentence = [word.upper() for word in sentence.split(' ')]
    matches = 0
    for word in split_sentence:
        if word in dictionary:
            matches += 1
    return matches


@timer
def is_english(sentence: str):
    matches = english_count(sentence)
    percentage = float(matches) / len(sentence.split(' ')) * 100
    print(f'{percentage}% of the words in the sentence are English.')


is_english('This is my sentence sentence')
