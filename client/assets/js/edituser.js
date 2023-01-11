function getuserid() {
    var url = 'http://alxtakiy.tech/api/users/'
    axios({
        method: 'get',
        url: url
    })
        .then(res => function(res){
            for (let i = 0; i < res.length; i++) {
                var data = res.data[i];
                if (data.email == sessionStorage.getItem("email")){
                    return data.id;
                }
            }
        })
        .catch(err => console.error(err));
  };

function getuser() {
    var userid = getuserid();
    var url = 'http://alxtakiy.tech/api/users/' + userid
    axios({
        method: 'get',
        url: url
    })
        .then(res => changeout(res))
        .catch(err => console.error(err));
  };

  window.addEventListener('load', getuser);

  function changeout(res){
    // check for user idnumber and match with users data
    // 
    let arr = res.data;
    let name = arr.firstname+ " " + arr.lastname;
     $('#diname').text(name);
     $('#diemail').text(arr.email);
     $('#edfirstname').val(arr.firstname);
     $('#edlastname').val(arr.lastname);
     $('#edphone').val(arr.phone);
     $('#edemail').val(arr.email)
     


};

function updateuser(){
    var firstname = $('#edfirstname').val();
	var lastname = $('#edlastname').val();
		var email 	 = $('#edemail').val();
		var phone = $('#edphone').val();
    var data = {firstname: firstname,
        lastname: lastname,
        email: email,
        phone: phone}
    axios.put('http://alxtakiy.tech/api/users/1', data
        
    )
        .then(res => console.log(res))
        .catch(err => console.error(err));

        document.getElementById('savebtn').addEventListener('click', getuser);
};

document.getElementById('savebtn').addEventListener('click', updateuser);
