const socket = io()

// If I have the ID from the server on the page I should be alright.
$(document).ready(function() {
    console.log("connecting")
    socket.on("connect", function() {
        socket.emit("load_waiting_room");
    });

    // Receive a response containing the room ID.
    socket.on("retrive_room_id", function(msg) {
        console.log("displaying id");
        const id_placement = document.getElementById("game_room_id");
        // TODO: handle case where there's no ID.
        id_placement.innerText = msg["id"];
    });
});