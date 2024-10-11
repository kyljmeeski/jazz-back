from flask import Flask, request, jsonify
from flask_cors import CORS

from idiom_read import vowels
from idioms_finder import find_idioms, init_idioms
from words_finder import init_words, find_matches

app = Flask(__name__)
CORS(app)


@app.route('/matching-words', methods=['POST'])
def matching_words():
    data = request.get_json()
    vowels = data['vowels']
    consonants = data['consonants']
    headless = data['headless']
    tailless = data['tailless']
    first_letter = data['first-letter']
    words = find_matches(vowels, consonants, headless, tailless, first_letter)
    idioms = find_idioms(vowels, consonants, first_letter)
    return {
        'words': words,
        'idioms': idioms
    }


if __name__ == '__main__':
    init_words()
    init_idioms()
    app.run(debug=True)
