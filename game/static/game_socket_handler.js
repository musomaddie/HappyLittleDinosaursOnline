var socket = io();
$(document).ready(function() {
	socket = io.connect("http://" + document.domain + ":" + location.port + "/chat");
	socket.on("connect", function() {
		console.log("joined");
		socket.emit("joined", {});
	});
});

socket.on("my_response", function(msg, cb) {
	console.log("I have receieved a message");
	$("#log").append("<br>" + msg.data).html();
});