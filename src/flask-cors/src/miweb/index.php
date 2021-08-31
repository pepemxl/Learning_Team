<html>
    <head>
        <title>My WEB</title>
    </head>

    <body>
        <h1>Welcome to my web experiment</h1>
        <ul>
            <?php
            $json = file_get_contents('http://example-service/');
            $obj = json_decode($json);
            $data2 = $obj->data;
            foreach ($data2 as $item) {
                echo "<li>$item</li>";
            }
            ?>
        </ul>
    </body>
</html>