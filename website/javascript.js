window.onload = function () {
new Vue({
el: '#app',

data: {

//Fragen-Variablen

question:'placeholder',

zaehler:-1,

//Datensatz zum Schluss
daten:[],

},

created: function(){
    this.fragen();
    this.save();
    this.alpaka_button();

},

mounted: function(){

},

methods: {
    alpaka_button () {
        var element = document.getElementById("Alpaka_Animation");
        element.classList.toggle("rotate-active");
    },
    save() {
        var answers = [];
        var array = document.getElementsByTagName("input")
        for(var i = 0; i < array.length ; i++) {
            var x = array[i].checked;
        
            if (x == true) {
                answers.push(i);
            }
            console.log("array Länge", x);
            console.log("answer arrray", answers);
        }
        if (answers.length > 0) {
        this.daten.push(answers);
        }
        console.log("Daten:", this.daten);
    },
    fragen (){
this.zaehler = this.zaehler + 1; 
this.save();    
document.getElementById("Antworten").innerHTML = "";
var url = "http://127.0.0.1:5000/fragebogen/";
axios
.get(url)
.then(response => {
    console.log('JSON Datei: ', response);
    console.log('zaehler: ', this.zaehler);
    var fragen = response.data.data;
    console.log('Alle Fragen:  ', fragen);
    var laenge =fragen.length;
    console.log('Array Länge: ', laenge);

    if (this.zaehler < laenge) {

        this.question = fragen[this.zaehler].frage;
        
    for(var i = 0; i < fragen[this.zaehler].antworten.length; i++) {
        var answer = fragen[this.zaehler].antworten[i];
        console.log("Antwort: ", answer);

        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        document.getElementById("Antworten").appendChild(checkbox);
        
        var text = document.createElement("a");
        text.classList.add("a");
        text.innerText = answer;
       var umbruch =  document.createElement("br");
        text.appendChild(umbruch);

        document.getElementById("Antworten").appendChild(text);


    }
        }
        else {
            this.question = "Auswertung!";
            // Daten los schicken!
            axios.post(url+ "/antworten/",    
    this.daten, // the data to post
    { headers: {
      'Content-type': 'text/plain',
      }
    }).then(response => {
        var endText = document.createElement("a");
        endText.classList.add("a");
        document.getElementById("Antworten").appendChild(endText);
        endText.innerText = response.data; // über response Text von der Verarbeitung abgreifen
    }
    )}
})


    }
    },

computed: {

},


})
}
