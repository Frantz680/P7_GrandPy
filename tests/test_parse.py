"""Test Parse"""

def test_parse_mock(monkeypatch):

    result = {"salutation": "True", "insult": "False", "key_word": ["openclassrooms"], "api": "True"}

    class MockResponse:

        def read(self):
            return result

    def mock_parse():
        return MockResponse()

    monkeypatch.setattr("parse_word.parse.Parse.parse_str_user", mock_parse())
    assert result["key_word"] == ["openclassrooms"]