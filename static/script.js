import Chat_bot from './chat_bot.py';

//-----------------Variable Global-----------------

var salutation = ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
var salutation_mini = []
var random = getRandomInt(0, salutation.length - 1)
var input = ""
var last_scrollheight = 0

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

        var scroll = document.getElementById("chat2");
        scroll.scrollTop = scroll.scrollHeight;

        if (event.keyCode === 13) {
            print_user();

            if (Chat_bot.parse_str_user()) {
                // si la fonction parse nous retourne un True on sort de la fonction event
                return;

            }
            print_papy("Un instant stp je te repond de suite");

            

            //Envoie de la requete
            spinner.style.display = "block";

        }
    });
    
}

//---------Creation d'element HTML---------

function print_user() {
    let para = document.createElement("P");
    para.className = "user";
    para.innerHTML = '<img src="/static/image/spirou-chat.jpg" alt="Avatar_user"></img>' + input.value;
    document.getElementById("chat2").appendChild(para);
}

function print_papy(reponse) {
    let bot = document.createElement("P");
    bot.className = "papy";
    bot.innerHTML = '<img src="/static/image/Grand-Papy_Spirou.png" alt="Avatar_papy"></img>' + reponse;
    bot.id = "id_papy";
    document.getElementById("chat2").appendChild(bot);

}

function print_maman(reponse_maman) {
    let bot_maman = document.createElement("P");
    bot_maman.className = "bot_maman";
    bot_maman.innerHTML = '<img src="/static/image/maman_Spirou.png" alt="Avatar_maman"></img>' + reponse_maman;
    document.getElementById("chat2").appendChild(bot_maman);

}