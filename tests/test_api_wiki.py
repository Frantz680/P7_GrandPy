def test_api_wiki_url_open_mock(monkeypatch):
    result = {
        "query": {
            "pages": {
                "2179": {
                    "pageid": 2179,
                    "ns": 0,
                    "title": "New York",
                    "extract": 
                    "New York."
                }
            }
        }
    }
    class MockResponse:

        def read(self):
            return result

    def mock_urlopen():
        return MockResponse()

    monkeypatch.setattr("apis.wikipedia.Wikipedia.response_api_wiki", mock_urlopen())
    assert result["query"]["pages"]["2179"]["extract"] == "New York."
