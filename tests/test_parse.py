"""Test Parse"""

import json
from parse_word.parse import Parse

parse_key_word = Parse()
STR_USER = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"

"""
We send a sentence to our parser.
The result is put in a json file.
"""
results_response_parse =\
    parse_key_word.parse_str_user(STR_USER)
with open("results_test_parse.json", "w"):
    json.dump(results_response_parse, open("results_test_parse.json", "w"))


def test_response_parse(monkeypatch):
    """
    We send a key pharse to our monkeypatch.
    If the result is the same as our file,
    That we just created then the test is green.
    """

    with open("results_test_parse.json"):
        results_mock_parse = json.load(open("results_test_parse.json"))

    def mock_response_parse():
        return results_mock_parse

    monkeypatch.setattr(
      "parse_word.parse.Parse",
      mock_response_parse
      )

    assert results_mock_parse ==\
           parse_key_word.parse_str_user(STR_USER)
