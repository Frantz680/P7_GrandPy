"""Test API Wikipedia"""


def test_api_wiki_url_open_mock(monkeypatch):
    """
    Wikipedia api test with monkeypatch
    """

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

    def mock_urlopen():
        return result

    monkeypatch.setattr(
        "apis.wikipedia.Wikipedia.response_api_wiki", mock_urlopen())
    assert result["query"]["pages"]["2179"]["extract"] == "New York."
