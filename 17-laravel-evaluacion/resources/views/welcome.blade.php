<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {
                font-family: 'figtree', sans-serif;
                margin: 0 20px;
                padding: 10;
                background-color: #f8f9fa;
            }
            ul {
                list-style-type: none;
                margin: 0;
                padding: 0;
                overflow: hidden;
                background-color: #333;
            }
            li {
                float: left;
            }
            li a {
                display: block;
                color: white;
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
            }
            li a:hover {
                background-color: #280e51;
            }
        </style>

        <title>Clientes Natalia</title>

        <!-- Fonts -->
        <link rel="preconnect" href="https://fonts.bunny.net">
        <link href="https://fonts.bunny.net/css?family=figtree:400,600&display=swap" rel="stylesheet" />

    </head>
    <body class="antialiased">
        <ul>
            <li><a href="./customers">Ver clientes</a></li>
            <li><a href="./customers/create">Agregar cliente</a></li>
        </ul>

        <h1>Clientes</h1>
        <p>En esta pagina se pueden administrar los clientes con los que cuenta la empresa</p>
    </body>
</html>
