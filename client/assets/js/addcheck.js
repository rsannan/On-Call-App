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
    var userid = localStorage.id;
    var url = 'http://alxtakiy.tech/api/users/' + userid
    axios({
        method: 'get',
        url: url
    })
        .then(res => changeout(res))
        .catch(err => console.error(err));
  };


  function changeout(res){
    // check for user idnumber and match with users data
    // 
    let arr = res.data;
    let name = arr.firstname+ " " + arr.lastname;
     $('#acname').text(name);
     $('#acemail').text(arr.email);

};

function postcheck() {
    var userid = localStorage.id;
    var url = 'http://alxtakiy.tech/api/checks/'
    var title = $('#actitle').val();
    var acurl = $('#acurl').val();
    var method = $('#acmethod').val();
    var code = $('#accode').val();
    var data = {
        title: title,
    url: acurl,
    method_id: method,
    status_code: code,
    }
    var token = localStorage.token;
    axios({
        method: 'post',
        url: url,
        data: data,
        headers: {
            Authorization: token,
            'Content-Type': 'application/json'
          }
    })
        
        .then (setTimeout(window.location.assign("homepage.html"), 10000))
        .catch(err => console.error(err));
  };
  window.addEventListener('load', getuser);
  document.getElementById('acbtn').addEventListener('click', postcheck);