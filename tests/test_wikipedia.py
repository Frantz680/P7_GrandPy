import json

from API.wikipedia import Wikipedia

api_wiki = Wikipedia()

results_response_api_wiki_text = api_wiki.response_api_wiki("new,york")
with open("results_test_wiki.json", "w"):
    json.dump(results_response_api_wiki_text, open("results_test_wiki.json", "w"))


def test_response_api_wiki_text(monkeypatch):
    with open("results_test_wiki.json"):
        results_response_api_wiki_text = json.load(open("results_test_wiki.json"))

    def mock_response_api_wiki():
        return results_response_api_wiki_text

    monkeypatch.setattr(
      "API.wikipedia.Wikipedia",
      mock_response_api_wiki
      )

    assert api_wiki.response_api_wiki("new,york") == results_response_api_wiki_text
