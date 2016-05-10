<?php

require_once __DIR__ . "/vendor/autoload.php";
	  $m = new MongoDB\Client("mongodb://127.0.0.1:27017/warrior");
    //$m = new MongoDB\Client("mongodb://somdeep:root@ds041861.mlab.com:41861/warrior");


$name = "name";





$db=$m->warrior;
   
$collection=$db->work;
 

   for ($i=0; $i <1000 ; $i++) { 
    // Insert into collection
   $collection->insertone(array('name' => $name,'email'=>'email@gmail.com','location'=>'location'));
     
   }
   

  header("Location: http://localhost/php/");
   exit();
   



   function endl()
   {
     echo "<br>";
   }
   



?>