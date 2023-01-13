function getuserid() {
    var url = 'http://alxtakiy.tech/api/users/'
    axios({
        method: 'get',
        url: url
    })
        .then(res =>test(res))
        .catch(err => console.error(err));
  
  };
  function test(res){
    console.log(res);
    var data = res.data;
    for (let i = 0; i < data.length; i++) {
        var obj = res.data[i];
        console.log(obj);
    }
};

window.addEventListener('load', getuserid());

var e = document.getElementById("dog-names");

document.getElementById('#submit').addEventListener('click', console.log(e.value));
