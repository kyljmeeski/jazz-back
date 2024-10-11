import requests
from bs4 import BeautifulSoup


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
    idioms = []
    soup = BeautifulSoup(html, 'html.parser')
    article_divs = soup.find_all('article')
    for article_div in article_divs:
        dictionary = article_div.find('span', attrs={'itemprop': 'inDefinedTermSet'}).text.strip()
        if dictionary == 'Фразеологический словарь кыргызского языка (2015)':
            idiom = article_div.find('h1').text.strip().capitalize()
            idioms.append(idiom)
    return idioms


def save(filename, idioms):
    if len(idioms) < 1:
        return
    with open(filename, mode='a', newline='', encoding='utf-8') as writer:
        for idiom in idioms:
            writer.write(idiom + '\n')
        print(str(len(idioms)) + ' idiom appended')


def main():
    for first in letters:
        for second in letters:
            comb = first + second
            print('requesting ' + comb)
            request_url = domain + comb
            html_response = request(request_url)
            new_idioms = parse(html_response)
            save('idioms.txt', new_idioms)


if __name__ == '__main__':
    main()
    # pass
