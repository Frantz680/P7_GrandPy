from flask import Flask, render_template, request
app = Flask(__name__)
import json
from parse import Parse
from api import Api


@app.route('/')
def index():
    return render_template('test.html' )#return envoie la reponse

@app.route('/str_user', methods = ['POST'])
def reponse_user():
    if request.method == 'POST':
        key_word = request.form['param_send']
        #print(key_word)
        parse_word = json.loads(parse_key_word.parse_str_user(key_word))
        print("APP python", parse_word)
        #print("ERREUR", parse_word['erreur'])
        #print(parse_word['key_word'])

        if parse_word['insulte'] == 'True':

            if parse_word['salutation'] == 'True':

                if parse_word['api'] == 'True':
                    return api_envoi_reponse(parse_word)

            else:   
                return parse_word

        elif parse_word['salutation'] == 'True':
            
            if parse_word['api'] == 'True':
                return api_envoi_reponse(parse_word)

            return parse_word

        else:   
            return parse_word

def api_envoi_reponse(parse_word):            
    #print("parsseee", parse_word)
    response_maps = json.loads(response_api_maps(parse_word['key_word']))
    response_wiki = response_api_wiki(parse_word['key_word'])
    #print(response_maps + response_wiki)
    #On return du JSON
    #print(response_maps)
    #print("ENVOImaps", response_maps, "ENVOImaps", response_wiki) 
    #print( json.dumps({"maps": response_maps, "wiki" : response_wiki}))
    #print(response_maps)
    #print(json.dumps({"adresse": response_maps["adresse_maps"], "location": response_maps["location_maps"],\
    #"wiki" : response_wiki, "insulte" : parse_word["insulte"]}))
    return json.dumps({"adresse": response_maps["adresse_maps"], "location": response_maps["location_maps"],\
        "wiki" : response_wiki, "insulte" : parse_word["insulte"], "salutation" : parse_word["salutation"], "api" : parse_word["api"]})



def response_api_maps(parse_word):
    params_maps = {
        "address": str(parse_word),
        "key": "AIzaSyChZyqQKTyt4r4GEXd9csdM7qUNXu5QT2A"
    }

    response_maps = maps.request_api(params_maps)
    maps_adress = response_maps["results"][0]["formatted_address"]
    maps_location = response_maps["results"][0]["geometry"]["location"]
    #print("maps_adress", maps_adress)
    #print("maps_location", maps_location)
    return json.dumps({"adresse_maps": maps_adress, "location_maps" : maps_location})

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
        #print(page["pageid"])
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
    #print(wiki.request_api(params_wiki_page_wiki))
    return  response_wiki["query"]["pages"][str(page_wiki)]["extract"]

if __name__ == '__main__':
    parse_key_word = Parse()

    wiki  =  Api ( "https://fr.wikipedia.org/w/api.php" )
    maps  =  Api ( "https://maps.googleapis.com/maps/api/geocode/json" )

    app.run()
    