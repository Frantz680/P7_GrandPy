//-----------------Variable Global-----------------

var salutation = ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
var salutation_mini = []
var stop_word = ["d'", "!", "j'", "je", "j'ai", "est-ce", "connais", "tu", "il", "grandpy"]
var key_word = ["adresse", "localisation", "position", "lieu", "l'adresse"]
var key_word_kurz = ["a", "à", "de", "sur", "la"]
var question_bot = ["Qu'elle adresse aimerais tu savoir ?", "Quel lieu veux tu connaitre ?", "Ou veux tu allez ?"]
var response_negative_bot = ["Je suis sourd, j'ai pas compris", "Pardon, mon petit j'ai pas compris", "Peut tu repeter stp"]
var gronder = ["On dit pas des choses comme ça Spirou !", "Je t'ai apris a parler ainsi Spirou !", "Attend que ton père rentre !"]
var mot_interdit = ["con", "connard", "salope", "salope", "pd"]
var random = getRandomInt(0, salutation.length - 1)
var input = ""

for (let index = 0; index < salutation.length; index++) {
    salutation_mini[index] = salutation[index].toLowerCase();

}


//-----------------Differentes Fonctions-----------------

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}

window.onload = function () {
    document.getElementById("str_user").setAttribute("value", salutation[random]);

    input = document.getElementById("str_user");

    input.addEventListener("keyup", function (event) {
        if (event.keyCode === 13) {
            print_user();

            if (parse_str_user()) {
                // si la fonction parse nous retourne un True on sort de la fonction event
                return;

            }
            print_papy("Un instant stp je te repond de suite");

            var scroll = document.getElementById("chat2");
            scroll.scrollTop = scroll.scrollHeight;

            //Envoie de la requete
            spinner.style.display = "block";
            request_ajax(response_request_string_user)

        }

    });

    function response_request_string_user() {

        spinner.style.display = "none";
        console.log(input.value);
    }


    //-----------------Function AJAX-----------------

    function request_ajax(callback) {


        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function () {
            //Fonction assynchrone
            if (this.readyState == 4 && this.status == 200) {
                //var rep_json = JSON.parse(this.response);
                callback()
            }
        };

        xhttp.open("POST", "/reponse_user", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("fname=Henry&lname=Ford");
    }

}

function parse_str_user() {
    if (input.value.length <= 2) {
        print_papy("Je n'arrive pas à comprendre");
        return true;
    }

    var mini_input_value = input.value.toLowerCase();

    for (let index = 0; index < mot_interdit.length; index++) {

        if (mini_input_value.includes(mot_interdit[index])) {
            // if (mini_input_value == salutation_mini[index]){
            random = getRandomInt(0, gronder.length - 1);
            print_maman(gronder[random]);
            return true;
            }

        }



        for (let index = 0; index < stop_word.length; index++) {
            mini_input_value = mini_input_value.replace(stop_word[index], "");
        }
        var split_input_value = mini_input_value.split(" ");

        console.log(split_input_value);

        // si un mot de saluation est présent dans la pharse le bot salut

        for (let index = 0; index < salutation.length; index++) {

            if (mini_input_value.includes(salutation_mini[index])) {
                // if (mini_input_value == salutation_mini[index]){
                random = getRandomInt(0, salutation.length - 1);
                print_papy(salutation[random]);

                // si la string fait moins que 3 mot alors on return
                if (split_input_value.length < 3) {
                    random = getRandomInt(0, question_bot.length - 1);
                    print_papy(question_bot[random]);
                    return true;
                }

            }


        }

        // si un mot de localisation est présent

        for (let index = 0; index < key_word.length; index++) {
            if (mini_input_value.includes(key_word[index])) {

                // si un mot de designation est présent
                for (let index_split = 0; index_split < split_input_value.length; index_split++) {
                    for (let index = 0; index < key_word_kurz.length; index++) {

                        if (split_input_value[index_split] == key_word_kurz[index]) {

                            print_papy("envoi serveur " + String(split_input_value[index_split + 1]))
                            return false;
                        }

                    }
                }

                if (split_input_value[index] == key_word[index]) {

                    print_papy("envoi serveur " + String(split_input_value[index_split + 1]))
                    return false;
                }

            }

        }

        random = getRandomInt(0, response_negative_bot.length - 1);
        print_papy(response_negative_bot)
        return true;

}

 

function print_user() {
    let para = document.createElement("P");
    para.className = "user"
    para.innerHTML = input.value;
    document.getElementById("chat2").appendChild(para);
}

function print_papy(reponse) {
    let img = document.createElement("img")
    let bot = document.createElement("P");
    bot.className = "papy"
    bot.innerHTML = reponse;
    img.src = "/static/image/Grand-Papy_Spirou.png"
    document.getElementById("chat2").appendChild(img)
    document.getElementById("chat2").appendChild(bot)
}

function print_maman(reponse_maman) {
    let bot_maman = document.createElement("P");
    bot_maman.className = "bot_maman"
    bot_maman.innerHTML = reponse_maman;
    document.getElementById("chat2").appendChild(bot_maman);

}