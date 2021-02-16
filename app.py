"""
Website "GrandPy" Grandpa knows a lot.
"""
import json

from parse_word.parse import Parse
from apis.geolocation import Geolocation
from apis.wikipedia import Wikipedia

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """
    return sends the response to the browser
    """

    return render_template('index.html')


@app.route('/str_user', methods=['POST'])
def response_user():
    """
    We process the POST type request.
    We get the value.
    We send it to the parse.
    :return: We return an answer.
    """

    if request.method == 'POST':

        key_word = request.form['param_send']
        parse_word = json.loads(parse_key_word.parse_str_user(key_word))

        if parse_word['insult'] == 'True':

            if parse_word['salutation'] == 'True':

                if parse_word['api'] == 'True':
                    return api_sending_response(parse_word)

                else:
                    return api_sending_response(parse_word)

            else:
                return parse_word

        elif parse_word['salutation'] == 'True':

            if parse_word['api'] == 'True':
                return api_sending_response(parse_word)

            else:
                return parse_word

        else:
            return parse_word


def api_sending_response(parse_word):
    """
    We send the keywords to the different APIs.
    :param parse_word: The value after the parse.
    :return: We send the response from the parse and the APIs to the browser.
    """

    response_maps = \
        json.loads(api_geo.response_api_maps(parse_word['key_word']))
    response_wiki = \
        api_wiki.response_api_wiki(parse_word['key_word'])

    return \
        json.dumps({"address": response_maps["maps_address"],
                    "location": response_maps["location_maps"],
                    "wiki": response_wiki,
                    "insult": parse_word["insult"],
                    "salutation": parse_word["salutation"],
                    "api": parse_word["api"],
                    "key_api": response_maps["key_api"]})


if __name__ == '__main__':
    parse_key_word = Parse()
    api_wiki = Wikipedia()
    api_geo = Geolocation()

    app.run(debug=True)
