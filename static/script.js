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

            if (parse_str_user()) {
                // si la fonction parse nous retourne un True on sort de la fonction event
                return;

            }
            print_papy("Un instant stp je te repond de suite");

            

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

    setInterval(function() {
        var scroll = document.getElementById("chat2");
        if (scroll.scrollHeight != last_scrollheight) {
            last_scrollheight = scroll.scrollHeight;
            scroll.scrollTop = scroll.scrollHeight;
        }
    }, 200);
}

