"""
API
"""

import json
import requests


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
        :param p_params: We retrieve each URL of each API.
        :return: We return the response from the API.
        """

        response_api =\
            json.loads(requests.get(url=self.url_api, params=p_params).text)
        return response_api
