<?Php
include_once ('conexion.php');

$sql_create = "CREATE TABLE IF NOT EXISTS Students (
    id INT ,
    name VARCHAR(70),
    age INT
)";

if (mysqli_query($conn, $sql_create)) {
    echo "Tabla 'Students' creada con éxito.";
} else {
    echo "Error al crear la tabla: " . mysqli_error($conn);
}

$sql_insert = "INSERT INTO Students (id, name, age) VALUES
    (1, 'Juan', 28),
    (2, 'Nicol', 25),
    (3, 'Emilio', 19),
    (4, 'karol', 13),
    (5, 'Alejandra', 22),
    (6, 'Daniel', 10),
";

if (mysqli_query($conn, $sql_insert)) {
    echo "Datos insertados correctamente en la tabla 'Students'.";
} else {
    echo "Error al insertar datos: " . mysqli_error($conn);
}
/*
sql_busqueda ="SELECT name FROM Students WHERE age > 18";*/



