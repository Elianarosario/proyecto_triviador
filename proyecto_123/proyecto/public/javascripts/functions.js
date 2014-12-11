var socket = io.connect('http://localhost:3000');
mysql = require('mysql');

//al actualizar la página eliminamos la sesión del usuario de sessionStorage
$(document).ready(function()
{
    manageSessions.unset("login");
    var connection = mysql.createConnection({
        host: 'localhost',
        user: 'trivial_sem',
        password: 'trivial_sem',
        database: 'trivial_sem'
    });

    connection.connect();

    var query = connection.query('SELECT id, nombre_partida, categoria FROM principal_partidas', function(error, result){
        if(error){
            throw error;
        }else{
            var resultado = result;
            console.log(resultado.length);
            for(var i = 0; i < resultado.length; i++)
            {
                $("#salas").append("<a href='" + resultado[i].id + " class='list-group-item'> <span class='badge' style='background:#2dcc70'> 1</span>" + resultado [i].nombre_partida + " <a/>");
            }
        }
    });

    connection.end();
});

//función para mantener el scroll siempre al final del div donde se muestran los mensajes
//con una pequeña animación
function animateScroll()
{
    var container = $('#containerMessages');
    container.animate({"scrollTop": $('#containerMessages')[0].scrollHeight}, "slow");
}

//función anónima donde vamos añadiendo toda la funcionalidad del chat
$(function()
{
    //llamamos a la función que mantiene el scroll al fondo
    animateScroll();
    //si el usuario no ha iniciado sesión prevenimos que pueda acceder
    //showModal("Formulario de inicio de sesión",renderForm());
    //al poner el foco en el campo de texto del mensaje o pulsar el botón de enviar
    $("#containerSendMessages, #containerSendMessages input").on("focus click", function(e)
    {
        e.preventDefault();
    });

    //al pulsar en el botón de Entrar 
    $("#create").on("click", function(e)
    {
        e.preventDefault();
        manageSessions.set("login", $("#name_sala").val());
        socket.emit("loginUser", manageSessions.get("login"));
        animateScroll();
        $("#title").text("Bienvenido a la sala " + $("#name_sala").val());
        
        //Insert a info create sal
        var connection = mysql.createConnection({
           host: 'localhost',
           user: 'trivial_sem',
           password: 'trivial_sem',
           database: 'trivial_sem'
        });

        connection.connect();

        var query = connection.query('INSERT INTO principal_partidas(nombre_partida, categoria) VALUES(?, ?)', [$("#name_sala"), "categorias"], function(error, result){    
            if(error){
              throw error;
            }else{
              console.log(result);
            }
        });

        connection.end();
    });

    //al pulsar en el botón de Entrar 
    $("#close").on("click", function(e)
    {
        setTimeout(location.href="http://localhost:3000", 1000);
    });

    //si el usuario está en uso lanzamos el evento userInUse y mostramos el mensaje
    socket.on("userInUse", function()
    {
        //mostramos la ventana modal
        //$("#formModal").modal("show");
        //eliminamos la sesión que se ha creado relacionada al usuario
        manageSessions.unset("login");
        //ocultamos los mensajes de error de la modal
        $(".errorMsg").hide();
        //añadimos un nuevo mensaje de error y ponemos el foco en el campo de texto de la modal
        $(".name_sala").after("<div class='col-md-12 alert alert-danger errorMsg'>El usuario que intenta escoge está en uso.</div>").focus();
        return; 
    });

    //cuando se emite el evente refreshChat
    socket.on("refreshChat", function(action, message)
    {
        //simplemente mostramos el nuevo mensaje a los usuarios
        //si es una nueva conexión
        if(action == "conectado")
        {
            $("#chatMsgs").append("<p class='col-md-12 alert-info'>" + message + "</p>");
        }
        //si es una desconexión
        else if(action == "desconectado")
        {
            $("#chatMsgs").append("<p class='col-md-12 alert-danger'>" + message + "</p>");
        }
        //si es un nuevo mensaje 
        else if(action == "msg")
        {
            $("#chatMsgs").append("<p class='col-md-12 alert-warning'>" + message + "</p>");
        }
        //si el que ha conectado soy yo
        else if(action == "yo")
        {
            $("#chatMsgs").append("<p class='col-md-12 alert-success'>" + message + "</p>");
        }
        //llamamos a la función que mantiene el scroll al fondo
        animateScroll();
    });

    //actualizamos el sidebar que contiene los usuarios conectados cuando
    //alguno se conecta o desconecta, el parámetro son los usuarios online actualmente
    socket.on("updateSidebarUsers", function(usersOnline)
    {
        //limpiamos el sidebar donde almacenamos usuarios
        $("#chatUsers").html("");
        //si hay usuarios conectados, para evitar errores
        if(!isEmptyObject(usersOnline))
        {
            //recorremos el objeto y los mostramos en el sidebar, los datos
            //están almacenados con {clave : valor}
            $.each(usersOnline, function(key, val)
            {
                $("#chatUsers").append("<p class='col-md-12 alert-info'>" + key + "</p>");
            })
        }
    });

    //al pulsar el botón de enviar mensaje
    $('.sendMsg').on("click", function() 
    {
        //capturamos el valor del campo de texto donde se escriben los mensajes
        var message = $(".message").val();
        if(message.length > 2)
        {
            //emitimos el evento addNewMessage, el cuál simplemente mostrará
            //el mensaje escrito en el chat con nuestro nombre, el cuál 
            //permanece en la sesión del socket relacionado a mi conexión
            socket.emit("addNewMessage", message);
            //limpiamos el mensaje
            $(".message").val("");
        }
        else
        {
            showModal("Error formulario","<p class='alert alert-danger'>El mensaje debe ser de al menos dos carácteres.</p>", "true");
        }
        //llamamos a la función que mantiene el scroll al fondo
        animateScroll();
    });

});

//objeto para el manejo de sesiones
var manageSessions = {
    //obtenemos una sesión //getter
    get: function(key) {
        return sessionStorage.getItem(key);
    },
    //creamos una sesión //setter
    set: function(key, val) {
        return sessionStorage.setItem(key, val);
    },
    //limpiamos una sesión
    unset: function(key) {
        return sessionStorage.removeItem(key);
    }
};

//función que comprueba si un objeto está vacio, devuelve un boolean
function isEmptyObject(obj) 
{
    var name;
    for (name in obj) 
    {
        return false;
    }
    return true;
}