import json


def get_word_pairs():
    words = []
    with open('words.csv', encoding='utf-8') as file:
        for pair in file.readlines():
            word = pair.split(',')[0]
            words.append(word)
    return words


def main():
    new_words = dict()
    words = get_word_pairs()
    for word in words:
        for offset in range(len(word)):
            new_word = word[offset:]
            if new_word in new_words:
                if word != new_word and new_word in words:
                    new_words[new_word].append(word)
            else:
                if word != new_word and new_word in words:
                    new_words[new_word] = [word]

    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(new_words, f, ensure_ascii=False, indent=4)

    for key, value in new_words.items():
        print(key)
        for v in value:
            print("\t" + v)




if __name__ == '__main__':
    main()
