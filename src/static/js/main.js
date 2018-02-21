function printHelloWorld() {
	console.log("Hello World!");	
}

var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() { 
    console.log("The server is now connected to me");
    socket.emit('browserEvent', {data: 'Browser connected, so I emitted this data'});
});

socket.on('serverEvent', function(eventMsg) {
    console.log("The server had an event!");
    console.log(eventMsg);
});
