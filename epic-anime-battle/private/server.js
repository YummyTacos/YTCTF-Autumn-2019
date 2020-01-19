#!/usr/bin/env node

var app = require('./app');
var debug = require('debug')('ytctf-task-server:server');
var http = require('http');

var config = require('./private/config.json');
var secure = config.secure || false;
var port = config.port;

var server;

if (secure){
    var options = {
        key: fs.readFileSync(config.secure_key),
        cert: fs.readFileSync(config.secure_cert)
    };
    server = require('https').createServer(options, app);
    server.listen(443);

    require('http').createServer(function(req, res) {
      res.writeHead(301, {
        Location: "https://" + req.headers["host"].replace("www.", "") + req.url
      });
      res.end()
    }).listen(80);
} else {
  server = http.createServer(app).listen(port);
}

app.set('port', port);

server.on('error', onError);
server.on('listening', onListening);

function onError(error) {
  if (error.syscall !== 'listen') {
    throw error;
  }

  var bind = typeof port === 'string'
    ? 'Pipe ' + port
    : 'Port ' + port;

  switch (error.code) {
    case 'EACCES':
      console.error(bind + ' requires elevated privileges');
      process.exit(1);
      break;
    case 'EADDRINUSE':
      console.error(bind + ' is already in use');
      process.exit(1);
      break;
    default:
      throw error;
  }
}


function onListening() {
  var addr = server.address();
  var bind = typeof addr === 'string'
    ? 'pipe ' + addr
    : 'port ' + addr.port;
  debug('Listening on ' + bind);
}
