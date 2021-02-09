import json

from API.geolocalisation import Geolocalisation

api_geo = Geolocalisation()

results_response_api_geo_loc = api_geo.response_api_maps({"paris"})
with open("results_test_geo.json", "w"):
    json.dump(results_response_api_geo_loc, open("results_test_geo.json", "w"))


def test_response_api_geo_loc(monkeypatch):
    with open("results_test_geo.json"):
        results_response_api_geo_loc = json.load(open("results_test_geo.json"))

    def mock_response_api_maps():
        return results_response_api_geo_loc

    monkeypatch.setattr(
      "API.geolocalisation.Geolocalisation",
      mock_response_api_maps
      )

    assert api_geo.response_api_maps({"paris"}) == results_response_api_geo_loc
