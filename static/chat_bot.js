//-----------------Variable Global-----------------

var mini_input_value = ""
var split_input_value = ""
var new_str = []

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

function parse_str_user() {
    if (input.value.length <= 2) {
        print_papy("Je n'arrive pas à comprendre");
        return true;
    }

    mini_input_value = input.value.toLowerCase();

    /*for (let index = 0; index < mot_interdit.length; index++) {

        if (mini_input_value.includes(mot_interdit[index])) {
            // if (mini_input_value == salutation_mini[index]){
            random = getRandomInt(0, gronder.length - 1);
            print_maman(gronder[random]);
            return true;
            }

        }*/

        // On remplace tout les mots inutiles
        for (let index = 0; index < stop_word.length; index++) {
            mini_input_value = mini_input_value.replace(stop_word[index], "");
        }

        // On créer un tableau 
        split_input_value = mini_input_value.split(" ");

        console.log(split_input_value);

        new_str = []
        for (let index = 0; index < split_input_value.length; index++) {
            if (split_input_value[index] != "") {
                new_str.push(split_input_value[index]);
            }
        }
    
        console.log(new_str);

        if (parse_salutation()) {
            return true;
            
        }

        if (parse_localisation()) {
            return false;
        }

        random = getRandomInt(0, response_negative_bot.length - 1);
        print_papy(response_negative_bot)
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
            if (split_input_value.length < 3) {
                random = getRandomInt(0, question_bot.length - 1);
                print_papy(question_bot[random]);
                return true;
            }

        }


    }
    return false    
}


function parse_localisation() {
            
// si un mot de localisation est présent
let index_split = 0;   
    for (let index = 0; index < key_word.length; index++) {
        if (mini_input_value.includes(key_word[index])) {

            // si un mot de designation est présent
            for (index_split = 0; index_split < split_input_value.length; index_split++) {
                for (let index = 0; index < key_word_kurz.length; index++) {

                    if (split_input_value[index_split] == key_word_kurz[index]) {

                        print_papy("envoi serveur " + String(split_input_value[index_split + 1]))
                        return true;
                    }

                }
            }
            console.log(new_str[index_split])
            console.log(key_word)
            if (new_str[index_split] == key_word[index_split]) {
                console.log("ok")
                print_papy("envoi serveur " + String(new_str[index_split + 1]))
                console.log(new_str[index_split])
                return true;
            }
            
        }

    }
    return false;
}