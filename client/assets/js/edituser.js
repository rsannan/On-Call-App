function getuserid() {
    var url = 'http://alxtakiy.tech/api/users/'
    axios({
        method: 'get',
        url: url
    })
        .then(res =>  getid(res))
        .catch(err => console.error(err));
  };


  function getid(res){
    var arr = res.data;
    for (let i = 0; i < arr.length; i++) {
        var data = res.data[i];
        if (data.email == localStorage.getItem('email')){
            localStorage.setItem("id",data.id);
            break;
        }
    }
}

function getuser() {
    getuserid();
    var userid = localStorage.id;
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
    var user_id = localStorage.id;
    var firstname = $('#edfirstname').val();
	var lastname = $('#edlastname').val();
		var email 	 = $('#edemail').val();
		var phone = $('#edphone').val();
    var data = {firstname: firstname,
        lastname: lastname,
        email: email,
        phone: phone}
    axios.put('http://alxtakiy.tech/api/users/' + user_id, data
        
    )
        .then(setTimeout(window.location.assign("homepage.html"), 10000))
        .catch(err => console.error(err));
};

document.getElementById('savebtn').addEventListener('click', updateuser);
