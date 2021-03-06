"""
API GOOGLE Geocoding
"""

import json

from apis.api import Api
from env import key_maps


class Geolocation:
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
        We send a request to the API.
        Then we retrieve the information that interests us.
        :param parse_word: Keywords to recover after parse.
        :return: We return the values retrieved from the API in JSON.
        """

        params_maps = {
            "address": str(parse_word),
            "key": key_maps
        }

        response_maps = self.maps.request_api(params_maps)
        maps_address = response_maps["results"][0]["formatted_address"]
        maps_location = response_maps["results"][0]["geometry"]["location"]
        return json.dumps({"maps_address": maps_address,
                           "location_maps": maps_location,
                           "key_api": key_maps})
