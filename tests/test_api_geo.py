"""Test API Geolocation"""


def test_api_geo_url_open_mock(monkeypatch):
    """
    Geolocation maps api test with monkeypatch
    """

    result = {
        "maps_address": "chez moi", "location_maps": {
            "lat": "4.8", "lng": "2.3"}, "key_api": "Secret"
            }

    def mock_urlopen():
        return result

    monkeypatch.setattr(
        "apis.geolocation.Geolocation.response_api_maps", mock_urlopen())
    assert result["location_maps"]["lat"] == "4.8"
