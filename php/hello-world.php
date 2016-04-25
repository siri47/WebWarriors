<html><body>
<?php

require_once __DIR__ . "/vendor/autoload.php";
	  $m = new MongoDB\Client("mongodb://somdeep:root@ds041861.mlab.com:41861/warrior");
   
   
   $db=$m->warrior;
   
   endl(); 
   echo "Somdeep Dey";
   endl();
   $collection=$db->work;
   $cursor=$collection->find();
    
        
       
       
   //Read Values
   foreach ($cursor as $id => $value) 
   {
    echo($value->name);
    endl();
   }
   
   

   
  
   // Insert into collection
   $collection->insertone(array('name' => 'Harry','job'=>'student'));
   
   //update collection
   $newdata = array('$set' => array("job" => "software"));
   //$c->update(array("firstname" => "Bob"), $newdata);
   $collection->updateone(array("name"=>"Somdeep"),$newdata);
   
   //Read a single value
   $cursor=$collection->findOne(["name"=>"Somdeep"]);
   var_dump($cursor);
   
   //Delete single document
   $collection->deleteone(array("name"=>"Harry"));
   
   function endl()
   {
     echo "<br>";
   }
   
   
?>
</body>
</html>