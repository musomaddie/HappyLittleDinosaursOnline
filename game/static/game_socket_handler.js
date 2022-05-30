const socket = io();
$(document).ready(function() {
	socket.on("connect", function() {
		console.log("joined");
	});
});

socket.on("my_response", function(msg, cb) {
	console.log("I have receieved a message " + msg);
	$("#log").append("<br>" + msg).html();
	// socket.emit("client_joined");
});

socket.on("disconnect", function() {
	console.log("disconnected");
	socket.emit("lost");
});