"""
API
"""

import requests
import json

"""
url_wikipedia = "https://fr.wikipedia.org/w/api.php?action=query&format=json&srsearch=musee,art,histoire,fribourg&list=search&limit=10&namespace=0"

url_wikimedia = "https://en.wikimedia.org/w/api.php?action=query&format=json&search=Paris&limit=1000&namespace=0"

url_wikimedia = "https://www.mediawiki.org/w/api.php?action=opensearch&format=json&search=tour_eiffel&limit=100&namespace=0"

url_maps = "https://maps.googleapis.com/maps/api/geocode/json&address=openclassrooms&key="
"""


class Api:
    """
    This class is used to do the requests at each API.
    """

    def __init__(self, p_url):
        """
        We build the instance of the class.
        """
        
        self.url_api = p_url

    def request_api(self, p_params):
        """
        This method allows you to make the request.
        :param p_params: On recuperer chaque URL de chaque API.
        :return: On retourne la reponse de l'API.
        """

        response_api = json.loads(requests.get(url=self.url_api, params=p_params).text)
        return response_api

