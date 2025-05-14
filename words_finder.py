import csv
import re

VOWELS = 'аеёиоөуүыэ'
LONG_VOWELS = 'аа|оо|өө|ээ|уу|үү'
CONSONANTS = 'бвгджзйклмнңпсртфхцчшщ'
SYLLABLE = rf'([{CONSONANTS}]*({LONG_VOWELS}|[{VOWELS}])[{CONSONANTS}]*)?'


words = []


def init_words():
    with open('words.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            words.append(row)


def non_empty_vowel(vowel):
    if vowel == '':
        return rf'({LONG_VOWELS}|[{VOWELS}])'
    else:
        vowel.replace('е', 'э').replace('ё', 'йо').replace('ю', 'йу').replace('я', 'йа')
    return vowel


def non_empty_consonant(consonant):
    if consonant == '':
        return rf'[{CONSONANTS}]+'
    return consonant


def one_vowel(vowel, headless=True, tailless=True):
    matches = []
    vowel = non_empty_vowel(vowel)
    if headless:
        head = rf''
    else:
        head = rf'{SYLLABLE}'
    if tailless:
        tail = rf''
    else:
        tail = rf'{SYLLABLE}'
    pattern = rf'{head}[{CONSONANTS}]*{vowel}[{CONSONANTS}]*{tail}'
    for word, category in words:
        if re.fullmatch(pattern, word):
            matches.append([word, category])
    return matches


def two_vowels(first_vowel, second_vowel, consonant='', headless=True, tailless=True):
    matches = []
    first_vowel = non_empty_vowel(first_vowel)
    second_vowel = non_empty_vowel(second_vowel)
    consonant = non_empty_consonant(consonant)
    if headless:
        head = rf''
    else:
        head = rf'{SYLLABLE}'
    if tailless:
        tail = rf''
    else:
        tail = rf'{SYLLABLE}'
    pattern = rf'{head}[{CONSONANTS}]*{first_vowel}{consonant}{second_vowel}[{CONSONANTS}]*{tail}'
    # print(pattern)
    for word, category in words:
        full_match = re.fullmatch(pattern, word)
        if full_match:
            matches.append([word, category])
    return matches


def three_vowels(first_vowel, second_vowel, third_vowel, first_consonant='', second_consonant='', headless=True, tailless=True):
    matches = []
    first_vowel = non_empty_vowel(first_vowel)
    second_vowel = non_empty_vowel(second_vowel)
    third_vowel = non_empty_vowel(third_vowel)
    first_consonant = non_empty_consonant(first_consonant)
    second_consonant = non_empty_consonant(second_consonant)
    if headless:
        head = rf''
    else:
        head = rf'{SYLLABLE}'
    if tailless:
        tail = rf''
    else:
        tail = rf'{SYLLABLE}'
    pattern = rf'{head}[{CONSONANTS}]*{first_vowel}{first_consonant}{second_vowel}{second_consonant}{third_vowel}[{CONSONANTS}]*{tail}'
    for word, category in words:
        if re.fullmatch(pattern, word):
            matches.append([word, category])
    return matches


def find_matches(vowels, consonants=(), headless=True, tailless=True, first_letter=''):
    matches = []
    if len(vowels) == 1:
        vowel = vowels[0]
        matches = one_vowel(vowel, headless, tailless)
    elif len(vowels) == 2:
        if len(consonants) < 1:
            consonants = ['']
        first_vowel = vowels[0]
        second_vowel = vowels[1]
        consonant = consonants[0]
        matches = two_vowels(first_vowel, second_vowel, consonant, headless, tailless)
    elif len(vowels) == 3:
        if len(consonants) < 2:
            consonants = ['', '']
        first_vowel = vowels[0]
        second_vowel = vowels[1]
        third_vowel = vowels[2]
        first_consonant = consonants[0]
        second_consonant = consonants[1]
        matches = three_vowels(first_vowel, second_vowel, third_vowel, first_consonant, second_consonant, headless, tailless)
    if first_letter != '':
        matches = [match for match in matches if match[0][0] == first_letter]
    return categorize_words(matches)


def categorize_words(words_to_categorize):
    result = {}
    for word, category in words_to_categorize:
        first_letter = word[0]
        if category not in result:
            result[category] = []
        found = False
        for sublist in result[category]:
            if sublist and sublist[0][0] == first_letter:
                sublist.append(word)
                found = True
                break
        if not found:
            result[category].append([word])
    return result



def main():
    init_words()
    # print(find_matches(['у'], first_letter='т'))
    matches = find_matches(['е', 'е'], ['р'], first_letter='к')
    print(matches)
    # matches = three_vowels('у', 'а', 'а', '')
    # print(matches)
    # print(find_matches(['у', 'а', 'а'], ['б', 'с'], first_letter='т'))

    # print(re.fullmatch(r'[бвгджзйклмнңпсртфхцчшщ]*е[бвгджзйклмнңпсртфхцчшщ]+е[бвгджзйклмнңпсртфхцчшщ]*', 'керек'))


def test():
    init_words()
    for pair in words:
        word = pair[0]
        if any(sub in word.lower() for sub in ["иа"]):
            print(word)

if __name__ == '__main__':
    test()
    # main()
