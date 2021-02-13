"""
API Wikipedia.
"""

from apis.api import Api


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
        self.page_wiki = any

    def response_api_wiki(self, parse_word):
        """
        We send a request to the API.
        Then we retrieve the information that interests us.
        :param parse_word: Keywords to recover after parse.
        :return: We return the values retrieved from the API in JSON.
        """

        params_wiki_location = {
            "action": "query",
            "namespace": "0",
            "list": "search",
            "srsearch": str(parse_word),
            "limit": "10",
            "format": "json"
        }

        response_wiki_location = self.wiki.request_api(params_wiki_location)

        for page in response_wiki_location["query"]["search"]:
            self.page_wiki = page["pageid"]
            break

        params_wiki_page_wiki = {
            'action': "query",
            'pageids': str(self.page_wiki),
            'format': "json",
            'prop': 'extracts',
            'explaintext': 1,
            'exsentences': 7
        }

        response_wiki = self.wiki.request_api(params_wiki_page_wiki)
        return response_wiki["query"]["pages"][str(self.page_wiki)]["extract"]
