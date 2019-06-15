window.onload = function () {
new Vue({
el: '#app',

data: {

//Fragen-Variablen

question:'placeholder',
answerA:'placeholder',
answerB:'placeholder',
answerC:'placeholder',
answerD: 'placeholder',

//Test Datensatz (Fragen)

zaehler:-1,
frage1:'Wer bin ich?',
frage2: 'Wann bin ich?',

//Datensatz zum Schluss
daten:[],

anzahlInputs:0,

},

created: function(){
    this.fragen();
    this.save();

},

mounted: function(){

},

methods: {
    save() {
        var answers = [];
        var array = document.getElementsByTagName("input")
        for(var i = 0; i < array.length ; i++) {
            var x = array[i].checked;
        
            if (x == true) {
                answers.push(i + 1);
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
document.getElementById("answers").innerHTML = "";
axios
.get("test.json")
.then(response => {
    console.log('JSON Datei: ', response);
    console.log('zaehler: ', this.zaehler);
    var fragen = response.data.data;
    console.log('Alle Fragen:  ', fragen);
    var laenge =fragen.length;
    console.log('Array Länge: ', laenge);

    if (this.zaehler < laenge) {

        this.question = fragen[this.zaehler].name;
        
    for(var i = 0; i < fragen[this.zaehler].antworten.length; i++) {
        var answer = fragen[this.zaehler].antworten[i];
        console.log("Antwort: ", answer);
        var text = document.createElement("h1");
        text.innerText = answer;
        document.getElementById("answers").appendChild(text);

        var checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        document.getElementById("answers").appendChild(checkbox);
    }
        }
        else {
            // Daten los schicken!
            axios.post('http://localhost:3030/api/new/post', 
    this.name, // the data to post
    { headers: {
      'Content-type': 'application/x-www-form-urlencoded',
      }
    }).then(response => {

    }
    )}
})


    }
    },

computed: {

},


})
}