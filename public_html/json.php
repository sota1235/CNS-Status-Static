<?php

// Enter your login name
$login_name = 'your_login_name';

header('Access-Control-Allow-Origin: *');

$json = file_get_contents("/home/".$login_name."/public_html/mail.json");

echo $json;
?>
