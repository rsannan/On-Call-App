document.querySelector('.img__btn').addEventListener('click', function() {
    document.querySelector('.cont').classList.toggle('s--signup');
  });

  $(document).on( "click", '#signupbtn', function(e) {
    e.preventDefault();
    var firstname = $('#sufname').val();
	var lastname = $('#sulname').val();
		var email 	 = $('#suemail').val();
		var password = $('#supassword').val();
		var phone = $('#suphone').val();
			
		var atpos  = email.indexOf('@');
		var dotpos = email.lastIndexOf('.com');

if(firstname == ''){ // check username not empty
			alert('please enter firstname !!'); 
		}
		else if(lastname == ''){ 
			alert('please enter lastname !!');
		}
		else if(!/^[a-z A-Z]+$/.test(firstname)){ // check username allowed capital and small letters 
			alert('firstname only capital and small letters are allowed !!');
		}
		else if(!/^[a-z A-Z]+$/.test(lastname)){ 
			alert('firstname only capital and small letters are allowed !!'); 
		}
		else if(email == ''){ //check email not empty
			alert('please enter email address !!'); 
		}
		else if(atpos < 1 || dotpos < atpos + 2 || dotpos + 2 >= email.length){ //check valid email format
			alert('please enter valid email address !!'); 
		}
		else if(!/^[0-9]+$/.test(phone)){ 
			alert('please enter valid phone number !!'); 
		}
		else if(password == ''){ //check password not empty
			alert('please enter password !!'); 
		}
		else if(password.length < 6){ //check password value length six 
			alert('password must be 6 !!');
		} 
		else{	
			var person= {firstname: firstname,
				lastname: lastname,
				email: email,
				password: password,
				phone: phone}		
			$.ajax({
				url: 'http://alxtakiy.tech/api/users/',
				type: 'POST',
				contentType: 'application/json; charset=utf-8;',
				dataType: 'json',
				data: JSON.stringify(person),
				success: function(response){
					$('#message').html("Thank You for joining us."),
					setTimeout(window.location.replace("signup.html"), 10000);
				},
				error: function(xhr, status, error) {
					alert(xhr.responseText);
				  }
			});
				
			$('#signupfr')[0].reset();
		}
	});

	$(document).on( "click", '#signinbtn', function(e) {
		e.preventDefault();
			var email 	 = $('#siemail').val();
			var password = $('#sipassword').val();
				
			var atpos  = email.indexOf('@');
			var dotpos = email.lastIndexOf('.com');
			console.log(email, password);
	
	if(email == ''){ // check username not empty
				alert('please enter email !!'); 
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
				var person= {
					email: email,
					password: password,}		
				$.ajax({
					url: 'http://alxtakiy.tech/api/users/login',
					type: 'POST',
					contentType: 'application/json; charset=utf-8;',
					dataType: 'json',
					data: JSON.stringify(person),
					success: function(response){
						var token = "Bearer ".concat(response['access_token'])
						localStorage.setItem("token", token),
						localStorage.setItem("email", email),
						setTimeout(window.location.replace("homepage.html"), 10000);

					},
					error: function(xhr, status, error) {
						alert(xhr.responseText);
					  }
				});
					
				$('#signinfr')[0].reset();
			}

	});