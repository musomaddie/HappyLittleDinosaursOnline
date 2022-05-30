// Probably going to get messed up because this is now a new connection. Do I even need the original one?
const socket = io();

const start_game_form = document.getElementById("form_start_new_game");

start_game_form.addEventListener("submit", function() {
    // When the waiting room start button is clicked this client should let the server know to start a room.
    socket.emit("start_waiting_room");
});