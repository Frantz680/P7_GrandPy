from flask import Flask, render_template, request
app = Flask(__name__)
import requests
import json
from parse import Parse
from api import Api


@app.route('/')
def index():
    return render_template('test.html' )#return envoie la reponse

@app.route('/str_user', methods = ['POST'])
def reponse_user():
    if request.method == 'POST':
        parse_word = []
        key_word = request.form['param_send']
        #print(key_word)
        parse_word = parse_key_word.parse_str_user(key_word)
        #print("parsseee", parse_word)
        response_maps = response_api_maps(parse_word)
        response_wiki = response_api_wiki(parse_word)

        return response_maps + response_wiki

def response_api_maps(parse_word):
    params_maps = {
        "address": str(parse_word),
        "key": ""
    }

    response_maps = maps.request_api(params_maps)
    print(response_maps["results"][0]["formatted_address"])
    return response_maps["results"][0]["formatted_address"]

def response_api_wiki(parse_word):

    params_wiki_location  = {
        "action" : "query",
        "namespace" : "0",
        "list" : "search",
        "srsearch" : str(parse_word),
        "limit" : "10",
        "format" : "json"
    }

    reponse_wiki_location = wiki.request_api(params_wiki_location)

    for page in reponse_wiki_location["query"]["search"]:
        print(page["pageid"])
        page_wiki = page["pageid"]
        break

    params_wiki_page_wiki  = {
        'action': "query",
        'pageids': str(page_wiki),
        'format': "json",
        'prop': 'extracts',
        'explaintext': 1,
        'exsentences': 7
    }
    response_wiki = wiki.request_api(params_wiki_page_wiki)
    return  response_wiki["query"]["pages"][str(page_wiki)]["extract"]

if __name__ == '__main__':
    parse_key_word = Parse()

    wiki = Api("https://fr.wikipedia.org/w/api.php")
    maps = Api("https://maps.googleapis.com/maps/api/geocode/json")
    

    app.run()
    

