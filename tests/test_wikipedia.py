"""Test API Wikipedia"""

import json

from apis.wikipedia import Wikipedia

api_wiki = Wikipedia()

"""
We send a keyword to the Wikipedia api.
The result is put in a JSON file.
"""
results_response_api_wiki_text = api_wiki.response_api_wiki("new,york")
with open("results_test_wiki.json", "w"):
    json.dump(results_response_api_wiki_text,
              open("results_test_wiki.json", "w"))


def test_response_api_wiki_text(monkeypatch):
    """
    We send a keyword to our monkeypatch.
    If the result is the same as our file,
    That we just created then the test is green.
    """

    with open("results_test_wiki.json"):
        results_mock_api_wiki = json.load(open("results_test_wiki.json"))

    def mock_response_api_wiki():
        return results_mock_api_wiki

    monkeypatch.setattr(
      "apis.wikipedia.Wikipedia",
      mock_response_api_wiki
      )

    assert api_wiki.response_api_wiki("new,york") == results_mock_api_wiki
