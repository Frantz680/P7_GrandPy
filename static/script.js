//-----------------Variable Global-----------------

var salutation = ["Salut", "Bonjour", "Hey", "Coucou", "Bonsoir", "Hello", "Hi"]
var scold = ["On ne dit pas des choses comme ça Spirou !", "Je t'ai pas appris à parler ainsi Spirou !", "Attends que ton père rentre !"]
var question_bot = ["Qu'elle adresse aimerais tu savoir ?", "Quel lieu veux-tu connaitre ?", "Veux-tu connaitre une histoire sur un lieu ?"]
var salutation_mini = []
var random = getRandomInt(0, salutation.length - 1)
var input = ""
var last_scrollheight = 0
var url_maps = "https://maps.googleapis.com/maps/api/js?"
var spinner = document.getElementById("spinner")

for (let index = 0; index < salutation.length; index++) {
    salutation_mini[index] = salutation[index].toLowerCase();
}


//-----------------Different Functions-----------------

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
        str_input_user = input.value
        
        if (event.keyCode == 13) {
            
            console.log(str_input_user)
            print_user();
            request_ajax("str_user", str_input_user, callback_json);
            //Send request
            spinner.style.display = "block";
        }

    });
    
}

//-----------------API JS Google Maps-----------------

function api_maps(location, address, key){
    /*
    This function allows me to create the site map.
    location: location of our research.
    adress: the address of the place.
    key: key api google.
    */

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
            title: address,
          });
        map.setTilt(45);
    }
    document.getElementById("maps").appendChild(script);
}

//-----------------Callback function-----------------

function callback_json(p_response) {
    /*
    Recall : A callback is a function passed as an argument to another function
    This technique allows a function to call another function
    A callback function can run after another function has finished.

    Once received the response from the server, then we call this function.
    This function allows us to know if the bot salutes it,
    if on display the card, if the mother intervenes.
    p_response : Server response value.
    */

    console.log(p_response)
    spinner.style.display = "none"
    response_json = JSON.parse(p_response);

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
        print_papy("Voici l'adresse que j'ai trouvez sur ce lieu :\n" + response_json.address);
        print_papy("Je vais te racontez ma petite histoire sur ce lieu\n" + response_json.wiki);
        api_maps(response_json.location, response_json.address, response_json.key_api);
    }
   
}

//-----------------Function AJAX-----------------

function request_ajax(name_resquest, param_send, callback) {
    /*
    The ajax function is used to exchange data with the server.
    name_resquest = the name of the request.
    param_send = the value we send to the server.
    callback = we call back the function when we receive the response.
    */

    var xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        //Asynchronous function
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
    /*
    This function allows me to avoid scroll 
    and does it automatically when there is a message.
    */

    var scroll = document.getElementById("chat2");
    if (scroll.scrollHeight != last_scrollheight) {
        last_scrollheight = scroll.scrollHeight;
        scroll.scrollTop = scroll.scrollHeight;
    }
}, 200);


//---------HTML element creation---------

function print_user() {
    /*
    We create an html element with an image of spirou
    and in this element there is the value
    of the user.
    */

    let para = document.createElement("P");
    para.className = "user";
    para.innerHTML = '<img src="/static/image/spirou-chat.jpg" alt="Avatar_user"></img>' + input.value;
    document.getElementById("chat2").appendChild(para);
}

function print_papy(response) {
    /*
    We create an html element with an image of papy spirou
    and in this element there is the answer of the grandpa.
    response = the value of grandpa's answer
    */

    let bot = document.createElement("P");
    bot.className = "papy";
    bot.innerHTML = '<img src="/static/image/Grand-Papy_Spirou.png" alt="Avatar_papy"></img>' + response;
    bot.id = "id_papy";
    document.getElementById("chat2").appendChild(bot);

}

function print_maman(response_maman) {
    /*
    We create an html element with an image of mother spirou
    and in this element there is the answer of the mother.
    response = the sentence to show that the mother is not happy
    */

    let bot_maman = document.createElement("P");
    bot_maman.className = "bot_maman";
    bot_maman.innerHTML = '<img src="/static/image/maman_spirou_chat.jpg" alt="Avatar_maman"></img>' + response_maman;
    document.getElementById("chat2").appendChild(bot_maman);

}