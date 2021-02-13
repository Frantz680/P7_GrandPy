"""Test API Geolocation"""

import json

from apis.geolocation import Geolocation

api_geo = Geolocation()

"""
We send a keyword to the google maps api.
The result is put in a JSON file.
"""
results_response_api_geo_loc = api_geo.response_api_maps({"paris"})
with open("results_test_geo.json", "w"):
    json.dump(results_response_api_geo_loc, open("results_test_geo.json", "w"))


def test_response_api_geo_loc(monkeypatch):
    """
    We send a keyword to our monkeypatch.
    If the result is the same as our file,
    That we just created then the test is green.
    """

    with open("results_test_geo.json"):
        results_mock_api_geo = json.load(open("results_test_geo.json"))

    def mock_response_api_maps():
        return results_mock_api_geo

    monkeypatch.setattr(
      "apis.geolocation.Geolocation",
      mock_response_api_maps
      )

    assert api_geo.response_api_maps({"paris"}) == results_mock_api_geo
