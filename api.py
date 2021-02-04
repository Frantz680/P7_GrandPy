import requests
import json


"""
API WIKI MEDIA
"""

"""
url_wikipedia = "https://fr.wikipedia.org/w/api.php?action=query&format=json&srsearch=musee,art,histoire,fribourg&list=search&limit=10&namespace=0"

url_wikimedia = "https://en.wikimedia.org/w/api.php?action=query&format=json&search=Paris&limit=1000&namespace=0"

url_wikimedia = "https://www.mediawiki.org/w/api.php?action=opensearch&format=json&search=tour_eiffel&limit=100&namespace=0"
"""

class Api:

    def __init__(self, p_url):
        """
        We build the instance of the class.
        """
        
        self.url_api = p_url


    def request_api(self, p_params):

        response_api = json.loads(requests.get(url=self.url_api, params=p_params).text)
        return response_api

