<?php

require_once __DIR__ . "/vendor/autoload.php";
$m = new MongoDB\Client("mongodb://somdeep:root@ds041861.mlab.com:41861/warrior");
session_start();



$name = $_POST["name"];
$password = $_POST["password"];
//echo $name;
//echo $password;

$db=$m->warrior;
$collection=$db->users;


$cursor=$collection->findOne(["name"=>$name]);


   
if ($cursor) 
{
	echo $cursor->name;
	echo $cursor->password;

	if ($cursor->name == $name && $cursor->password == $password) {
			 $_SESSION['username'] = $cursor->name;
			 echo $_SESSION['username'];
			header("Location: http://localhost/php/success.php");

			exit();
		}	
}
   


header("Location: http://localhost/php/login.html");
exit();
   
 






?>