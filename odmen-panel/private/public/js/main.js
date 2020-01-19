var timeout;

document.addEventListener('keydown', function(event) {
    if (event.code == 'Enter' && document.getElementById("loginp").value && document.getElementById("passinp").value) {
        signIn();
    } else if (event.code == 'Enter'){
        setError('Заполните все поля');
    }
});

function setError(err){
    clearTimeout(timeout);
    document.querySelector('#user-success').innerText = err;
    timeout = setTimeout(function(){
        document.querySelector('#user-success').innerText = '';
    }, 8000);
}

function signIn(){
    axios.post('/user', {
        login: document.getElementById("loginp").value,
        password: document.getElementById("passinp").value
    })
    .then(function (response) {
        if (response.data[0]){
            clearTimeout(timeout);
            window.location.replace("/odmen");
        } else {
            setError(response.data[1]);
        }
    })
}