from abc import ABC, abstractmethod
from typing import List


class Word(ABC):
    @abstractmethod
    def type(self) -> str:
        pass

    @abstractmethod
    def vowels(self) -> List[str]:
        pass

    @abstractmethod
    def consonants(self) -> List[str]:
        pass

    @abstractmethod
    def form(self) -> str:
        pass

    @abstractmethod
    def normalized(self) -> str:
        pass

class Words(ABC):
    @abstractmethod
    def all(self) -> List[Word]:
        pass


class BaseWord(Word):
    def __init__(self, src: str):
        self.__source = src
        self.__vowels = [
            "а", "ы", "о", "у",
            "э", "и", "ө", "ү",
            "е", "ё", "ю", "я"
        ]
        self.__consonants = [
            "п", "т", "с", "ш", "к", "ф", "ч", "х", "щ", "ц",
            "б", "д", "з", "ж", "г", "в",
            "м", "н", "ң", "л", "р", "й"
        ]

    def type(self) -> str:
        return self.__source.split(",")[1].strip()

    def vowels(self) -> List[str]:
        for letter in self.normalized():
            if letter in self.__vowels:
                yield letter

    def consonants(self) -> List[str]:
        for letter in self.normalized():
            if letter in self.__consonants:
                yield letter
            elif letter in self.__vowels:
                yield "+"
            elif letter == "ь" or letter == "ъ" or letter == " ":
                continue
            else:
                yield "?"

    def form(self) -> str:
        form = ""
        for letter in self.normalized():
            if letter in self.__consonants:
                form += "c"
            elif letter in self.__vowels:
                form += "v"
            else:
                continue
        return form

    def __str__(self) -> str:
        return self.__source.split(",")[0].strip()

    def __len__(self) -> int:
        count = 0
        for letter in self.normalized():
            if letter in self.__vowels:
                count += 1
        return count

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__str__() == other.__str__()
        return False

    def normalized(self):
        word = self.__source.split(",")[0].strip()
        word = word.replace("аа", "а").replace("оо", "о")
        word = word.replace("уу", "у").replace("ээ", "э")
        word = word.replace("өө", "ө").replace("үү", "ү")

        result = ""
        mapping = {
            "е": "йэ",
            "ё": "йо",
            "ю": "йу",
            "я": "йа"
        }

        if word[0] in mapping:
            result += mapping[word[0]]
        else:
            result += word[0]

        for i in range(1, len(word)):
            if word[i] in mapping and word[i-1] in self.__vowels + [" "]:
                result += mapping[word[i]]
            else:
                result += word[i]

        return result

class AllWords(Words):
    def __init__(self, path: str):
        self.__path = path

    def all(self) -> List[Word]:
        with open(self.__path, "r", encoding="utf-8") as file:
            for line in file:
                yield BaseWord(line)

class SizedWords(Words):
    def __init__(self, words: Words, size: int):
        self.__words = words
        self.__size = size

    def all(self) -> List[Word]:
        for word in self.__words.all():
            if len(word) == self.__size:
                yield word


def test():
    words = SizedWords(AllWords("words.csv"), 2)
    for word in words.all():
        print(word)

def forms():
    words = AllWords("words.csv")
    one_syllable_words = SizedWords(words, 2)
    grouped = {}
    for word in one_syllable_words.all():
        key = word.form()
        grouped[key] = word
    sorted_items = sorted(grouped.items(), key=lambda x: len(x[1].form()))
    for key, value in sorted_items:
        print(key, value)


class CVCCVC:
    def __init__(self, word: Word):
        self.__word = word

    def left(self) -> str:
        return self.__word.normalized()[:3]

    def right(self) -> str:
        return self.__word.normalized()[3:]



def main():
    words = AllWords("words.csv")
    one_syllable_words = SizedWords(words, 1)
    one_syllable_words_normalized = {}
    for word in one_syllable_words.all():
        key = word.normalized()
        one_syllable_words_normalized[key] = word
    two_syllable_words = SizedWords(words, 2)
    for word in two_syllable_words.all():
        if word.form() == "cvccvc":
            whole = CVCCVC(word)
            left_part = whole.left()
            right_part = whole.right()
            if left_part in one_syllable_words_normalized and right_part in one_syllable_words_normalized:
                print(word, str(one_syllable_words_normalized[left_part]) + "+" + str(one_syllable_words_normalized[right_part]))

if __name__ == "__main__":
    # main()
    # forms()
    test()
