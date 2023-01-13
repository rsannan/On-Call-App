
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
            var del = "<button class='btn btn-delete' id='" + data.id + "' onClick='removecheck(this.id)''> <span class='mdi mdi-delete mdi-24px'></span> " + 
            "<span class='mdi mdi-delete-empty mdi-24px'></span> <span>Delete</span></button>"
            var str = "<tr>" + title + url + code + curcode + count + del + "</tr>"
            $('#datatablesSimple > tbody:last-child').append(str);
         }
        }
};

function removecheck(check_id) {
    var url = 'http://alxtakiy.tech/api/checks/' + check_id;
    axios({
        method: 'delete',
        url: url,
        headers: {
            Authorization: token,
          }
    })
        .then(res =>  getid(res))
        .catch(err => console.error(err));
  };

  function getbtnid() {
   
  };

$( document ).ready( getchecks );
$( document ).ready( getuser );
document.getElementByClassName('btn-delete').addEventListener('click',);