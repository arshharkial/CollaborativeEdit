const sio = io();

sio.on('connect', () => {
    sio.send("User has connected!!")
    console.log('connected');
});

sio.on("Start", (message) => {
    message.forEach((element, index, array) => {
        document.getElementById(element.TextArea).value = element.Data;
    });
})

sio.on("UpdateText", (message) => {
    textarea = message["TextArea"]
    document.getElementById(textarea).value = message["Data"];
    console.log("Message Received");
});

function myFunction(TextArea){
    sio.emit("TextUpdated", {"TextArea": TextArea, "Data": document.getElementById(TextArea).value});
    console.log("Button Clicked");
}

sio.on('disconnect', () => {
    console.log('disconnected');
});
