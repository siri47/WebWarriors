<?php 
session_start();


if(!isset($_SESSION['username']))
{
	echo "entered here";
	header("Location: http://localhost/php/login.html");
	exit();

}

else{
echo $_SESSION['username'];
echo "YAY!, Login  successful";
}


unset($_SESSION["username"]);


 ?>






