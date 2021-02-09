

//-----------------Variable Global-----------------

var salutation = ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
var scold = ["On dit pas des choses comme ça Spirou !", "Je t'ai pas a pris a parler ainsi Spirou !", "Attend que ton père rentre !"]
var question_bot = ["Qu'elle adresse aimerais tu savoir ?", "Quel lieu veux tu connaitre ?", "Ou veux tu allez ?"]
var salutation_mini = []
var random = getRandomInt(0, salutation.length - 1)
var input = ""
var last_scrollheight = 0
var url_maps = "https://maps.googleapis.com/maps/api/js?"
var spinner = document.getElementById("spinner")

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
            //print_papy("Un instant stp je te repond de suite");
            request_ajax("str_user", input.value, callback_json);
            //Envoie de la requete
            spinner.style.display = "block";

        }
    });
    
}
  
//-----------------API JS Google Maps-----------------

function api_maps(location, adresse, key){
    let script = document.createElement("script");
    script.src = url_maps + "key=" + key + "&callback=initmaps";
    script.defer = true;
    console.log(location)
    window.initmaps = function() {
        const map = new google.maps.Map(document.getElementById("maps"), {
            center: location,
            zoom: 15,
            mapTypeId: "satellite",
        });
        new google.maps.Marker({
            position: location,
            map,
            title: adresse,
          });
        map.setTilt(45);
    }
    document.getElementById("maps").appendChild(script);
}

//-----------------Fonction Callback-----------------

function callback_json(p_response) {
    spinner.style.display = "none"
    response_json = JSON.parse(p_response);
    console.log(response_json);
    console.log(response_json.salutation);

    if (response_json.salutation == "True") {
        random = getRandomInt(0, salutation.length);
        print_papy(salutation[random]);

        if (response_json.api == "False"){
            random = getRandomInt(0, question_bot.length );
            print_papy(question_bot[random]);
        }
    }

    if (response_json.insult == "True") {
        random = getRandomInt(0, scold.length);
        print_maman(scold[random]);
    }

    if (response_json.api == "True") {
        /*console.log("response json: ", response_json)
        console.log("response_json_wiki: ", response_json.wiki)
        console.log(response_json.adresse)
        console.log(response_json.location)*/
        print_papy("Voici l'adresse que j'ai trouvez sur ce lieu :\n" + response_json.adresse);
        print_papy("Je vais te racontez ma petite histoire sur ce lieu\n" + response_json.wiki);
        api_maps(response_json.location, response_json.adresse, response_json.key_api);
    }
   
}

//-----------------Function AJAX-----------------

function request_ajax(name_resquest, param_send, callback) {
    /*
    La fonction ajax sert à échanger des données avec un serveur.
    name_resquest = le nom de la requete
    param_send = la valeur qu'on envoi au serveur
    callback = on rappel la fonction quand on recoit la reponse
    */


    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        //Fonction assynchrone
        if (this.readyState == 4 && this.status == 200) {
            callback(this.response)
        } 
        else if (this.readyState == 4 && this.status == 500) {
            print_papy("Désole je n'ai pas d'histoire te raconter");
        }
        
    };

    xhttp.open("POST", name_resquest, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("param_send=" + param_send);
}

setInterval(function() {
    var scroll = document.getElementById("chat2");
    if (scroll.scrollHeight != last_scrollheight) {
        last_scrollheight = scroll.scrollHeight;
        scroll.scrollTop = scroll.scrollHeight;
    }
}, 200);


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