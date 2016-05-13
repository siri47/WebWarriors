# WebWarriors	

***Web-app framework comparison***



## Team

- Aishwarya Iyer
- Kavya Premkumar
- Rohit Gurunath
- Siri Haricharan
- Somdeep Dey




## Sample Framework and App Setup : Ruby on Rails



![img](http://thenextweb.com/wp-content/blogs.dir/1/files/2015/02/CoM_Stuk.io-Ruby-on-Rails1.jpg)



#### Basic Setup

Everything involved in setting up RubyOnRails can be found here:

http://guides.rubyonrails.org/getting_started.html



Thereafter,  after cloning the repository via: 

`git clone https://github.com/siri47/WebWarriors.git`



All that needs to be done now is to enter the `rails` folder and run the following command:

```markdown
bundle install
```

This will automatically take care of all the package management associated with the application by generating all the **Gems** (necessary dependencies) required by Ruby for this project.



#### Project Overview

The essential steps involved in running and testing this application  are as follows :



1. In order to start the server, type:

   `rails server`

2. Now, the following options/routes/tests are available:

   - **Basic Sign up**

     /upload/signup

   - **Basic Sign in**

     /upload/signin

   - **Image Rendering**

     /upload/serveimages

     - To load test : `ab -n 1000 http://localhost:PORT/upload/serveimages `

   - **Video Rendering**

     /upload/servevideos

     - To load test : `ab -n 1000 http://localhost:PORT/upload/servevideo `

   - **Server-Side encryption**

     /upload/encrypt

     - To load test : Go to the test folder in the root directory of the repository, run:

       ` python test_scripts.py 0 urls.txt`

   - **CSRF Attack**

     Test html file located under tests/security_tests/csrf.html

   - **Cross-side Scripting**

     Attack can be carried after signup and logging in, by inserting a **JavaScript** scriptlet in an input box on the front-end view present after logging in. 




## Sample Framework and App Setup : PHP

![img](https://upload.wikimedia.org/wikipedia/commons/c/c1/PHP_Logo.png)



#### Basic Setup

Everything involved in setting up PHP can be found here:

http://www.howtogeek.com/howto/ubuntu/installing-php5-and-apache-on-ubuntu/



Thereafter,  after cloning the repository via: 

`git clone https://github.com/siri47/WebWarriors.git`



Additionally for PHP, it is also necessary to install **Composer**:

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-composer-on-ubuntu-14-04
Composer is a third-party dependency manager for PHP. 

```
$ pecl install mongodb
$ echo "extension=mongodb.so" >> `php --ini | grep "Loaded Configuration" | sed -e "s|.*:\s*||"`

```

The preferred method of installing this library is with [Composer](https://getcomposer.org/) by running the following from the `php` folder:

```
$ composer require "mongodb/mongodb=^1.0.0"
```



It is also necessary to create a symlink to the `php` folder in the `/var/www/` webroot folder to ensure the PHP project is hosted on Apache.



#### Project Overview

The essential steps involved in running and testing this application  are as follows :



1. In order to start the server, type:

   Apache is up and running by default on Ubuntu.

2. Now, the following options/routes/tests are available:

   - **Basic Sign up**

     /php/signup.html

   - **Basic Sign in**

     /php/login.html

   - **Image Rendering**

     /php/mkdir.png

     - To load test : `ab -n 1000 http://localhost:PORT/php/mkdir.png `

   - **Video Rendering**

     /php/sample.mp4

     - To load test : `ab -n 1000 http://localhost:PORT/php/sample.mp4`

   - **Server-Side encryption**

     /php/encrypt.php

     - To load test : Go to the test folder in the root directory of the repository, run:

       ` python test_scripts.py 0 urls.txt`

   - **CSRF Attack**

     Test html file located under tests/security_tests/csrf.html

   - **Cross-side Scripting**

     Attack can be carried after signup and logging in, by inserting a **JavaScript** scriptlet in an input box on the front-end view present after logging in. 

     ​

## Sample Framework and App Setup : Node.Js

![img](https://camo.githubusercontent.com/009dff4f162c762ed0f6f26ad4436eb118a629b2/687474703a2f2f7777772e646d7574682e6f72672f66696c65732f6e6f64656a732d6461726b2e706e67)



#### Basic Setup

Everything involved in setting up NodeJs can be found here:

https://nodejs.org/en/download/package-manager/



Thereafter,  after cloning the repository via: 

`git clone https://github.com/siri47/WebWarriors.git`



All that need to be done inside the node folder is :

```
$ npm install
```



This will take care of all the node libraries required as the dependencies are provided in the `package.json` file.

#### Project Overview

The essential steps involved in running and testing this application  are as follows :



1. In order to start the server, type:

   `node server.js`

2. Now, the following options/routes/tests are available:

   - **Basic Sign up**

     /signup

   - **Basic Sign in**

     /login

   - **Image Rendering**

     /image

     - To load test : `ab -n 1000 http://localhost:9000/image `

   - **Video Rendering**

     /video

     - To load test : `ab -n 1000 http://localhost:9000/video`

   - **Server-Side encryption**

     /encrypt

     - To load test : Go to the test folder in the root directory of the repository, run:

       ` python test_scripts.py 0 urls.txt`

   - **CSRF Attack**

     Test html file located under tests/security_tests/csrf.html

   - **Cross-side Scripting**

     Attack can be carried after signup and logging in, by inserting a **JavaScript** scriptlet in an input box on the front-end view present after logging in. 



## Sample Framework and App Setup : Python - Flask

![img](https://stormpath.com/images/blog/Flask.png)



#### Basic Setup

Everything involved in setting up Flask can be found here:

http://flask.pocoo.org/docs/0.10/installation/

Thereafter,  after cloning the repository via: 

`git clone https://github.com/siri47/WebWarriors.git`

Pip, a package manager for Python, generally comes out of the box but can be installed based on:

https://pip.pypa.io/en/stable/installing/

All that need to be done inside the node folder for any  missing dependencies is :

```
$ pip install dependency
```



#### Project Overview

The essential steps involved in running and testing this application  are as follows :



1. In order to start the server, type:

   `python server.py`

2. Now, the following options/routes/tests are available:

   - **Basic Sign up**

     /signup

   - **Basic Sign in**

     /login

   - **Image Rendering**

     /imgRetrieve

     - To load test : `ab -n 1000 http://localhost:5000/imageRetrieve `

   - **Video Rendering**

     /videoRetrieve

     - To load test : `ab -n 1000 http://localhost:5000/videoRetrieve`

   - **Server-Side encryption**

     /encrypt

     - To load test : Go to the test folder in the root directory of the repository, run:

       ` python test_scripts.py 0 urls.txt`

   - **CSRF Attack**

     Test html file located under tests/security_tests/csrf.html

   - **Cross-side Scripting**

     Attack can be carried after signup and logging in, by inserting a **JavaScript** scriptlet in an input box on the front-end view present after logging in. 



## Eventual Results

![comparison.png](https://github.com/siri47/WebWarriors/blob/master/comparison.png?raw=true)