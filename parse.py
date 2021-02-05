""" Pharse test
Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?
Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.
Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"""

import json
"""
Import the module json.
"""


class Parse:
    """
    This class is used for
    parse value to type user.
    """

    def __init__(self):
        """
        We build the instance of the class.
        """

        self.salutation = ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
        self.verbe = ["suis", "as", "es", "est", "sommes", "etes", "êtes", "fait", "passé", "ai", "indiquer", "avons", "avez", "ont", "avoir", "etre", "être", "indique", "indiques", "indiquons", "indiquez", "indiquent", "voir", "vois", "voit", "voyons", "voyez", "voient", "penser", "pense", "penses", "pensons", "pensez", "pensent", "pouvoir", "peux", "peut", "pouvons", "pouvez", "peuvent", "pourrais", "pourras", "pourra", "pourrons", "pourrez", "pourront", "trouver", "trouve", "trouves", "trouvons", "trouvez", "trouvent", "connaitre", "connaître", "connais", "connait", "connaît", "connaissons", "connaissez", "connaissent", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy",]
        self.pronom = ["d'", "je", "j'", "l'", "la", "à", "tu", "et", "de", "ta", "il", "elle", "on", "nous", "vous", "ils", "se", "elles", "me", "te", "le", "les", "lui", "leur", "qu'", "quoi", "qui", "que", "ou", "où", "ce", "cela", "s'", "un", "une", "-"]
        self.mot = ["grandpy", "grandma", "mamie", "espère", "adresse", "avance", "papy", "hier", "avec", "soir", "plait", "plaît", "comment", "pendant", "au", "belle", "beau", "nuit", "soiree", "soire", "soirée", "soiré", "semaine", "merci", "salutations", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy",]
        self.ponctuation = [".", ",", "!", "?", ";", ":", " ", "'", "-"]
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
        self.question_bot = ["Qu'elle adresse aimerais tu savoir ?", "Quel lieu veux tu connaitre ?", "Ou veux tu allez ?"]
        self.gronder = ["On dit pas des choses comme ça Spirou !", "Je t'ai pas a pris a parler ainsi Spirou !", "Attend que ton père rentre !"]
        self.insulte = ["con", "connard", "salope", "pute", "pd"]
        self.response_negative_bot = ["Je suis sourd, j'ai pas compris", "Pardon, mon petit j'ai pas compris", "Peut tu repeter stp"]
        self.mini_input_value = ""
        self.input_value_important_word = ""
        self.new_input_value = []
        self.tbl_mini_input_value = []
        self.key_word = []
        self.salutation_mini = []
        self.status_salutation = {'salutation': 'False'}
        self.status_insulte = {'insulte': 'False'}
        self.status_api = {'api': 'False'}
        self.status = {}

        """---------On additionne tous les tableaux ensembles pour le parse ---------"""

        self.tbl_remove_word = self.verbe + self.pronom + self.mot + self.ponctuation + self.alphabet

    def parse_str_user(self, value_input):
        """
        On parse la valeur entre par l'utilisateur pour recuperer les mots clés.
        :param value_input: Valeur du input de l'utilisateur.
        :return: Les mots clés.
        """

        self.status_salutation = {'salutation': 'False'}
        self.status_insulte = {'insulte': 'False'}
        self.status_api = {'api': 'False'}

        for index in range(0, len(self.salutation), 1):
            self.salutation_mini.append(self.salutation[index].lower())

        print(value_input)
        print(self.key_word)

        """On met tout les charactere en minuscules"""
        value_input = self.transform_mini(value_input)
            
        """On supprime les ponctuations"""
        value_input = self.remove_ponctuation(value_input)

        """On crée un tableau"""
        value_input_tbl = self.create_tableau(value_input)
        print("keyword tableau", len(value_input_tbl))

        """On regarde dans la chaine si il y a un mot de salutation, si oui on returne un True"""
        self.status_salutation = self.parse_salutation(value_input_tbl)

        """On supprime les mots de salutation"""
        self.key_word = self.remove_word(value_input_tbl, self.salutation_mini)

        """On regarde dans la chaine si il y a un mot d'insulte, si oui on returne un True"""
        self.status_insulte = self.parse_mot_insulte(self.key_word)

        """On supprime les mots d'insultes"""
        self.key_word = self.remove_word(self.key_word, self.insulte)

        """On supprime les mots restants"""
        self.key_word = self.remove_word(self.key_word, self.tbl_remove_word)

        """On additionne les status salutation et insulte ensemble"""
        self.status.update(self.status_salutation)
        self.status.update(self.status_insulte)
        print(self.status)

        print(self.key_word)

        """On regarde dans la chaine si il y a plus que un mot, si oui on return un True"""
        self.status_api = self.parse_api(value_input_tbl)

        """On ajoute le status api aux autres status"""
        self.status.update(self.status_api)

        print(self.status)

        return json.dumps(self.status)
    
    def parse_api(self, param):
        """
        Permet de savoir si on envoi les mots clé l'api
        :param param: Valeur du input de l'utilisateur
        :return: status de l'api True ou False
        """

        if len(param) <= 2:
            print("LONGUEUR", len(param))
            self.status_api = {'api': 'False'}

            """On converti les mots clés en dictionnaire"""
            self.key_word = dict({'key_word': 'Nothing'})

            """On ajoute les status au mots clés"""
            self.status.update(self.key_word) 
            return self.status_api
            
        else:
            print("LONGUEUR",len(param))
            self.status_api = {'api': 'True'}

            """On converti les mots clés en dictionnaire"""
            self.key_word = dict({'key_word': self.key_word})

            """On ajoute les status au mots clés"""
            self.status.update(self.key_word) 
            return self.status_api

    def parse_salutation(self, param):
        """
        Permet de savoir si le papy va dire bonjour.
        :param param: Valeur du input de l'utilisateur
        :return: status de salutation True ou False
        """

        for index in range (0, len(self.salutation_mini), 1):
            for index_param in range (0, len(param), 1):
                if self.salutation_mini[index] == param[index_param]:
                    # if (new_input_value == salutation_mini[index])
                    self.status_salutation = {"salutation": "True"}
                    return self.status_salutation

        return self.status_salutation

    def parse_mot_insulte(self, param):
        """
        Permet de savoir si la maman va dire quelque chose ou non.
        :param param: Valeur du input de l'utilisateur.
        :return: status de insulte True ou False.
        """

        for index in range (0, len(self.insulte), 1):
            for index_param in range (0, len(param), 1):

                if self.insulte[index] == param[index_param]:
                    #if (new_input_value == salutation_mini[index])
                    self.status_insulte = {"insulte": "True"}
                    return self.status_insulte

        return self.status_insulte
        
    def transform_mini(self, param):
        """
        Permet de mettre tout les char en minuscule.
        :param param: Valeur du input de l'utilisateur.
        :return: Valeur du input en minuscule de l'utilisateur.
        """

        return param.lower()

    def remove_ponctuation(self, param):
        """
        Permet de remplacer la ponctuation par un espace.
        :param param: Valeur du input de l'utilisateur.
        :return: Valeur du input sans ponctuation de l'utilisateur.
        """

        for index in range(0, len(self.ponctuation), 1):

            param = param.replace(self.ponctuation[index], " ")
    
        return param

    def create_tableau(self, param):
        """
        On créer un tableau avec notre chaine de charactere de l'utilisateur.
        :param param: Valeur du input de l'utilisateur.
        :return: Valeur du input dans un tableau.
        """

        return param.split(" ")

    def remove_word(self, p_key_word, p_remove_word):
        """
        On remplace tout les mots inutiles par des ""
        :param p_key_word: Valeur du input de l'utilisateur.
        :param p_remove_word: Valeur des mots à supprimer.
        :return: La valeur avec que les mots clés.
        """

        for index in range(0, len(p_key_word), 1):
            for index_remove in range(0, len(p_remove_word), 1):
                if p_key_word[index] == p_remove_word[index_remove]:
                    p_key_word[index] = p_key_word[index].replace(p_remove_word[index_remove], "")
        
        'On ajoute les mots dans un nouveau tableau mais pas les "" '
        new_input_value = []
        for index in range(0, len(p_key_word), 1):
            if p_key_word[index] != "":
                #print(p_key_word)
                new_input_value.append(p_key_word[index])
        
        return new_input_value
