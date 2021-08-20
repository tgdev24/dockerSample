from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Endpoint to get translation is get_translation'


def isVowel(letter):
    vowels = ["a", "o", "i", "u", "e"]
    if letter.lower() in vowels:
        return True
    else:
        return False


def get_pig_latin(word):
    last_letter = word[-1]
    lastLetterIsSpecialChar = False

    indexToEnd = len(word)
    if not last_letter.isalnum():
        indexToEnd = len(word) - 1
        lastLetterIsSpecialChar = True

    firstVowelIndex = -1
    for i in range(indexToEnd):
        if isVowel(word[i]):
            firstVowelIndex = i
            break

    if lastLetterIsSpecialChar is False:
        wordToReturn = word[firstVowelIndex:] + word[:firstVowelIndex] + "ay"
    else:
        wordToReturn = word[firstVowelIndex:indexToEnd] + word[:firstVowelIndex] + "ay" + word[-1]

    # no vowels found, so just "ay" at end
    if firstVowelIndex == -1:
        return word + "ay"

    return wordToReturn


@app.route('/get_translation', methods=['POST'])
def get_translation():
    """
    this endpt will provide the pig latin translation to the request with field sentence
    approach: iterate through the sentence then for each word apply:
        -find the index of the first vowel then add:
            (substring before first vowel) + (substring from first vowel to end of word) + "ay"
        -if the last letter of a word string is a special character then append that at end of pig lating translation
        of word
    :return: json
    """
    if not request.json:
        return "please provide sentence field in json request"

    sentence = request.json.get('sentence')

    if len(sentence) == 0 or sentence in ["", None]:
        return jsonify({"translation": ""})

    translatedSentence = ""
    sentence = sentence.split(" ")
    for word in sentence:
        translated = get_pig_latin(word)
        if word != sentence[-1]:
            translatedSentence += translated + " "
        else:
            translatedSentence += translated
    return jsonify({"translation": translatedSentence})


if __name__ == '__main__':
    app.run(host="0.0.0.0")

