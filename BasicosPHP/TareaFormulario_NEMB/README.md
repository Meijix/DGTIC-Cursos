# Proyecto de Gestión de Usuarios

Este proyecto es una aplicación web básica para la gestión de usuarios, donde los usuarios pueden registrarse e iniciar sesión. La aplicación está desarrollada en PHP y utiliza sesiones para manejar la autenticación de usuarios.

## Estructura del Proyecto

- `index.php`: Página principal de la aplicación.
- `formulario.php`: Página de registro de usuarios.
- `login.php`: Página de inicio de sesión.
- `info.php`: Página de información del usuario autenticado.
- `usuario.php`: Archivo que contiene la lógica relacionada con los usuarios.
- `estilos.css`: Archivo de estilos CSS para la aplicación.

## Funcionalidades

### Registro de Usuarios

Los usuarios pueden registrarse proporcionando la siguiente información:
- Número de cuenta
- Nombre
- Primer apellido
- Segundo apellido
- Género
- Contraseña
- Fecha de nacimiento

La información del usuario se guarda en la sesión.

### Inicio de Sesión

Los usuarios pueden iniciar sesión proporcionando su número de cuenta y contraseña. Si las credenciales son correctas, el usuario es redirigido a la página de información del usuario.

### Información del Usuario

Una vez autenticado, el usuario puede ver su información personal en la página `info.php`.

## Estilos CSS

El archivo `estilos.css` contiene los estilos para la aplicación, incluyendo estilos para formularios, tablas y mensajes de error y éxito.

## Uso

1. Abre `formulario.php` para registrar un nuevo usuario.
2. Completa el formulario de registro y envíalo.
3. Abre `login.php` para iniciar sesión con el usuario registrado.
4. Completa el formulario de inicio de sesión y envíalo.
5. Si las credenciales son correctas, serás redirigido a `info.php` donde podrás ver la información del usuario.

## Video
[Video de la aplicación](video-prueba.mp4)

## Autor

Desarrollado por Natalia Edith Mejia Bautista para el curso de PHP DGTIC, Diciembre 2024.