var socket = io();
$(document).ready(function() {
	// TODO: update the connection name.
	socket = io.connect("http://" + document.domain + ":" + location.port + "/aaaaaaaaaaaaaaaaaa");
	socket.on("connect", function() {
		console.log("joined");
		socket.emit("joined", {});
	});
});

socket.on("my_response", function(msg, cb) {
	console.log("I have receieved a message");
	$("#log").append("<br>" + msg.data).html();
});

socket.on("disconnect", function() {
	console.log("disconnected");
	socket.emit("lost");
});