"""
Parse
"""

import json


class Parse:
    """
    This class is used for
    parse value to type user.
    """

    def __init__(self):
        """
        We build the instance of the class.
        """

        self.salutation = \
            ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
        self.verb = \
            ["suis", "as", "es", "est", "sommes", "etes", "êtes",
             "fait", "passé", "ai", "indiquer", "avons", "avez", "ont",
             "avoir", "etre", "être", "indique", "indiques", "indiquons",
             "indiquez", "indiquent", "voir", "vois", "voit", "voyons",
             "voyez", "voient", "penser", "pense", "penses", "pensons",
             "pensez", "pensent", "pouvoir", "peux", "peut", "pouvons",
             "pouvez", "peuvent", "pourrais", "pourras", "pourra",
             "pourrons", "pourrez", "pourront", "trouver", "trouve",
             "trouves", "trouvons", "trouvez", "trouvent", "connaitre",
             "connaître", "connais", "connait", "connaît",
             "connaissons", "connaissez", "connaissent",
             "grandpy", "grandpy", "grandpy", "grandpy", "grandpy",
             "grandpy", "grandpy", ]
        self.pronoun = \
            ["d'", "je", "j'", "l'", "la", "à", "tu", "et",
             "de", "ta", "il", "elle", "on", "nous", "vous",
             "ils", "se", "elles", "me", "te", "le", "les", "lui",
             "leur", "qu'", "quoi", "qui", "que", "ou", "où", "ce",
             "cela", "s'", "un", "une", "-"]
        self.word = \
            ["grandpy", "grandma", "mamie", "espère", "adresse",
             "avance", "papy", "hier", "avec", "soir", "plait",
             "plaît", "comment", "pendant", "au", "belle", "beau",
             "nuit", "soiree", "soire", "soirée", "soiré", "semaine",
             "merci", "salutations", "grandpy", "grandpy", "grandpy",
             "grandpy", "grandpy", "grandpy", "grandpy", ]
        self.punctuation = [".", ",", "!", "?", ";", ":", " ", "'", "-"]
        self.alphabet = \
            ["a", "b", "c", "d", "e", "f", "g", "h",
             "i", "j", "k", "l", "m", "n", "o", "p",
             "q", "r", "s", "t", "u", "v", "w", "y", "z"]
        self.question_bot = \
            ["Qu'elle adresse aimerais tu savoir ?",
             "Quel lieu veux tu connaitre ?",
             "Que veux tu savoir ?"]
        self.scold = \
            ["On dit pas des choses comme ça Spirou !",
             "Je t'ai pas a pris a parler ainsi Spirou !",
             "Attend que ton père rentre !"]
        self.insult = ["con", "connard", "salope", "pute", "pd"]
        self.response_negative_bot = \
            ["Je suis sourd, j'ai pas compris",
             "Pardon, mon petit j'ai pas compris", "Peut tu repeter stp"]
        self.mini_input_value = ""
        self.input_value_important_word = ""
        self.new_input_value = []
        self.tbl_mini_input_value = []
        self.key_word = []
        self.salutation_mini = []
        self.status_salutation = {'salutation': 'False'}
        self.status_insult = {'insult': 'False'}
        self.status_api = {'api': 'False'}
        self.status = {}

        """---------We add the arrays together for the parse.---------"""

        self.tbl_remove_word = \
            self.verb + self.pronoun +\
            self.word + self.punctuation +\
            self.alphabet

    def parse_str_user(self, value_input):
        """
        We parse the value entered by the user to retrieve the keywords.
        :param value_input: User input value.
        :return: Keywords.
        """

        self.status_salutation = {'salutation': 'False'}
        self.status_insult = {'insult': 'False'}
        self.status_api = {'api': 'False'}

        for index in range(0, len(self.salutation), 1):
            self.salutation_mini.append(self.salutation[index].lower())

        # We put all the characters in lowercase.
        value_input = self.transform_mini(value_input)

        # We remove the punctuation.
        value_input = self.remove_punctuation(value_input)

        # We create a table.
        value_input_tbl = self.create_array(value_input)

        """
        We look in the chain if there
        is a word of greeting, if so we
        return a True.
        """
        self.status_salutation = self.parse_salutation(value_input_tbl)

        # We delete the words of greeting.
        self.key_word = self.remove_word(value_input_tbl, self.salutation_mini)

        """
        We look in the chain if there
        is a word of insult, if so we
        return a True.
        """
        self.status_insult = self.parse_word_insult(self.key_word)

        # We delete the words of insults.
        self.key_word = self.remove_word(self.key_word, self.insult)

        # We delete the remaining words.
        self.key_word = self.remove_word(self.key_word, self.tbl_remove_word)

        # We add the statuses greeting and insult together.
        self.status.update(self.status_salutation)
        self.status.update(self.status_insult)

        """
        We look in the chain if there are more
        than two words, if so we return a True.
        """
        self.status_api = self.parse_api(value_input_tbl)

        # We add the API status to the other statuses.
        self.status.update(self.status_api)

        return json.dumps(self.status)

    def parse_api(self, param):
        """
        Allows you to know if we send the API keywords.
        :param param: User input value.
        :return: API status True or False.
        """

        if len(param) <= 2:
            self.status_api = {'api': 'False'}

            # We convert the keywords into a dictionary.
            self.key_word = dict({'key_word': 'Nothing'})

            # We add the statuses to the keywords.
            self.status.update(self.key_word)
            return self.status_api

        elif len(param) > 2:
            self.status_api = {'api': 'True'}

            # We convert the keywords into a dictionary.
            self.key_word = dict({'key_word': self.key_word})

            # We add the statuses to the keywords.
            self.status.update(self.key_word)
            return self.status_api

        else:
            self.status_api = {'api': 'False'}

            # We convert the keywords into a dictionary.
            self.key_word = dict({'key_word': 'Nothing'})

            # We add the statuses to the keywords.
            self.status.update(self.key_word)
            return self.status_api

    def parse_salutation(self, param):
        """
        Lets know if the grandpa is going to say hello.
        :param param: User input value.
        :return: Salutation status True or False.
        """

        for index in range(0, len(self.salutation_mini), 1):
            for index_param in range(0, len(param), 1):

                if self.salutation_mini[index] == param[index_param]:
                    self.status_salutation = {"salutation": "True"}
                    return self.status_salutation

        return self.status_salutation

    def parse_word_insult(self, param):
        """
        Lets know if mom is going to say something or not.
        :param param: User input value.
        :return: Insult status True or False.
        """

        for index in range(0, len(self.insult), 1):
            for index_param in range(0, len(param), 1):

                if self.insult[index] == param[index_param]:
                    self.status_insult = {"insult": "True"}
                    return self.status_insult

        return self.status_insult

    @staticmethod
    def transform_mini(param):
        """
        Allows to put all char in lowercase.
        :param param: User input value.
        :return: User input lowercase value.
        """

        return param.lower()

    def remove_punctuation(self, param):
        """
        Used to replace punctuation with a space.
        :param param: User input value.
        :return: Value of the input without user punctuation.
        """

        for index in range(0, len(self.punctuation), 1):
            param = param.replace(self.punctuation[index], " ")

        return param

    @staticmethod
    def create_array(param):
        """
        We create a table with our user string.
        :param param: User input value.
        :return: Value of the input in an array.
        """

        return param.split(" ")

    @staticmethod
    def remove_word(p_key_word, p_remove_word):
        """
        We replace all unnecessary words with "".
        Then we delete them.
        :param p_key_word: User input value.
        :param p_remove_word: Value of words to delete.
        :return: The value with that keywords.
        """

        for index in range(0, len(p_key_word), 1):
            for index_remove in range(0, len(p_remove_word), 1):

                if p_key_word[index] == p_remove_word[index_remove]:
                    p_key_word[index] = p_key_word[index]\
                        .replace(p_remove_word[index_remove], "")

        # We add the words in a new table but not the "".
        new_input_value = []

        for index in range(0, len(p_key_word), 1):

            if p_key_word[index] != "":
                new_input_value.append(p_key_word[index])

        return new_input_value
