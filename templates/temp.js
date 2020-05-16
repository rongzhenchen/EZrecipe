
async function getrecipe(id){
url = `https://api.spoonacular.com/recipes/${id}/information?includeNutrition=0&apiKey=5a634bdaaa544ee18579ccbfcdfb92f1`;
 m = document.getElementById("modtex").value;
 console.log("this is: "+m);
 try{
     let response = await fetch(url);
     let result = await response.json();
     console.log("this is the id: "+id);
     console.log(result);
   //   for( ingredient of result.extendedIngredients){
      //data = {"id": ingredient.id,
      //"aisle": ingredient.aisle,
      //"image": ingredient.image,
      //"name": ingredient.name,
      //"amount": ingredient.amount,
     // "unit": ingredient.unit
    // }
   await post(result);
      
     // }
      }

     
  catch(e){
      console.log(e);

}

removeElement(id);
}
async function post(data){
  url =server+"/jesusislord";
  try{
     let response = await fetch(
       url, 
       {
            method: 'POST',
            body: JSON.stringify(data),//convert data to JSON string
          headers: { 'Content-Type':'application/json'}// JSON data
       },
     );//1. Send http request and get response
     
     let result = await response.text();//2. Get message from response
     console.log(result);//3. Do something with the message
   
   }catch(error){
     console.log(error);//catch and log any errors
   }
}

function removeElement(elementId) {
    // Removes an element from the document
    var element = document.getElementById(elementId);
    element.parentNode.removeChild(element);
}
//modal logic----------------------------------------------------------


// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close1")[0];

function gomodal(id){
  var m = document.getElementById("submod");
  m.innerHTML=`<button class="btn btn-primary" onclick="getrecipe(${id})">submit</button>`  
  modal.style.display = "block";
}
// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}