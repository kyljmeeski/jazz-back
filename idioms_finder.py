from words_finder import non_empty_vowel, CONSONANTS, non_empty_consonant
import re

idioms = []


def init_idioms():
    with open('idioms.txt', 'r', encoding='utf-8') as file:
        for idiom in file:
            idioms.append(idiom.lower())


def one_vowel(vowel, first_letter):
    matches = []
    vowel = non_empty_vowel(vowel)
    pattern = rf'[{CONSONANTS}]*{vowel}[{CONSONANTS}]*'
    for idiom in idioms:
        for word in idiom.split():
            if re.fullmatch(pattern, word):
                if first_letter != '':
                    if word[0] == first_letter:
                        matches.append(idiom)
                else:
                    matches.append(idiom)
                continue
    return matches


def two_vowel(first_vowel, second_vowel, consonant, first_letter):
    matches = []
    first_vowel = non_empty_vowel(first_vowel)
    second_vowel = non_empty_vowel(second_vowel)
    consonant = non_empty_consonant(consonant)
    pattern = rf'[{CONSONANTS}]*{first_vowel}{consonant}{second_vowel}[{CONSONANTS}]*'
    for idiom in idioms:
        for word in idiom.split():
            if re.fullmatch(pattern, word):
                if first_letter != '':
                    if word[0] == first_letter:
                        matches.append(idiom)
                else:
                    matches.append(idiom)
                continue
    return matches


def three_vowels(first_vowel, second_vowel, third_vowel, first_consonant, second_consonant, first_letter):
    matches = []
    first_vowel = non_empty_vowel(first_vowel)
    second_vowel = non_empty_vowel(second_vowel)
    third_vowel = non_empty_vowel(third_vowel)
    first_consonant = non_empty_consonant(first_consonant)
    second_consonant = non_empty_consonant(second_consonant)
    pattern = rf'[{CONSONANTS}]*{first_vowel}{first_consonant}{second_vowel}{second_consonant}{third_vowel}[{CONSONANTS}]*'
    for idiom in idioms:
        for word in idiom.split():
            if re.fullmatch(pattern, word):
                if first_letter != '':
                    if word[0] == first_letter:
                        matches.append(idiom)
                else:
                    matches.append(idiom)
                continue
    return matches


def find_idioms(vowels, consonants=(), first_letter=''):
    matches = []
    if len(vowels) == 1:
        matches = one_vowel(vowels[0], first_letter)
    elif len(vowels) == 2:
        if len(consonants) < 1:
            consonants = ['']
        matches = two_vowel(vowels[0], vowels[1], consonants[0], first_letter)
    elif len(vowels) == 3:
        if len(consonants) < 2:
            consonants = ['', '']
        matches = three_vowels(vowels[0], vowels[1], vowels[2], consonants[0], consonants[1], first_letter)
    return [match.capitalize() for match in matches]


def main():
    init_idioms()
    for idiom in find_idioms(['у', 'а', 'а'], ['б', '']):
        print(idiom)


if __name__ == '__main__':
    main()
