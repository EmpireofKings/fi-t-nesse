socket = io.connect('http://' + document.domain + ':' + location.port);
// socket.on('connect', function() {
//     socket.emit('client_connected', {data: 'New client!'});
// });

socket.on('alert', function (data) {
    alert('Your files have been successfully uploaded');
});


function alert_button() {
    socket.emit('alert_button', {"data":"processing"})
}