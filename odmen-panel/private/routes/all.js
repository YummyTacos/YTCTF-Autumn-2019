var express = require('express');
var router = express.Router();
var path = require('path'); 
var fs = require('fs');

router.all('/odmen', function(req, res, next){
    if (req.session.user != undefined && req.session.user.login != undefined){
        res.render('odmen');
    } else {
        res.status(418);
        res.render('error', { statusCode: 418 });
    }
})

router.all('/get_a_super_secret_flag_that_is_hidden_in_the_source_code', function(req, res, next){
    let flag = "ytctf{we_hid3_flags_in_source_c0des_yay}";
    res.send(flag);
})

router.all('/*', function(req, res, next) {
    fs.readFile('.' + req.originalUrl, function(err, contents) {
        if (err){
            res.status(404);
            res.render('error', { statusCode: 404 });
        } else {
            res.render('all', {data: contents.toString()});
        }
    });
});


module.exports = router;
