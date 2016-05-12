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




## Eventual Results

![comparison.png](https://github.com/siri47/WebWarriors/blob/master/comparison.png?raw=true)