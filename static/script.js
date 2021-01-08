//-----------------Variable Global-----------------

var text = ["SALUT", "BONJOUR", "HEY", "COUCOU"]
var random = getRandomInt(0, text.length - 1)

//-----------------Differentes Fonctions-----------------

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}

window.onload = function () {
    document.getElementById("str_user").setAttribute("value", text[random]);


    var input = document.getElementById("str_user");

    input.addEventListener("keyup", function (event) {
        if (event.keyCode === 13) {
            //alert(string_user.length)
            if (input.value.length <= 3) {
                document.getElementById("erreur").innerHTML = "Tapez autre chose"
            }
            else {
                //Envoie de la requete
                spinner.style.display = "block";
                request_ajax(response_request_string_user)
            }
        }

    });

    function response_request_string_user() {

        spinner.style.display = "none";
        console.log(input.value);
    }



    function request_ajax(callback) {
    //Fonction assynchrone
    
        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function () {
            
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
