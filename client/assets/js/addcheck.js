function getuser() {
    var userid = 4;
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
    var userid = 4;
    var url = 'http://alxtakiy.tech/api/checks/'
    var title = $('#actitle').val();
    var acurl = $('#acurl').val();
    var method = $('#acmethod').val();
    var code = $('#accode').val();
    var data = {
        title: title,
    url: acurl,
    method_id: method,
    status_code: code
    }
    var token = sessionStorage.getItem('token');
    axios({
        method: 'post',
        url: url,
        data: data,
        headers: {
            Authorization: token
          }
    })
        .then(res => console.log(res))
        .catch(err => console.error(err));
  };
  window.addEventListener('load', getuser);
  document.getElementById('acbtn').addEventListener('click', postcheck);