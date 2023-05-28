// Here You can type your custom JavaScript...
//just paste in web telegram console
pastCode = "";
// Function to process the last message
function processLastMessage(code) {

  // Send the code to your server
  fetch(`http://localhost/?code=${code}`)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not OK');
      }
      return response.json();
    })
    .then(data => {
      // Process the response data from the server
      console.log(data);
    })
    .catch(error => {
      // Handle the error
      console.error('Error:', error);
    });
}

// Function to handle new messages
function handleNewMessage(event) {
    const message = event.currentTarget;//event.target;
    /*let l = message.getElementsByClassName("message-content-wrapper can-select-text");
    let lastPosi = l[l.length - 1];
    const code = lastPosi.querySelector("div").getElementsByClassName("content-inner")[0].querySelector("code").textContent;
*/
    let l = message.getElementsByClassName("message-content-wrapper can-select-text");
    let lastPosi = l[l.length-1];let codeEle = lastPosi.querySelector("div").getElementsByClassName("content-inner")[0];
    if (lastPosi.querySelector("code") == null){
    code = codeEle.querySelectorAll("div")[1].firstChild
}else{
    code = lastPosi.querySelector("code").textContent;
}
if (code.length == 8){
    //console.log(code);
if (pastCode != code){
    pastCode = code;
    processLastMessage(code);
    }    
    }
    
}
// Listen for new message events
document.addEventListener("DOMNodeInserted", handleNewMessage);
