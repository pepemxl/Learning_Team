<!DOCTYPE html>
<html>
    <head>
        <title>Learn how services works in docker-compose</title>
    </head>
    <body>
        <div class="jumbotron text-center">
            <h1>Ejemplo de uso de servicios con <code>docker-compose</code></h1>
            <p>Ejemplo utilizando funci&oacute;n <code>file_get_contents</code>
            del lado del servidor.</p>
            <div class="container p-3 my-3 border text-left">
                <p>Resultado de <code>file_get_contents('http://example-service/')</code>:</p>
                <ul>
                    <?php
                    // el servicio http://example-service/ es llamado desde el lado del servidor
                    $json = file_get_contents('http://example-service/');
                    //$json = file_get_contents('http://localhost:5001/');
                    $obj = json_decode($json);
                    echo "<li>cors: $obj->cors</li>";
                    $data2 = $obj->data;
                    foreach ($data2 as $item) {
                        echo "<li>$item</li>";
                    }
                    ?>
                </ul>
            </div>
            <div class="container p-3 my-3 border text-left">
                <p>Resultado de <code>file_get_contents('http://example-service/miapi/')</code>:</p>
                <ul>
                    <?php
                    $json = file_get_contents('http://example-service/miapi/');
                    $obj = json_decode($json);
                    echo "<li>cors: $obj->cors</li>";
                    $data2 = $obj->data;
                    foreach ($data2 as $item) {
                        echo "<li>$item</li>";
                    }
                    ?>
                </ul>
            </div>
            <p>En este caso como estamos haciendo la llamada dentro del servicio y estamos
                usando docker-compose no tenemos el problema de cors.
            </p>
        </div>
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <!-- jQuery library -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <!-- Popper JS -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <!-- Latest compiled JavaScript -->
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script> 
    </body>
</html>