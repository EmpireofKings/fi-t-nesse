socket = io.connect('http://' + document.domain + ':' + location.port);
socket.on('connect', function() {
    socket.emit('client_connected', {data: 'New client!'});
});


socket.on('alert', function (data) {
    alert('Alert Message!! ' + data);
});


function alert_button() {
    socket.emit('alert_button', {"x":"0","y":"0"})
}

function submitSignup() {
  var formData = JSON.stringify($("#myForm").serializeArray());
  $.post("http://localhost:5000/register", formData);
}
