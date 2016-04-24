<html><body>
<?php
// A simple web site in Cloud9 that runs through Apache
// Press the 'Run' button on the top to start the web server,
// then click the URL that is emitted to the Output tab of the console
require_once __DIR__ . "/vendor/autoload.php";
echo 'Hello world from Cloud9!';
	$m = new MongoDB\Client("mongodb://somdeep:root@ds041861.mlab.com:41861/warrior");
    //echo extension_loaded("mongo") ? "loaded\n" : "not loaded\n";
   ;
    $db=$m->warrior;
   
    // $db->array('messages');
    // $collection=$db->users;
    // $cursor = $collection->find();
    $collection=$db->work;
    $cursor=$collection->findOne();
    //echo $collection;
    // foreach ($cursor as $id => $value) {
    //     echo "$id:";
    //     var_dump($value);
    // 
    // }
    
    var_dump($cursor);
    
    // $document = $collection->findOne(['username'=> 'Somdeep Dey']);
    //$document = $collection->findOne(['username' => 'Somdeep Dey']);
    // foreach ($collection as $document) {
    //     echo $document;
    //      // code...
    // }
    //var_dump($document);
?>
</body>
</html>