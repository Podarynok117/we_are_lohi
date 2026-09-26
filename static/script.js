let socket=io();
let input = document.getElementById("message");
let button = document.getElementById("send");
let messages = document.getElementById("messages");
function showMwssage(message) {
    console.log(message);
    let p=document.createElement("p");
    p.textContent=message; 
    messages.appendChild(p);
    
}
socket.emit("message", "прювет");
socket.on("message", showMwssage);
button.onclick = function() {
    socket.emit("message", input.value);
    input.value = "";
    
}
input.onkeydown = function(){
    if (event.key=="Enter") {
        socket.emit("message", input.value);
        input.value = "";
        
    }
}
