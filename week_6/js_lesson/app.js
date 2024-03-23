// Data Types:
/* //Multiline comment in Javascript
 1.String 
 2.integers/ numbers
 3.booleans 
 4.Arrays
 */

 let name = "Mike"
 let height = 50

 //oneclick events
 //element selesctor in js
 function submit(){
    var input = document.getElementById("inputField").value;
    var input = parseInt(input); //data type conversion
    var input = input + 1;
    //console.log(input)
 }
 
let adult = true; //boolean datatype
let fruits = ['kiwi','pineapple','apple',30,false]
let person = {
    Firstname: 'Ada' ,
    Lastname: 'Lovelace',
    age: 18,
    address: {
        country: 'Sudan',
        city: 'Juba',
        street: 'bani bani',
    },
    children: ['Kelly','Mary']
}
function saveItem(){
    var input = document.getElementById("inputField").value
    localStorage.setItem('inputItem', input);
    showWelcomeMessage(input)
}
function showWelcomeMessage(input){
    var messageElement= document.getElementById("showMessage")
    messageElement.textContent = "we have saved your input as "+ input;
}
var storedItem = localStorage.getItem('inputItem');
if(storedItem){
    showWelcomeMessage(storedItem)
}