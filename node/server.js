var http = require('http');
var express = require('express'),
path = require('path'),
logger = require('morgan'),
bodyParser = require('body-parser'),
//session = require('express-session'),
fs = require('fs');
var mongoose    = require('mongoose');
var dbUrl       = "mongodb://localhost:27017/warrior";
var session = require('client-sessions');

    //var dbUrl = "mongodb://localhost:27017/flatmate1";

    var db = mongoose.connect(dbUrl);

    const port  = 9000;

    var users = require('./app/models/users');
    var work = require('./app/models/work');

    var app = express();
    app.set('view engine','ejs');
    app.set('views', __dirname + '/views');   

    // app.use(express.static(__dirname + '/views'));     // set the static files location

    app.use(bodyParser.json());
    app.use(logger('dev'));

app.use(session({
  cookieName: 'session',
  secret: 'random_string_goes_here',
}));

    app.get('/image', function(req, res){

     res.sendfile('mkdir.png');

 });

    app.get('/video', function(req, res){

     res.sendfile('video.mp4');

 });




    app.get('/work', function(req, res){

        work.find(function(err,data){
            if(err)
                res.send(err);
            res.json(data);
        });

    });


    app.get('/workAdd', function(req, res){
 var newUser;
        for(var i=0;i<1000;i++){
          newUser = work({
          name: 'Peter Quill',
          username: 'starlord55',
          admin: true
        });

        // save the user
        newUser.save(function(err) {
          if (err) throw err;

          //console.log('User created!');
        });
        }
        console.log('Users created!');
        res.send(200);
    });


   app.get('/login',function(req,res){

        res.render('login');
    });

   app.get('/signup',function(req,res){

        res.render('signup');
    });


app.post('/signupcheck', function(req, res) {
    console.log(req.body);
var u=new users({ 
    email: req.body.email,
    name: req.body.name,
    password:req.body.password,
});
  users.create(u, function(err, user) {
       if (err) throw err; 
    });
    res.redirect('/login');
});

app.post('/logincheck', function(req, res) {
  users.findOne({ email: req.body.email }, function(err, user) {
    if (!user) {
        console.log("no user");
      res.render('login', { error: 'Invalid email or password.' });
    } else {
      if (req.body.password === user.password) {
        // sets a cookie with the user's info
                  console.log("passwd correct");

        req.session.user = user;
        res.redirect('/userinfo');
      } else {
          console.log("passwd incorrect");

        res.redirect('/login', { error: 'Invalid email or password.' });
      }
    }
  });
});

app.pos


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
