import random


#-----------------Variable Global-----------------


salutation = ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
verbe = ["suis", "as", "es", "est", "sommes", "etes", "êtes", "fait", "passé", "ai", "indiquer", "avons", "avez", "ont", "avoir", "etre", "être", "indique", "indiques", "indiquons", "indiquez", "indiquent", "voir", "vois", "voit", "voyons", "voyez", "voient", "penser", "pense", "penses", "pensons", "pensez", "pensent", "pouvoir", "peux", "peut", "pouvons", "pouvez", "peuvent", "pourrais", "pourras", "pourra", "pourrons", "pourrez", "pourront", "trouver", "trouve", "trouves", "trouvons", "trouvez", "trouvent", "connaitre", "connaître", "connais", "connait", "connaît", "connaissons", "connaissez", "connaissent", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy",]
pronom = ["d'", "je", "j'", "l'", "la", "à", "tu", "et", "de", "ta", "il", "elle", "on", "nous", "vous", "ils", "se", "elles", "me", "te", "le", "les", "lui", "leur", "qu'", "quoi", "qui", "que", "ou", "où", "ce", "cela", "s'", "un", "une", "-"]
mot = ["grandpy", "grandma", "mamie", "espère", "adresse", "avance", "papy", "hier", "avec", "soir", "plait", "plaît", "comment", "pendant", "au", "belle", "beau", "nuit", "soiree", "soire", "soirée", "soiré", "semaine", "merci", "salutations", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy",]
ponctuation = [".", ",", "!", "?", ";", ":", " ", "'", "-"]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
question_bot = ["Qu'elle adresse aimerais tu savoir ?", "Quel lieu veux tu connaitre ?", "Ou veux tu allez ?"]
gronder = ["On dit pas des choses comme ça Spirou !", "Je t'ai pas a pris a parler ainsi Spirou !", "Attend que ton père rentre !"]
mot_interdit = ["con", "connard", "salope", "salope", "pd"]
response_negative_bot = ["Je suis sourd, j'ai pas compris", "Pardon, mon petit j'ai pas compris", "Peut tu repeter stp"]
mini_input_value = ""
input_value_important_word = ""
new_input_value = []
tbl_mini_input_value = []
key_word = []
salutation_mini = []
random = random.choice(salutation)

#---------On additionne tous les tableaux ensembles pour le parse ---------

tbl_remove_word = verbe + pronom + mot + ponctuation + alphabet

class Chat_bot:

    def __init__(self):
        pass
    


    def parse_str_user(self):

        #papy ne comprend pas en dessous de deux mots
        if (input.value.length <= 2):
            
            self.print_papy("Je n'arrive pas à comprendre")
            return True
    

        input.value = self.transform_mini(input.value)
        #console.log("input.value", input.value)

        input.value = self.remove_ponctuation(input.value)
        #console.log("input.value2", input.value)

        key_word = self.create_tableau(input.value)
        #console.log("key_word", key_word)

        key_word = self.remove_word(key_word, tbl_remove_word)
        #console.log("key_word2", key_word)

        #console.log("new input value", new_input_value)

        if self.parse_mot_interdit(key_word):
            random = random.choice(gronder)
            print(gronder[random])
            return True
        


        if self.parse_salutation(key_word):

            random = random.choice(salutation)
            self.print_papy(salutation[random])
        

        key_word = self.remove_word(key_word, salutation_mini)

        self.print_papy("envoi serveur " + str(key_word))
        #request_ajax(str(key_word), response_server)

        """random = getRandomInt(0, response_negative_bot.length)
        print_papy(response_negative_bot[random])
        return true"""

    def parse_salutation(self, param):
    # si un mot de saluation est présent dans la pharse le bot salut

        for index in range (0,len(salutation_mini),1):
            for index_param in range (0,len(param), 1):
                if salutation_mini[index] == param[index_param]:
                    # if (new_input_value == salutation_mini[index])
                    return True
        
    """for (let index = 0; index < mot_interdit.length; index++) {

        if (mini_input_value.includes(mot_interdit[index])) {
            // if (mini_input_value == salutation_mini[index]){
            random = getRandomInt(0, gronder.length - 1);
            print_maman(gronder[random]);
            return true;
            }

    """

    def parse_mot_interdit(self, param):
    # si un mot interdit est présent dans la pharse la maman repond

        for index in range (0,len(mot_interdit),1):
            for index_param in range (0,len(param), 1):

                if mot_interdit[index] == param[index_param]:
                    #if (new_input_value == salutation_mini[index])
                    return True
        
    def transform_mini(self, param):
    # on met toute les char en minuscule
        return param.toLowerCase()

    def remove_ponctuation(self, param):
    # on remplace la ponctuation par un espace 

        for index in range (0,len(ponctuation),1):

            param = param.replaceAll(ponctuation[index], " ")
    
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
                
    
        # On ajoute les mots dans un nouveau tableau mais pas les "" 
        new_input_value = []
        for index in range (0,len(p_key_word),1): 
            if (p_key_word[index] != ""):
                new_input_value.insert(p_key_word[index])
        
    
        return new_input_value


    def response_server(self, response):

        self.print_papy("envoi serveur " + str(response))

    


