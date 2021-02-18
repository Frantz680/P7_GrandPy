def test_api_geo_url_open_mock(monkeypatch):

    result = {"maps_address": "chez moi", "location_maps": {"lat": "4.8", "lng": "2.3"}, "key_api": "Secret"}


    class MockResponse:

        def read(self):
            """Wikipedia api test with monkeypatch"""
            return result

    def mock_urlopen():
        return MockResponse()

    monkeypatch.setattr("apis.geolocation.Geolocation.response_api_maps", mock_urlopen())
    assert result["location_maps"]["lat"] == "4.8"
