var text_box = '<div class="card-panel right" style="width: 75%; position: relative">' +
        '<div style="position: absolute; top: 0; left:3px; font-weight: bolder" class="title">{sender}</div>' +
        '{message}' +
        '<div class="card-footer right" style="position: relative;top: 12px">\n' +
          '<small class="title text-muted">{created}</small>\n' +
    '            </div>'+
        '</div>';

function scrolltoend() {
    $('#board').stop().animate({
        scrollTop: $('#board')[0].scrollHeight
    }, 5000);//maybe scroll the content every 5 seconds
}

function send(sender, receiver, message) {
    $.post('/chats/api/messages/', '{"sender": "'+ sender +'", "receiver": "'+ receiver +'","message": "'+ message +'" }', function (data) {
        console.log(data,sender,receiver);
        var box = text_box.replace('{sender}', "You");
        box = box.replace('{message}', message);
        box =box.replace('{created}',moment().fromNow());
        $('#board').append(box);
        scrolltoend();
    }).catch(function (error) {
        console.log("Errors: ",error)
    })
}

function receive() {
    $.get('/chats/api/messages/'+ sender_id + '/' + receiver_id+'/', function (data) {
        console.log('receiving:',data, sender_id,receiver_id);
        if (data.length !== 0)
        {
            for(var i=0;i<data.length;i++) {
                console.log(data[i]);
                var box = text_box.replace('{sender}', data[i].sender);
                box = box.replace('{message}', data[i].message);
                box =box.replace('{created}',moment(data[i].created).fromNow());
                box = box.replace('right', 'left blue lighten-5');
                $('#board').append(box);
               scrolltoend();
            }
        }
    });
}

function register(username, password) {
    $.post('/api/users', '{"username": "'+ username +'", "password": "'+ password +'"}',
        function (data) {
        console.log(data);
        window.location = '/';
        }).fail(function (response) {
            $('#id_username').addClass('invalid');
        })
}