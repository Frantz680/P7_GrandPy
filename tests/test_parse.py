import json
from parse_word.parse import Parse 
parse_key_word = Parse()

results_response_parse = parse_key_word.parse_str_user("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?")
with open("results_test_parse.json", "w"):
    json.dump(results_response_parse, open("results_test_parse.json", "w"))


def test_response_parse(monkeypatch):
    with open("results_test_parse.json"):
        results_response_parse = json.load(open("results_test_parse.json"))

    def mock_response_parse():
        return results_response_parse

    monkeypatch.setattr(
      "parse_word.parse.Parse",
      mock_response_parse
      )

    assert parse_key_word.parse_str_user("Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?") == results_response_parse