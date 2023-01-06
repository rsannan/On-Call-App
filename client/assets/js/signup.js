document.querySelector('.img__btn').addEventListener('click', function() {
    document.querySelector('.cont').classList.toggle('s--signup');
  });

  $( "#signupbtn" ).on( "click", function(e) {
    e.preventDefault();
    var username = $('#suname').val();
		var email 	 = $('#suemail').val();
		var password = $('#supassword').val();
			
		var atpos  = email.indexOf('@');
		var dotpos = email.lastIndexOf('.com');

if(username == ''){ // check username not empty
			alert('please enter username !!'); 
		}
		else if(!/^[a-z A-Z]+$/.test(username)){ // check username allowed capital and small letters 
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
				url: 'signup.php',
				type: 'post',
				data: 
					{newusername:username, 
					 newemail:email, 
					 newpassword:password
					},
				success: function(response){
					$('#message').html(response);
				}
			});
				
			$('#registraion_form')[0].reset();
		}
	});

$( "#signinbtn" ).on( "click", function() {
  window.alert( "<p> was clicked" );
});
