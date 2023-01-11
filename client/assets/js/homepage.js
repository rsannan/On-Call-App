function getuser() {
    var userid = 1;
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
    var userid = 1;
    var url = 'http://alxtakiy.tech/api/checks'
    axios({
        method: 'get',
        url: url
    })
        .then(res => showcheck(res, userid))
        .catch(err => console.error(err));
  };

  function showcheck(res, id){
    // check for user idnumber and match with users data
    // 
    for (let i = 0; i < res.length; i++) {
        var data = res.data[i];
        if (id = data.user_id) {
            var title = "<td>"+ data.title +"</td>"
            var url = "<td>"+ data.url +"</td>"
            var code = "<td>"+ data.status_code +"</td>"
            var curcode = "<td>"+ data.status_code +"</td>"
            var date = "<td>"+ "0" +"</td>"
            var str = "tr" + title + url + code + curcode + date +"</tr>"
            $('#datatablesSimple > tbody:last-child').append(str);
        }
    }
};

window.addEventListener('load', getchecks);
window.addEventListener('load', getuser);