/* Pharse test
Salut grandpy! Comment s'est passé ta soirée avec Grandma hier soir? Au fait, pendant que j'y pense, pourrais-tu m'indiquer où se trouve le musée d'art et d'histoire de Fribourg, s'il te plaît?
Bonsoir Grandpy, j'espère que tu as passé une belle semaine. Est-ce que tu pourrais m'indiquer l'adresse de la tour eiffel? Merci d'avance et salutations à Mamie.
Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?*/

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

