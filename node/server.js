var http = require('http');
var express = require('express'),
    path = require('path'),
    logger = require('morgan'),
    bodyParser = require('body-parser'),
    session = require('express-session'),
    fs = require('fs');
    var mongoose    = require('mongoose');
    var dbUrl       = "mongodb://flatemate:flatemate@ds033915.mongolab.com:33915/flatemateio";
    //var dbUrl = "mongodb://localhost:27017/flatmate1";

    var db          = mongoose.connect(dbUrl);

const PORT  = 9000;



function handleRequest(request,response){
    console.log(request.url);
    response.end('It works!! Path hit: ' + response.url);
}

var server = http.createServer(handleRequest);

server.listen(PORT,function(){
    console.log("Server listening on : http://localhost:%s",PORT);

});





