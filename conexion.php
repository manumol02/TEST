<?php
$servername = "localhost";
$username = "root";
$password = "Michin8805";
$db = "school";
 

$conn = mysqli_connect($servername, $username, $password,$db);
if (!$conn) {
    die("Conexión fallida: " . mysqli_connect_error());
}

if (!mysqli_select_db($conn, $db)) {
    die("Error al seleccionar la base de datos: " . mysqli_error($conn));
}


?>

