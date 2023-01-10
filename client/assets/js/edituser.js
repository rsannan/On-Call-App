$( document ).ready(function() {
    var token = sessionStorage.token;
    $.ajax({
        url: 'http://3.239.72.122:5000/api/checks',
        type: 'GET',
        headers: {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MjkyNzgyMSwianRpIjoiNmQxNzg0NjUtOGIyOC00MTM0LWE0ZjctNzUyZGFiNmYzYjk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjcyOTI3ODIxfQ.ctvSSie9E_xrKN921YmzUtNnE-hp8uxpRDCHGXnfZFs',
        },
        dataType: 'json',
        success: function(response){
            console.log(response)
            $('edfirstname').text('New Header!!!'),
            $('edlastname').text('New Header!!!'),
            $('edphone').text('New Header!!!'),
            $('edemail').text('New Header!!!');
        },
        error: function(xhr, status, error) {
            alert(xhr.responseText);
          }
    });
  });


