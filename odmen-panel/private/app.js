var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var path = require('path');

var allRouter = require('./routes/all');
var indexRouter = require('./routes/index');

var app = express();

app.set('views', path.join(__dirname, 'views'));
app.set('view engine','ejs');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use('/css',express.static(__dirname +'/css'));

app.use('', indexRouter);
app.use('/', allRouter);

app.use(function(err, req, res, next) {
    console.log('ERROR');
    res.status(500);
    res.render('error', {statusCode: 500});
});

module.exports = app;
