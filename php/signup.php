<?php

require_once __DIR__ . "/vendor/autoload.php";
	  //$m = new MongoDB\Client("mongodb://129.236.228.63:27017/warrior");
    //$m = new MongoDB\Client("mongodb://somdeep:root@ds041861.mlab.com:41861/warrior");
    $m = new MongoDB\Client("mongodb://127.0.0.1:27017/warrior");


$name = $_POST["name"];
$password = $_POST["password"];
echo $name;
echo $password;


$db=$m->warrior;
   
$collection=$db->users;
 

    //Read a single value
   $cursor=$collection->findOne(["name"=>$name]);
   //var_dump($cursor);
   if ($cursor) 
   {
   		header("Location: http://localhost/php/signup.html");
		exit();
   }
    // Insert into collection
   $collection->insertone(array('name' => $name,'password'=>$password));
        
   header("Location: http://localhost/php/login.html");
   exit();
   



   function endl()
   {
     echo "<br>";
   }
   



?>