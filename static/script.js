//-----------------Variable Global-----------------

var salutation = ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
var salutation_mini = []
var random = getRandomInt(0, salutation.length - 1)
var input = ""
var last_scrollheight = 0
var url_maps = "https://maps.googleapis.com/maps/api/js"
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

/*function initmaps() {
    const map = new google.maps.Map(document.getElementById("maps"), {
      center: { lat: Math.random(), lng: Math.random() },
      zoom: 8,
      mapTypeId: "satellite",
    });
    map.setTilt(45);
}*/
  
function api_maps(location){
    let script = document.createElement("script");
    script.src = "https://maps.googleapis.com/maps/api/js?key=AIzaSyCVpEx_0aIjh-DX_6YhKStsYwGEGoK2lyQ&callback=initmaps";
    script.defer = true;
    console.log(location)
    window.initmaps = function() {
        const map = new google.maps.Map(document.getElementById("maps"), {
          center: location,
          zoom: 15,
          mapTypeId: "satellite",
        });
        map.setTilt(45);
    }
    document.getElementById("maps").appendChild(script);
}

function callback_json(p_response) {
    spinner.style.display = "none"
    response_json = JSON.parse(p_response)
    console.log(response_json.erreur)

    if (response_json.salutation == "True") {
        print_papy("Bonjour mon grand.")
    }

    if (response_json.erreur == "True") {
        print_papy("Je ne comprend pas ce que tu veux me demander.")
    }

    if (response_json.api == "True") {
        /*console.log("response json: ", response_json)
        console.log("response_json_wiki: ", response_json.wiki)
        console.log(response_json.adresse)
        console.log(response_json.location)*/
        print_papy("Voici l'adresse que j'ai trouvez sur ce lieu :\n" + response_json.adresse)
        print_papy("Je vais te racontez ma petite histoire sur ce lieu\n" + response_json.wiki)
        api_maps(response_json.location)
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

/*function print_maman(reponse_maman) {
    let bot_maman = document.createElement("P");
    bot_maman.className = "bot_maman";
    bot_maman.innerHTML = '<img src="/static/image/maman_Spirou.png" alt="Avatar_maman"></img>' + reponse_maman;
    document.getElementById("chat2").appendChild(bot_maman);

}*/