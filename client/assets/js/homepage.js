
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

  function changeout(res){
    // check for user idnumber and match with users data
    // 
    let arr = res.data;
    let name = arr.firstname+ " " + arr.lastname;
     $('#hpname').text(name);
};
function getuser() {
    getuserid();
    var userid = localStorage.getItem("id");
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
     $('#hpname').text(name);
};

function getchecks() {
    getuserid();
    var userid = localStorage.id;
    var url = 'http://alxtakiy.tech/api/checks';
    var token = localStorage.token;

    axios({
        method: 'get',
        url: url,
        headers: {
            Authorization: token,
          }
    })
        .then(res => showcheck(res, userid))
        .catch(err => console.error(err));
  };

  function showcheck(res, id){
    // check for user idnumber and match with users data
    // 
    var arr = res.data;
    for (let i = 0; i < arr.length; i++) {
        var data = res.data[i];
         if (id == data.user_id) {
            var title = "<td>"+ data.title +"</td>"
            var url = "<td>"+ data.url +"</td>"
            var code = "<td>"+ data.status_code +"</td>"
            var curcode = "<td>"+ data.status +"</td>"
            var count = "<td>"+ data.check_count +"</td>"
            var str = "<tr>" + title + url + code + curcode + count +"</tr>"
            $('#datatablesSimple > tbody:last-child').append(str);
         }
        }
};
$( document ).ready( getchecks );
$( document ).ready( getuser );