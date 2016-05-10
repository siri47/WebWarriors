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

    var db = mongoose.connect(dbUrl);

    const port  = 9000;

    var users = require('./app/models/users');

    var app = express();
    app.set('view engine','ejs');
    app.set('views', __dirname + '/views');   

    // app.use(express.static(__dirname + '/views'));     // set the static files location

    app.use(bodyParser.json());
    app.use(logger('dev'));

    app.get('/image', function(req, res){

     res.sendfile('mkdir.png');

 });

    app.get('/video', function(req, res){

     res.sendfile('video.mp4');

 });




    app.get('/users', function(req, res){

        users.find(function(err,data){
            if(err)
                res.send(err);
            res.json(data);
        });

    });


    app.get('/login',function(req,res){

        res.render('login');
    });

    app.get('/logincheck',function(req,res){
        
        res.render('success');
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
