import re
import random
from collections import defaultdict

short_vowels = [
    'а', 'о', 'у',
    'э', 'ө', 'ү',
    'и', 'ы'
]
long_vowels = [
    'аа', 'оо', 'уу',
    'ээ', 'өө', 'үү'
]

VOWELS = 'аэоөуүиы'
LONG_VOWELS = 'аа|ээ|оо|өө|уу|үү|ээ'
CONSONANTS = 'бвгджзйклмнңпсртфхцчшщ'
SYLLABLE = rf'([{CONSONANTS}]*({LONG_VOWELS}|[{VOWELS}])[{CONSONANTS}]*)?'


def get_word_pairs():
    pairs = []
    with open('words.csv', encoding='utf-8') as file:
        for pair in file.readlines():
            word = pair.split(',')[0]
            word.replace('я', 'йа')
            word.replace('е', 'йэ')
            word.replace('ё', 'йо')
            word.replace('ю', 'ю')
            pairs.append((word, pair.split(',')[1].strip()))
    return pairs


def get_two_syllable_word_pairs(word_pairs):
    two_syllable_word_pairs = []
    pattern = rf'{SYLLABLE}{SYLLABLE}'
    for pair in word_pairs:
        if re.fullmatch(pattern, pair[0]):
            two_syllable_word_pairs.append(pair)
    return two_syllable_word_pairs


def get_nouns(word_pairs):
    nouns = []
    for pair in word_pairs:
        if pair[1] == 'зат':
            nouns.append(pair)
    return nouns


def get_head_open_words(word_pairs):
    head_open_words = []
    words = []
    for pair in word_pairs:
        words.append(pair[0])
    for word in words:
        if len(word) < 3:
            continue
        for head in range(1, len(word) - 1):
            open_word = word[head:]
            if open_word in words:
                head_open_words.append((open_word, word))
    return head_open_words



def main():
    word_pairs = get_word_pairs()
    # two_syllable_word_pairs = get_two_syllable_word_pairs(word_pairs)
    # nouns = get_nouns(two_syllable_word_pairs)
    # word = random.choice(nouns)
    # print(word)
    words = get_head_open_words(word_pairs)
    # for word in words:
    #     print(word)
    grouped = defaultdict(list)
    for s in words:
        first, second = s
        grouped[first].append(second)
    grouped = dict(grouped)
    for k, v in grouped.items():
        print(k, v)



if __name__ == '__main__':
    main()
