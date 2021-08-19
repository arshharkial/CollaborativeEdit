const sio = io();

sio.on('connect', () => {
    sio.send("User has connected!!")
    console.log('connected');
});

sio.on("UpdateText", (message) => {
    document.getElementById("TextArea").value = message;
    console.log("Message Received");
});

function myFunction(){
    sio.emit("TextUpdated", document.getElementById("TextArea").value);
    console.log("Button Clicked");
}

function emitToAll(){
    sio.emit("UpdateAll", document.getElementById("TextArea").value);
}


sio.on('disconnect', () => {
    console.log('disconnected');
});
