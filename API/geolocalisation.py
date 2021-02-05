"""
API GOOGLE Geocoding
"""

import json
from API.api import Api

"""
Import the module json
Import different class.
"""


class Geolocalisation:
    """
    This class is used for information
    retrieval in the API GOOGLE Geocoding.
    """

    def __init__(self):
        """
        We build the instance of the class.
        """

        self.maps = Api("https://maps.googleapis.com/maps/api/geocode/json?")

    def response_api_maps(self, parse_word):
        """
        On envoi une requete a l'api
        Puis on recuperer les informations qui nous interesse
        :param parse_word: Les mots clés recuperer après le parse
        :return: On retourne les valeurs recuperer de l'api en JSON
        """
        print(str(parse_word))
        params_maps = {
            "address": str(parse_word),
            "key": "AIzaSyAm-6JMAnaWFCiAnEQAw3KYCtLGo3SQzA8"
        }

        response_maps = self.maps.request_api(params_maps)
        print("response_maps", response_maps)
        print("results", response_maps["results"])
        maps_adress = response_maps["results"][0]["formatted_address"]
        maps_location = response_maps["results"][0]["geometry"]["location"]
        #print("maps_adress", maps_adress)
        #print("maps_location", maps_location)
        return json.dumps({"adresse_maps": maps_adress, "location_maps": maps_location})
