var express = require('express');
var router = express.Router();
var fs = require('fs')
var session = require('express-session');
var bcrypt = require('bcrypt');
var jsonParser = express.json();
var md5 = require('md5');

router.use(session({
    secret: '8d4thWXFhGdh4J1s',
    resave: false,
    saveUninitialized: false
}))
  

router.all('/', function(req, res, next) {
    req.session.destroy();
    res.render('index');
});

router.post('/user', jsonParser, function (req, res) {
    var user = req.body; // {login : login, password : password}
    var users = JSON.parse(fs.readFileSync('private/users.json', 'utf8'));
    if (users[user.login]){
        bcrypt.compare(user.password, users[user.login].password, (err, result) => {
            console.log(err, result);
            if (result){
                req.session.user = {
                    login: user.login
                };
                res.send([true, 'Успешная авторизация']);
            } else {
                res.send([false, 'Неверный логин или пароль']);
            }
        });
    } else {
        res.send([false, 'Неверный логин или пароль']);
    }
});

module.exports = router;
