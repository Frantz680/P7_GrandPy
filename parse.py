""" Pharse test
Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?
Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.
Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"""

import json
import random
   
class Parse:

    def __init__(self):

        self.salutation = ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
        self.verbe = ["suis", "as", "es", "est", "sommes", "etes", "êtes", "fait", "passé", "ai", "indiquer", "avons", "avez", "ont", "avoir", "etre", "être", "indique", "indiques", "indiquons", "indiquez", "indiquent", "voir", "vois", "voit", "voyons", "voyez", "voient", "penser", "pense", "penses", "pensons", "pensez", "pensent", "pouvoir", "peux", "peut", "pouvons", "pouvez", "peuvent", "pourrais", "pourras", "pourra", "pourrons", "pourrez", "pourront", "trouver", "trouve", "trouves", "trouvons", "trouvez", "trouvent", "connaitre", "connaître", "connais", "connait", "connaît", "connaissons", "connaissez", "connaissent", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy",]
        self.pronom = ["d'", "je", "j'", "l'", "la", "à", "tu", "et", "de", "ta", "il", "elle", "on", "nous", "vous", "ils", "se", "elles", "me", "te", "le", "les", "lui", "leur", "qu'", "quoi", "qui", "que", "ou", "où", "ce", "cela", "s'", "un", "une", "-"]
        self.mot = ["grandpy", "grandma", "mamie", "espère", "adresse", "avance", "papy", "hier", "avec", "soir", "plait", "plaît", "comment", "pendant", "au", "belle", "beau", "nuit", "soiree", "soire", "soirée", "soiré", "semaine", "merci", "salutations", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy",]
        self.ponctuation = [".", ",", "!", "?", ";", ":", " ", "'", "-"]
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
        self.question_bot = ["Qu'elle adresse aimerais tu savoir ?", "Quel lieu veux tu connaitre ?", "Ou veux tu allez ?"]
        self.gronder = ["On dit pas des choses comme ça Spirou !", "Je t'ai pas a pris a parler ainsi Spirou !", "Attend que ton père rentre !"]
        self.mot_interdit = ["con", "connard", "salope", "salope", "pd"]
        self.response_negative_bot = ["Je suis sourd, j'ai pas compris", "Pardon, mon petit j'ai pas compris", "Peut tu repeter stp"]
        self.mini_input_value = ""
        self.input_value_important_word = ""
        self.new_input_value = []
        self.tbl_mini_input_value = []
        self.key_word = []
        self.salutation_mini = []
        self.erreur = {'erreur': 'False'}
        self.salutation_dict = {'salutation': 'False'}
        self.random = random.choice(self.salutation)

        #---------On additionne tous les tableaux ensembles pour le parse ---------

        self.tbl_remove_word = self.verbe + self.pronom + self.mot + self.ponctuation + self.alphabet

    def parse_str_user(self, value_input):
        self.salutation_dict = {'salutation': 'False'}
        self.erreur = {'erreur': 'False'}
        for index in range (0, len(self.salutation), 1):
            self.salutation_mini.append(self.salutation[index].lower())
        
        #print("SALUTATION MINI", self.salutation_mini)
 
        value_input = self.transform_mini(value_input)
        #console.log("input.value", input.value)
            
        value_input = self.remove_ponctuation(value_input)
        #console.log("input.value2", input.value)

        self.key_word = self.create_tableau(value_input)
        #console.log("key_word", key_word)

        #print("Longueur",len(self.key_word))
        #print(self.key_word)
        #papy ne comprend pas en dessous de deux mots
        if (len(self.key_word) <= 2):
                
            self.erreur = {'erreur': 'True'}
            
            self.salutation_dict = self.parse_salutation(self.key_word)
            print("SALUT",self.salutation_dict)

            if self.salutation_dict['salutation'] == 'True':
                self.erreur.update(self.salutation_dict)
                print(self.erreur)
                return json.dumps(self.erreur)

            else:
                self.erreur.update(self.salutation_dict)
                print(self.erreur)
                return json.dumps(self.erreur)

        self.key_word = self.remove_word(self.key_word, self.tbl_remove_word)
        #console.log("key_word2", key_word)

        #console.log("new input value", new_input_value)

        if self.parse_mot_interdit(self.key_word):
            #print(self.gronder[random])
            print("GRONDER")
            return 
        


        #if self.parse_salutation(self.key_word):
            #random = random.choice(self.salutation)
            #self.print_papy(self.salutation[random])

        #self.print_papy("envoi serveur " + str(key_word))
        #request_ajax(str(key_word), response_server)

        #random = getRandomInt(0, response_negative_bot.length)
        #print_papy(response_negative_bot[random])
            #return True

        self.key_word = self.remove_word(self.key_word, self.salutation_mini)
        # On ajout le dictionnaire api au mots clés
        self.key_word = dict({'key_word': self.key_word})
        api = {'erreur': 'False', 'api': 'True', 'salutation': 'True'}
        y = api.update(self.key_word)
        return json.dumps(api)

    def parse_salutation(self, param):
    # si un mot de saluation est présent dans la pharse le bot salut

        for index in range (0, len(self.salutation_mini), 1):
            for index_param in range (0, len(param), 1):
                if self.salutation_mini[index] == param[index_param]:
                    # if (new_input_value == salutation_mini[index])
                    self.salutation_dict = {"salutation": "True"}
                    return self.salutation_dict

        return self.salutation_dict
                
    """for (let index = 0; index < mot_interdit.length; index++) {

        if (mini_input_value.includes(mot_interdit[index])) {
            // if (mini_input_value == salutation_mini[index]){
            random = getRandomInt(0, gronder.length - 1);
            print_maman(gronder[random]);
            return true;
            }"""

    

    def parse_mot_interdit(self, param):
    # si un mot interdit est présent dans la pharse la maman repond

        for index in range (0, len(self.mot_interdit), 1):
            for index_param in range (0, len(param), 1):

                if self.mot_interdit[index] == param[index_param]:
                    #if (new_input_value == salutation_mini[index])
                    gronder = {"gronder": "True"}
                    return gronder
        
    def transform_mini(self, param):
    # on met toute les char en minuscule
        return param.lower()

    def remove_ponctuation(self, param):
    # on remplace la ponctuation par un espace 

        for index in range (0,len(self.ponctuation),1):

            param = param.replace(self.ponctuation[index], " ")
    
        return param

    def create_tableau(self, param): 
        # on créer un tableau avec notre chaine de caractere
        return param.split(" ")


    def remove_word(self, p_key_word, p_remove_word):
        # On remplace(supprimer) tout les mots inutiles dans notre tableau 
        for index in range (0,len(p_key_word),1):
            for index_remove in range (0,len(p_remove_word),1): 
                if (p_key_word[index] == p_remove_word[index_remove]):
                    p_key_word[index] = p_key_word[index].replace(p_remove_word[index_remove], "")
        
        #print("p_key_word1", p_key_word )
        
        #print("p_key_word4444")

        # On ajoute les mots dans un nouveau tableau mais pas les "" 
        new_input_value = []
        for index in range (0,len(p_key_word),1): 
            if (p_key_word[index] != ""):
                #print(p_key_word)
                new_input_value.append(p_key_word[index])
        
        return new_input_value


    #def response_server(self, response):

        #self.print_papy("envoi serveur " + str(response))
