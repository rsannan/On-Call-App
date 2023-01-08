$( document ).ready(function() {
    var token = sessionStorage.token;
    $.ajax({
        url: 'http://localhost:5000/api/checks',
        type: 'GET',
        headers: {
            'Authorization': token,
        },
        dataType: 'json',
        success: function(response){
            console.log(response)
        },
        error: function(xhr, status, error) {
            alert(xhr.responseText);
          }
    });
  });