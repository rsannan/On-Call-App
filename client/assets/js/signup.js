document.querySelector('.img__btn').addEventListener('click', function() {
    document.querySelector('.cont').classList.toggle('s--signup');
  });

  $(document).on( "click", '#signupbtn', function(e) {
    e.preventDefault();
    var firstname = $('#sufname').val();
	var lastname = $('#sulname').val();
		var email 	 = $('#suemail').val();
		var password = $('#supassword').val();
			
		var atpos  = email.indexOf('@');
		var dotpos = email.lastIndexOf('.com');

if(firstname == ''){ // check username not empty
			alert('please enter firstname !!'); 
		}
		else if(lastname == ''){ 
			alert('please enter lastname !!');
		}
		else if(!/^[a-z A-Z]+$/.test(firstname)){ // check username allowed capital and small letters 
			alert('username only capital and small letters are allowed !!');
		}
		else if(!/^[a-z A-Z]+$/.test(lastname)){ 
			alert('username only capital and small letters are allowed !!'); 
		}
		else if(email == ''){ //check email not empty
			alert('please enter email address !!'); 
		}
		else if(atpos < 1 || dotpos < atpos + 2 || dotpos + 2 >= email.length){ //check valid email format
			alert('please enter valid email address !!'); 
		}
		else if(password == ''){ //check password not empty
			alert('please enter password !!'); 
		}
		else if(password.length < 6){ //check password value length six 
			alert('password must be 6 !!');
		} 
		else{			
			$.ajax({
				url: 'http://alxtakiy.tech/api/users/',
				type: 'POST',
				contentType: 'application/json',
				data: 
					{firstname: firstname,
					lastname: lastname,
					email: email,
					password: password,
					phone: "0987654"
					},
				success: function(response){
					$('#message').html(response);
				}
			});
				
			$('#signupfr')[0].reset();
		}
	});

$( "#signinbtn" ).on( "click", function() {
  window.alert( "<p> was clicked" );
});