let socket=io();
let input = document.getElementById("message");
let button = document.getElementById("send");
function showMwssage(message) {
    console.log(message);
}
socket.emit("message", "прювет");
socket.on("message", showMwssage);
button.onclick = function() {
    socket.emit("message", input.value);
    input.value = "";
}
