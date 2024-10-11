import re

idioms = []


vowels = 'аеёиоөуүы'
long_vowels = 'аа|оо|өө|ээ|уу|үү'
consonants = 'бвгджзйклмнңпсртфхцчшщ'


def init_idioms():
    with open('idioms.txt', 'r', encoding='utf-8') as file:
        for idiom in file:
            idioms.append(idiom.strip())


def matching_idioms(first_letter):
    return [idiom for idiom in idioms if any(word.startswith(first_letter) for word in idiom.strip().lower().split())]


def one_vowel(vowel):
    pattern = rf'[{consonants}]+{vowel}[{consonants}]+'
    return [idiom for idiom in idioms if any(word.startswith(vowel) for word in idiom.strip().lower().split())]


def two_vowels(first_vowel, second_vowel):
    pattern = rf'[{consonants}]+{first_vowel}[{consonants}]+{second_vowel}[{consonants}]+'
    matches = []
    for idiom in idioms:
        words = idiom.strip().lower().split()
        for word in words:
            if re.fullmatch(pattern, word):
                matches.append(idiom)
    return matches


def three_vowels(first_vowel, second_vowel, third_vowel, first_letter=None):
    pattern = rf'[{consonants}]+{first_vowel}[{consonants}]+{second_vowel}[{consonants}]+{third_vowel}[{consonants}]+'
    matches = []
    for idiom in idioms:
        words = idiom.strip().lower().split()
        for word in words:
            if first_letter is None:
                if re.fullmatch(pattern, word):
                    matches.append(idiom)
                    continue
            else:
                if re.fullmatch(pattern, word):
                    if word.startswith(first_letter):
                        matches.append(idiom)
                        continue
    return matches


def main():
    init_idioms()
    # for idiom in two_vowels('ү', 'ү'):
    #     print(idiom)
    for idiom in three_vowels('ү', 'ү', 'ү'):
        print(idiom)


if __name__ == '__main__':
    main()
