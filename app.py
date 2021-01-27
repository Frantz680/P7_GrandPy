from flask import Flask, render_template, request
app = Flask(__name__)
import requests
import json
from chat_bot import Chat_bot 

def call_google_maps(lieu):
    """
    On appelle l'api de google maps pour recuperer l'adresse et les coordonnées.
    """

    url_maps = "https://maps.googleapis.com/maps/api/geocode/json"
    params_maps = {
        "address": lieu,
        "key": ""
        } 
    reponse_maps = json.loads(requests.get(url=url_maps, params=params_maps).text)


    print("REPONSE API MAPS")
    print(reponse_maps)
    print("REPONSE LOCALISATION")
    print(reponse_maps["results"])



def call_wikipedia_text(page_wiki):
    """
    On appelle de nouveau l'api de wikipedia avec la page pour recuperer le texte.
    """

    session_wiki = requests.session()

    url_wiki= "https://fr.wikipedia.org/w/api.php"

    params_wiki  = {
        'action': "query",
        'pageids': page_wiki,
        'format': "json",
        'prop': 'extracts',
        'explaintext': 1,
        'exsentences': 7
    }

    reponse_wiki = json.loads(session_wiki.get(url=url_wiki, params=params_wiki).text)
    """print("TEXTE")
    print(reponse_wiki["query"]["pages"][str(page_wiki)]["extract"])"""
    return reponse_wiki["query"]["pages"][str(page_wiki)]["extract"]


def call_wikipedia_page(lieu):
    """
    On appele l'api de wikipedia et on recupere la page de notre titre.
    """
    
    session_wiki = requests.session()

    url_wiki= "https://fr.wikipedia.org/w/api.php"

    params_wiki  = {
        "action" : "query",
        "namespace" : "0",
        "list" : "search",
        "srsearch" : lieu,
        "limit" : "10",
        "format" : "json"
    }

    reponse_wiki = json.loads(session_wiki.get(url=url_wiki, params=params_wiki).text)

    #print(reponse_wiki["query"]["search"])
    

    for page in reponse_wiki["query"]["search"]:
        #print(page["pageid"])
        page_wiki = page["pageid"]
        break

    print(page_wiki)

    return call_wikipedia_text(page_wiki)


@app.route('/')
def index():
    return render_template('test.html' )#return envoie la reponse

@app.route('/key_word_user', methods = ['POST'])
def reponse_user():
    if request.method == 'POST':
        key_word = request.form['param_send']
        #print(key_word)
        call_google_maps(key_word)
        return call_wikipedia_page(key_word)

if __name__ == '__main__':
    app.run()
    

