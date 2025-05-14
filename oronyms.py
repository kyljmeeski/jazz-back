vowels = [
    'а', 'о', 'у',
    'э', 'ө', 'ү',
    'и', 'ы'
]

long_vowels = [
    'аа', 'оо', 'уу',
    'ээ', 'өө', 'үү'
]

consonants = [
    'б', 'в', 'г', 'д', 'з',
    'п', 'ф', 'к', 'т', 'с',
    'ж' ,'ш', 'щ', 'х', 'ч', 'ц',
    'л', 'м', 'н', 'ң', 'р', 'й'
]

def get_word_pairs():
    with open("words.csv", mode="r", encoding="utf-8") as f:
        for line in f.readlines():
            word = line.split(",")[0].strip()
            category = line.split(",")[1].strip()
            yield word, category

def get_nouns(pairs):
    for pair in pairs:
        if pair[1] == "зат":
            yield pair[0]

def get_adjectives(pairs):
    for pair in pairs:
        if pair[1] == "сын":
            yield pair[0]

def get_syllables_count(word):
    long_to_short = dict(zip(long_vowels, [v[0] for v in long_vowels]))
    for long_vowel, short_vowel in long_to_short.items():
        word = word.replace(long_vowel, short_vowel)
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

def get_three_syllable_words(words):
    for word in words:
        if get_syllables_count(word) == 3:
            yield word

def main():
    word_pairs = get_word_pairs()
    adjectives = get_adjectives(word_pairs)
    nouns = get_nouns(word_pairs)

if __name__ == '__main__':
    # syllables_count_of("ээрчи")
    main()
