function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min)) + min;
}

var text = ["SALUT", "BONJOUR", "HEY", "COUCOU"]
var random = getRandomInt(0, text.length - 1)
window.onload = function () {
    document.getElementById("valeur_reponse_user").setAttribute("value", text[random]);
}

function text_user() {
    var reponse_user = document.getElementById("valeur_reponse_user").value
    //alert(string_user.length)
    if (reponse_user.length <= 3) {
        document.getElementById("erreur").innerHTML = "Tapez autre chose"
    }
    else {
        //Envoie de la requete
        spinner.style.display = "block";

        var xhttp = new XMLHttpRequest();

        xhttp.onreadystatechange = function () {
            //Fonction assynchrone
            if (this.readyState == 4 && this.status == 200) {
                //var rep_json = JSON.parse(this.response);
                spinner.style.display = "none";
                console.log(reponse_user);
            }
        };

        xhttp.open("POST", "/reponse_user", true);
        xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhttp.send("fname=Henry&lname=Ford");
    }

}