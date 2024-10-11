import requests
from bs4 import BeautifulSoup
import csv


domain = 'https://el-sozduk.kg/'
letters = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
    'ң', 'о', 'ө', 'п', 'р', 'с', 'т', 'у', 'ү', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
    'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]


def request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        print('Request to ' + url + ' failed')


def parse(html):
    words = []
    soup = BeautifulSoup(html, 'html.parser')
    article_divs = soup.find_all('article')
    for article_div in article_divs:
        dictionary = article_div.find('span', attrs={'itemprop': 'inDefinedTermSet'}).text.strip()
        if dictionary == 'Толковый словарь кыргызского языка (1969)':
            word = article_div.find('h1').text.strip()
            description_div = article_div.find('div', attrs={'itemprop': 'description'})
            description = description_div.text.strip()
            word_type = description.split('.')[0]
            if len(word_type) > 4:
                if 'этишинин' in description:
                    word_type = 'этиш формасы'
                else:
                    word_type = 'неизвестно'
            words.append({'слово': word, 'часть речи': word_type})
    return words


def save(filename, new_words):
    if len(new_words) < 1:
        return
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=new_words[0].keys())
        writer.writerows(new_words)
        print(str(len(new_words)) + ' word appended')


def main():
    for first in letters:
        for second in letters:
            comb = first + second
            print('requesting ' + comb)
            request_url = domain + comb
            html_response = request(request_url)
            new_words = parse(html_response)
            save('words.csv', new_words)


if __name__ == '__main__':
    # main()
    pass
