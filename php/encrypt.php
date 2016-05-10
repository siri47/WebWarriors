<?php


// $dir    = '.';
// $files1 = array(scandir($dir));

// // foreach ($files1 as $key=>$value ) {
// // 	echo $key," ",$value;
// // }


// print_r($files1);


$text = file_get_contents('mkdir.png');
echo "RIJNDAEL 128 CBC\n";
$max_key_size = mcrypt_get_key_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC)*8;
echo "Max key size: $max_key_size\n";
$block_size = mcrypt_get_block_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC)*8;
echo "Block size: $block_size\n";

//$text = "http://xkcd.com/1323/";

//$iv = mcrypt_create_iv(mcrypt_get_iv_size($enc, $mode), MCRYPT_DEV_URANDOM);

  $iv_size = mcrypt_get_iv_size(MCRYPT_RIJNDAEL_128, MCRYPT_MODE_CBC);
    $iv = mcrypt_create_iv($iv_size, MCRYPT_RAND);

$key="1234567891234567";


for ($i=0; $i <10000 ; $i++) { 

$crypt=aes128_cbc_encrypt($key,$text,$iv);

$uncrypt=aes128_cbc_decrypt($key,$crypt,$iv);

//echo $uncrypt;



//file_put_contents('new.png', $uncrypt);

}

file_put_contents('new.png', $uncrypt);



function aes128_cbc_encrypt($key, $data, $iv) {
  if(16 !== strlen($key)) $key = hash('MD5', $key, true);
  if(16 !== strlen($iv)) $iv = hash('MD5', $iv, true);
  $padding = 16 - (strlen($data) % 16);
  $data .= str_repeat(chr($padding), $padding);
  return mcrypt_encrypt(MCRYPT_RIJNDAEL_128, $key, $data, MCRYPT_MODE_CBC, $iv);
}






function aes128_cbc_decrypt($key, $data, $iv) {
  if(16 !== strlen($key)) $key = hash('MD5', $key, true);
  if(16 !== strlen($iv)) $iv = hash('MD5', $iv, true);
  $data = mcrypt_decrypt(MCRYPT_RIJNDAEL_128, $key, $data, MCRYPT_MODE_CBC, $iv);
  $padding = ord($data[strlen($data) - 1]);
  return substr($data, 0, -$padding);
}




?>