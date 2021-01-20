import requests
import json

"""
API WIKI MEDIA
"""

"""
url_wikipedia = "https://fr.wikipedia.org/w/api.php?action=query&format=json&srsearch=musee,art,histoire,fribourg&list=search&limit=10&namespace=0"

url_wikimedia = "https://fr.wikimedia.org/w/api.php?action=query&format=json&search=Paris&limit=1000&namespace=0"

url_wikimedia = "https://www.mediawiki.org/w/api.php?action=opensearch&format=json&search=tour_eiffel&limit=100&namespace=0"
"""

def call_wikipedia_text(page_wiki):
    """
    On appelle de nouveau l'api de wikipedia avec la page pour recuperer le texte
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
    print("TEXTE")
    print(reponse_wiki["query"]["pages"][str(page_wiki)]["extract"])

    session_wiki = requests.session()


def call_wikipedia_page():
    """
    On appele l'api de wikipedia et on recupere la page de notre titre
    """

    session_wiki = requests.session()

    url_wiki= "https://fr.wikipedia.org/w/api.php"

    params_wiki  = {
        "action" : "query",
        "namespace" : "0",
        "list" : "search",
        "srsearch" : "New_york",
        "limit" : "10",
        "format" : "json"
    }

    reponse_wiki = json.loads(session_wiki.get(url=url_wiki, params=params_wiki).text)

    print(reponse_wiki["query"]["search"])
    

    for page in reponse_wiki["query"]["search"]:
        print(page["pageid"])
        page_wiki = page["pageid"]
        break

    print(page_wiki)

    call_wikipedia_text(page_wiki)


call_wikipedia_page()



