"""
API Wikipedia.
"""

from API.api import Api

"""
Import different class.
"""


class Wikipedia:
    """
    This class is used for information
    retrieval in the API Wikipedia.
    """

    def __init__(self):
        """
        We build the instance of the class.
        """

        self.wiki = Api("https://fr.wikipedia.org/w/api.php")

    def response_api_wiki(self, parse_word):
        """
        On envoi une requete a l'api
        Puis on recuperer les informations qui nous interesse
        :param parse_word: Les mots clés recuperer après le parse
        :return: On retourne les valeurs recuperer de l'api en JSON
        """

        params_wiki_location = {
            "action": "query",
            "namespace": "0",
            "list": "search",
            "srsearch": str(parse_word),
            "limit": "10",
            "format": "json"
        }
        
        reponse_wiki_location = self.wiki.request_api(params_wiki_location)

        for page in reponse_wiki_location["query"]["search"]:
            #print(page["pageid"])
            page_wiki = page["pageid"]
            break

        params_wiki_page_wiki = {
            'action': "query",
            'pageids': str(page_wiki),
            'format': "json",
            'prop': 'extracts',
            'explaintext': 1,
            'exsentences': 7
        }
        
        response_wiki = self.wiki.request_api(params_wiki_page_wiki)
        #print(wiki.request_api(params_wiki_page_wiki))
        return response_wiki["query"]["pages"][str(page_wiki)]["extract"]
