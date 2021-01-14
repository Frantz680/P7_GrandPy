/* Pharse test
Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?
Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.
Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?*/

//-----------------Variable Global-----------------

var verbe = ["suis", "es", "est", "sommes", "etes", "êtes", "fait", "passé", "ai", "indiquer", "avons", "avez", "ont", "avoir", "etre", "être", "indique", "indiques", "indiquons", "indiquez", "indiquent", "voir", "vois", "voit", "voyons", "voyez", "voient", "penser", "pense", "penses", "pensons", "pensez", "pensent", "pouvoir", "peux", "peut", "pouvons", "pouvez", "peuvent", "pourrais", "pourras", "pourra", "pourrons", "pourrez", "pourront", "trouver", "trouve", "trouves", "trouvons", "trouvez", "trouvent", "connaitre", "connaître", "connais", "connait", "connaît", "connaissons", "connaissez", "connaissent", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", ]
var pronom = ["d'", "je", "j'", "l'", "tu", "et", "de" ,"ta", "il", "elle", "on", "nous", "vous", "ils", "se", "elles", "me", "te", "le", "les", "lui", "leur", "qu'", "quoi", "qui", "que", "ou", "où", "ce", "cela", "s'", "un", "une", "-"]
var mot = ["grandpy", "grandma", "mamie", "papy", "hier", "avec", "soir", "plait", "plaît", "comment", "pendant", "au", "belle", "beau", "nuit", "soiree", "soire", "soirée", "soiré", "semaine", "merci", "salutations", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", "grandpy", ]
var ponctuation = [".", ",", "!", "?", ";", ":", " ", "'", "-"]
var alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z"]
var question_bot = ["Qu'elle adresse aimerais tu savoir ?", "Quel lieu veux tu connaitre ?", "Ou veux tu allez ?"]
var gronder = ["On dit pas des choses comme ça Spirou !", "Je t'ai pas a pris a parler ainsi Spirou !", "Attend que ton père rentre !"]
var mot_interdit = ["con", "connard", "salope", "salope", "pd"]
var response_negative_bot = ["Je suis sourd, j'ai pas compris", "Pardon, mon petit j'ai pas compris", "Peut tu repeter stp"]
var mini_input_value = ""
var input_value_important_word = ""
var new_input_value = []
var tbl_mini_input_value = []

//---------On additionne tous les tableaux ensembles pour le parse ---------

var remove_word = verbe.concat(pronom, mot, ponctuation, alphabet);


//-----------------Differentes Fonctions-----------------

//---------Creation d'element HTML---------

function print_user() {
    let para = document.createElement("P");
    para.className = "user"
    para.innerHTML = '<img src="/static/image/spirou-chat.jpg" alt="Avatar_user"></img>' + input.value;
    document.getElementById("chat2").appendChild(para);
}

function print_papy(reponse) {
    let bot = document.createElement("P");
    bot.className = "papy"
    bot.innerHTML ='<img src="/static/image/Grand-Papy_Spirou.png" alt="Avatar_papy"></img>' + reponse;
    bot.id = "id_papy"
    document.getElementById("chat2").appendChild(bot)

}

function print_maman(reponse_maman) {
    let bot_maman = document.createElement("P");
    bot_maman.className = "bot_maman"
    bot_maman.innerHTML ='<img src="/static/image/maman_Spirou.png" alt="Avatar_maman"></img>' + reponse_maman;
    document.getElementById("chat2").appendChild(bot_maman);

}

//---------Parse---------

function parse_str_user() {
    if (input.value.length <= 2) {
        print_papy("Je n'arrive pas à comprendre");
        return true;
    }


    // on met toute les char en minuscule
    mini_input_value = input.value.toLowerCase();

    /*for (let index = 0; index < mot_interdit.length; index++) {

        if (mini_input_value.includes(mot_interdit[index])) {
            // if (mini_input_value == salutation_mini[index]){
            random = getRandomInt(0, gronder.length - 1);
            print_maman(gronder[random]);
            return true;
            }

        }*/
        
        // on remplace les ' par un espace 
        for (let index = 0; index < ponctuation.length; index++) {
            mini_input_value = mini_input_value.replaceAll(ponctuation[index], " ");
            
        }

        console.log(mini_input_value);
        // on créer un tableau avec notre chaine de caractere
        tbl_mini_input_value = mini_input_value.split(" ");
        console.log(tbl_mini_input_value);

        // On remplace(supprimer) tout les mots inutiles dans notre tableau et dans le tableaux des mots supprimers
        for (let index = 0; index < tbl_mini_input_value.length; index++) {
            for (let index_remove = 0; index_remove < remove_word.length; index_remove++) {
                if (tbl_mini_input_value[index] == remove_word[index_remove]) {
                    tbl_mini_input_value[index] = tbl_mini_input_value[index].replace(remove_word[index_remove], "");
                }
            }    
        }

        console.log("tbl_mini_input_value remove = ", tbl_mini_input_value)

        new_input_value = []
        for (let index = 0; index < tbl_mini_input_value.length; index++) {
            if (tbl_mini_input_value[index] != "") {
                new_input_value.push(tbl_mini_input_value[index]);
            }
        }
    
        console.log("new input value", new_input_value);

        if (parse_salutation()) {
            return true;
            
        }

        if (parse_localisation()) {
            return false;
        }

        random = getRandomInt(0, response_negative_bot.length);
        print_papy(response_negative_bot[random])
        return true;

}

function parse_salutation() {
    // si un mot de saluation est présent dans la pharse le bot salut

    for (let index = 0; index < salutation.length; index++) {

        if (mini_input_value.includes(salutation_mini[index])) {
            // if (mini_input_value == salutation_mini[index]){
            random = getRandomInt(0, salutation.length - 1);
            print_papy(salutation[random]);

            // si la string fait moins que 3 mot alors on return
            if (input_value_important_word.length < 3) {
                random = getRandomInt(0, question_bot.length - 1);
                print_papy(question_bot[random]);
                return true;
            }

        }


    }
    return false    
}


function parse_localisation() {
    console.log("parse_local")
    // les mots suivant ont les envoient au serveur 
    for (let index = 0; index < new_input_value.length; index++) {
        for (let index_salutation = 0; index_salutation < salutation.length; index_salutation++) {

            if(new_input_value[index] == salutation[index_salutation]){
                key_word[index] = new_input_value[index].replace(salutation[index_salutation], "")
                console.log("key_word", key_word)
                print_papy("envoi serveur " + String(key_word[index.length]))
                console.log("Print papy passer")
                return true;
            }
        
        }
    
    }
    return false;
}   