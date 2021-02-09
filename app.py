"""
Website "GrandPy" Grandpa knows a lot.
"""

from flask import Flask, render_template, request
app = Flask(__name__)
import json

from parse_word.parse import Parse
from API.geolocalisation import Geolocalisation
from API.wikipedia import Wikipedia

"""
Import different class.
"""


@app.route('/')
def index():
    return render_template('test.html')
    # return envoie la reponse


@app.route('/str_user', methods=['POST'])
def response_user():
    if request.method == 'POST':
        key_word = request.form['param_send']
        #print(key_word)
        parse_word = json.loads(parse_key_word.parse_str_user(key_word))
        print("APP python", parse_word)
        #print("ERREUR", parse_word['erreur'])
        #print(parse_word['key_word'])

        if parse_word['insult'] == 'True':

            if parse_word['salutation'] == 'True':
                
                if parse_word['api'] == 'True':
                    return api_sending_response(parse_word)

                return api_sending_response(parse_word)

            else:
                return parse_word

        elif parse_word['salutation'] == 'True':

            if parse_word['api'] == 'True':
                return api_sending_response(parse_word)

            return parse_word

        else:
            return parse_word


def api_sending_response(parse_word):
    """

    :param parse_word:
    :return:
    """

    #print("parsseee", parse_word)
    response_maps = json.loads(api_geo.response_api_maps(parse_word['key_word']))
    response_wiki = api_wiki.response_api_wiki(parse_word['key_word'])
    #print(response_maps + response_wiki)
    #On return du JSON
    #print(response_maps)
    #print("ENVOImaps", response_maps, "ENVOImaps", response_wiki)
    #print( json.dumps({"maps": response_maps, "wiki" : response_wiki}))
    print(response_maps)
    #print(json.dumps({"adresse": response_maps["maps_address"], "location": response_maps["location_maps"],\
    #"wiki" : response_wiki, "insult" : parse_word["insult"]}))
    return json.dumps({"adresse": response_maps["maps_address"], "location": response_maps["location_maps"],\
        "wiki": response_wiki, "insult": parse_word["insult"], "salutation": parse_word["salutation"],\
        "api": parse_word["api"], "key_api": response_maps["key_api"]})


if __name__ == '__main__':

    parse_key_word = Parse()
    api_wiki = Wikipedia()
    api_geo = Geolocalisation()

    app.run()
