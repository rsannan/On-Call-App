$( document ).ready(function() {
    var token = sessionStorage.token;
    var token1 = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY3MjkyNzgyMSwianRpIjoiNmQxNzg0NjUtOGIyOC00MTM0LWE0ZjctNzUyZGFiNmYzYjk3IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNjcyOTI3ODIxfQ.ctvSSie9E_xrKN921YmzUtNnE-hp8uxpRDCHGXnfZFs';
    $.ajax({
        url: 'http://3.239.72.122:5000/api/checks',
        type: 'GET',
        dataType: 'json',
        headers: {"Authorization": 'Bearer '+token1},
        success: function(response){
            console.log(response)
            $('edfirstname').text('New Header!!!'),
            $('edlastname').text('New Header!!!'),
            $('edphone').text('New Header!!!'),
            $('edemail').text('New Header!!!');
        },
        error: function(err) {
            console.log(err);
            console.log('Bearer '+token1);
              }
          
    });
  });

