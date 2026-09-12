let socket=io();
let input = document.getElementById("message");
let button = document.getElementById("send");
let messages = document.getElementById("messages");
function showMwssage(message) {
    console.log(message);
}
socket.emit("message", "прювет");
socket.on("message", showMwssage);
button.onclick = function() {
    socket.emit("message", input.value);
    let p=document.createElement("p");
    p.textContent=input.value; 
    messages.appendChild(p);
    input.value = "";
}
