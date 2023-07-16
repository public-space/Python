$('#send').click(function() {
    var note = $('#note').val();
    if(note.trim() != '') {
        $.ajax({
            url: '/add_note',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({'note': note}),
            success: function(response) {
                $('#note').val('');
                loadNotes();
            }
        });
    }
});

function loadNotes() {
    $.ajax({
        url: '/get_notes',
        type: 'GET',
        success: function(response) {
            $('#chat-window').empty();
            response.forEach(function(item) {
                $('#chat-window').append('<p>[' + item[0] + '][' + item[1] + '] ' + item[2] + '</p>');
            });
        }
    });
}

loadNotes();

