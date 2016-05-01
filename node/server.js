var http = require('http');
var express = require('express'),
    path = require('path'),
    logger = require('morgan'),
    bodyParser = require('body-parser'),
    session = require('express-session'),
    fs = require('fs');
    var mongoose    = require('mongoose');
    var dbUrl       = "mongodb://somdeep:root@ds041861.mlab.com:41861/warrior";
    //var dbUrl = "mongodb://localhost:27017/flatmate1";

    var db          = mongoose.connect(dbUrl);

const port  = 9000;
var app = express();
app.use(bodyParser.json());
app.use(logger('dev'));

app.get('/image', function(req, res){

		res.sendfile('mkdir.png');

	});

app.get('/video', function(req, res){

		res.sendfile('football.mp4');

	});



app.listen(port, function(){
  console.log('listening on port', port);
});






// function handleRequest(request,response){
//     console.log(request.url);
//     response.end('It works!! Path hit: ' + response.url);
// }

// var server = http.createServer(handleRequest);

// server.listen(PORT,function(){
//     console.log("Server listening on : http://localhost:%s",PORT);

// });





