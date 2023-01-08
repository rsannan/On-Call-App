$( document ).ready(function() {
    var token = sessionStorage.token;
    $.ajax({
        url: 'http://localhost:5000/api/checks',
        type: 'GET',
        headers: {
            'Authorization': token,
        },
        contentType: 'application/json; charset=utf-8;',
        dataType: 'json',
        data: JSON.stringify(person),
        success: function(response){
            console.log(response)
        },
        error: function(xhr, status, error) {
            alert(xhr.responseText);
          }
    });
  });