const socket = require("socket.io");
const io = socket(server);

$(document).ready(function() {
	// Connect to the Socket.IO server.
	var socket = io;

	// Event handler for new connections
	socket.on("connect", function() {
		socket.emit("my_event", {data: "I'm connected!"});
	});

	// Event handler for server sent data: adding it to a log for my sanity
	socket.on("my_response", function(msg, cb) {
		$('#log').append('AHHH');
		// $('#log').append('<br>' + $('<div/>').text('Received #' msg.count + ': ' + msg.data).html());
	});
});
