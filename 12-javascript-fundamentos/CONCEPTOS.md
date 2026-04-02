# Modulo 12: JavaScript - Fundamentos

## Indice de contenidos

1. [Introduccion a JavaScript](#1-introduccion-a-javascript)
2. [Variables: var, let y const](#2-variables-var-let-y-const)
3. [Tipos de datos](#3-tipos-de-datos)
4. [Operadores](#4-operadores)
5. [Estructuras de control: bucles](#5-estructuras-de-control-bucles)
6. [Funciones](#6-funciones)
7. [Programacion Orientada a Objetos (POO)](#7-programacion-orientada-a-objetos-poo)
8. [El DOM (Document Object Model)](#8-el-dom-document-object-model)
9. [Eventos](#9-eventos)
10. [Fetch API y AJAX](#10-fetch-api-y-ajax)
11. [Patrones comunes en JavaScript](#11-patrones-comunes-en-javascript)
12. [Manejo de errores](#12-manejo-de-errores)
13. [Comparacion JavaScript vs Python](#13-comparacion-javascript-vs-python)
14. [Mapa de archivos del modulo](#14-mapa-de-archivos-del-modulo)
15. [Ejercicios de practica](#15-ejercicios-de-practica)

---

## 1. Introduccion a JavaScript

JavaScript es el **lenguaje de programacion de la web**. Es el unico lenguaje que los navegadores ejecutan de forma nativa para hacer las paginas interactivas.

### Que puede hacer JavaScript

- **Modificar el contenido** de una pagina sin recargarla
- **Reaccionar a eventos** del usuario (clicks, teclas, scroll)
- **Comunicarse con servidores** para obtener o enviar datos (AJAX/Fetch)
- **Validar formularios** antes de enviarlos
- **Crear animaciones** y efectos visuales
- **Ejecutarse fuera del navegador** con Node.js (backend)

### Donde se ejecuta

```
Navegador (Frontend):
  HTML (estructura) + CSS (estilos) + JavaScript (comportamiento)

Servidor (Backend):
  Node.js permite ejecutar JavaScript fuera del navegador
```

### Como incluir JavaScript en HTML

```html
<!-- Forma 1: Archivo externo (RECOMENDADA) -->
<script src="mi-script.js"></script>

<!-- Forma 2: Inline (dentro del HTML) -->
<script>
  console.log("Hola desde el HTML");
</script>

<!-- Forma 3: En atributos (NO RECOMENDADA) -->
<button onclick="alert('Hola')">Click</button>
```

### Archivos del modulo que demuestran esto
- `script00.js`, `script01.js`, `script02.js` -> JavaScript puro (se ejecutan con Node.js o en el navegador)
- `Eventos1/eventos.html` + `eventos.js` -> JavaScript conectado a HTML
- `PracticaFinalNat/` -> Proyecto completo con HTML + CSS + JavaScript + API

---

## 2. Variables: var, let y const

Las variables son "contenedores" que almacenan valores. En JavaScript hay tres formas de declararlas:

### const (constante)
```javascript
const PI = 3.14159;
const nombre = "Maria";
// PI = 3.14;  // ERROR: no se puede reasignar

// PERO los objetos/arrays SI se pueden modificar internamente:
const lista = [1, 2, 3];
lista.push(4);       // OK: [1, 2, 3, 4]
// lista = [5, 6];   // ERROR: no se puede reasignar la referencia
```
**Usar const siempre que sea posible.** Es la opcion por defecto.

### let (variable de bloque)
```javascript
let contador = 0;
contador = 1;        // OK: se puede reasignar
let contador = 2;    // ERROR: no se puede re-declarar en el mismo scope

if (true) {
    let x = 10;      // x solo existe dentro de estas llaves
}
// console.log(x);   // ERROR: x no esta definida aqui
```
**Usar let cuando necesites reasignar el valor.**

### var (variable de funcion) - EVITAR
```javascript
var edad = 25;
var edad = 30;       // OK (pero confuso): se puede re-declarar

if (true) {
    var y = 10;      // y existe fuera de las llaves!
}
console.log(y);      // 10 (esto es un bug potencial)
```
**Evitar var.** Tiene comportamientos confusos (hoisting, scope de funcion).

### Tabla comparativa

| Caracteristica | var | let | const |
|---|---|---|---|
| Reasignable | Si | Si | No |
| Re-declarable | Si | No | No |
| Scope | Funcion | Bloque {} | Bloque {} |
| Hoisting | Si (undefined) | Si (error) | Si (error) |
| Uso recomendado | Nunca | Cuando cambia | Por defecto |

### Archivos que lo demuestran
- `script00.js` -> Usa `const` para la tabla (no cambia) y `let` para el incremento (cambia)
- `Eventos1/eventos.js` -> Usa `let` para referencias a elementos del DOM

---

## 3. Tipos de datos

JavaScript tiene tipos **primitivos** (inmutables) y **objetos** (mutables).

### Tipos primitivos

```javascript
// string (cadena de texto)
const nombre = "Maria";
const saludo = 'Hola';              // Comillas simples o dobles
const template = `Hola ${nombre}`;  // Template literal (backticks)

// number (entero o decimal, no hay distincion)
const edad = 25;
const precio = 19.99;
const infinito = Infinity;
const noNumero = NaN;  // "Not a Number" (resultado de 0/0, parseInt("abc"))

// boolean (verdadero o falso)
const activo = true;
const eliminado = false;

// undefined (variable declarada pero sin valor)
let sinValor;
console.log(sinValor);  // undefined

// null (ausencia intencional de valor)
const vacio = null;

// symbol (identificador unico, avanzado)
const id = Symbol("id");

// bigint (numeros enteros muy grandes)
const grande = 9007199254740991n;
```

### Tipos objeto

```javascript
// object (coleccion de pares clave-valor)
const persona = { nombre: "Maria", edad: 25 };

// array (lista ordenada, ES UN OBJETO)
const numeros = [1, 2, 3, 4, 5];

// function (las funciones son objetos de primera clase)
const saludar = function() { return "Hola"; };

// Date, RegExp, Map, Set, etc.
const hoy = new Date();
```

### typeof - Verificar el tipo

```javascript
typeof "hola"      // "string"
typeof 42          // "number"
typeof true        // "boolean"
typeof undefined   // "undefined"
typeof null        // "object"  (BUG historico de JavaScript!)
typeof [1, 2, 3]   // "object"  (arrays son objetos)
typeof function(){} // "function"
```

### Valores Truthy y Falsy

En JavaScript, cualquier valor puede evaluarse como `true` o `false`:

```javascript
// FALSY (se evaluan como false):
false, 0, "", null, undefined, NaN

// TRUTHY (todo lo demas):
true, 42, "hola", [], {}, function(){}

// Ejemplo:
if ("") { /* no se ejecuta */ }
if ("hola") { /* SI se ejecuta */ }
if (0) { /* no se ejecuta */ }
if (42) { /* SI se ejecuta */ }
```

---

## 4. Operadores

### Comparacion: == vs ===

Esta es una de las **trampas mas comunes** de JavaScript:

```javascript
// == (comparacion DEBIL): Convierte tipos antes de comparar
5 == "5"       // true  (convierte "5" a numero)
0 == false     // true  (convierte false a 0)
null == undefined  // true
"" == 0        // true

// === (comparacion ESTRICTA): NO convierte tipos
5 === "5"      // false (diferente tipo)
0 === false    // false
null === undefined  // false

// REGLA: SIEMPRE usar === y !== para evitar bugs
```

### Operadores aritmeticos

```javascript
5 + 3    // 8 (suma)
5 - 3    // 2 (resta)
5 * 3    // 15 (multiplicacion)
5 / 3    // 1.6667 (division, SIEMPRE decimal)
5 % 3    // 2 (modulo/residuo)
5 ** 3   // 125 (potencia, ES7+)

// CUIDADO con + y strings:
5 + "3"    // "53" (concatenacion, no suma!)
"5" - 3    // 2 (conversion a numero)
```

### Operadores logicos

```javascript
true && false   // false (AND: ambos deben ser true)
true || false   // true  (OR: al menos uno debe ser true)
!true           // false (NOT: invierte el valor)

// Short-circuit evaluation (evaluacion de cortocircuito):
const nombre = usuario.nombre || "Anonimo";  // Si nombre es falsy, usa "Anonimo"
const nombre = usuario?.nombre ?? "Anonimo"; // Nullish coalescing (moderno)
```

---

## 5. Estructuras de control: bucles

### Bucle for
```javascript
// Estructura: for (inicio; condicion; incremento)
for (let i = 0; i < 10; i++) {
    console.log(i);
}
```

### Bucle while
```javascript
let i = 0;
while (i < 10) {
    console.log(i);
    i++;  // NUNCA olvidar el incremento!
}
```

### Bucle for...of (para arrays)
```javascript
const frutas = ["manzana", "pera", "uva"];
for (const fruta of frutas) {
    console.log(fruta);  // manzana, pera, uva
}
```

### Bucle for...in (para objetos)
```javascript
const persona = { nombre: "Maria", edad: 25 };
for (const clave in persona) {
    console.log(clave, persona[clave]);  // nombre Maria, edad 25
}
```

### Metodos de array (alternativa moderna a bucles)
```javascript
const numeros = [1, 2, 3, 4, 5];

// forEach: ejecuta una funcion para cada elemento
numeros.forEach(n => console.log(n));

// map: transforma cada elemento y retorna un nuevo array
const dobles = numeros.map(n => n * 2);  // [2, 4, 6, 8, 10]

// filter: filtra elementos segun una condicion
const pares = numeros.filter(n => n % 2 === 0);  // [2, 4]

// find: encuentra el primer elemento que cumple la condicion
const primero = numeros.find(n => n > 3);  // 4

// reduce: reduce el array a un solo valor
const suma = numeros.reduce((acc, n) => acc + n, 0);  // 15
```

### Archivos que lo demuestran
- `script00.js` -> Bucles `for` (tabla de multiplicar) y `while` (triangulo de asteriscos)
- `PracticaFinalNat/js/index.js` -> `$.each()` (equivalente jQuery de forEach)

---

## 6. Funciones

### Tres formas de declarar funciones

```javascript
// 1. Function Declaration (tradicional)
function sumar(a, b) {
    return a + b;
}

// 2. Arrow Function (flecha, ES6)
const sumar = (a, b) => {
    return a + b;
};
// Version corta (una sola expresion):
const sumar = (a, b) => a + b;

// 3. Function Expression (anonima)
const sumar = function(a, b) {
    return a + b;
};
```

### Scope (alcance)

```javascript
const global = "Soy global";

function ejemplo() {
    const local = "Soy local";
    console.log(global);  // OK: puede acceder a variables globales
    console.log(local);   // OK: puede acceder a sus propias variables
}

// console.log(local);    // ERROR: no existe fuera de la funcion
```

### Closures (clausuras)

Un closure es una funcion que "recuerda" las variables del scope donde fue creada:

```javascript
function crearContador() {
    let cuenta = 0;  // Variable "privada"
    return function() {
        cuenta++;
        return cuenta;
    };
}

const contador = crearContador();
console.log(contador());  // 1
console.log(contador());  // 2
console.log(contador());  // 3
// 'cuenta' no es accesible directamente, solo a traves del closure
```

### Callbacks

Un callback es una funcion que se pasa como argumento a otra funcion:

```javascript
function hacerAlgo(callback) {
    console.log("Haciendo algo...");
    callback();  // Ejecuta la funcion recibida
}

hacerAlgo(function() {
    console.log("Terminado!");
});

// Con arrow function:
hacerAlgo(() => console.log("Terminado!"));
```

### Archivos que lo demuestran
- `script01.js` -> Las tres formas de funciones: tradicional, flecha, anonima
- `Eventos1/eventos.js` -> Callbacks en `addEventListener` y `DOMContentLoaded`
- `PracticaFinalNat/js/index.js` -> Callbacks en `$.ajax()` (success, error, beforeSend)

---

## 7. Programacion Orientada a Objetos (POO)

### Clases (ES6)

```javascript
class Animal {
    // Constructor: se ejecuta al crear una instancia con 'new'
    constructor(nombre, tipo) {
        this.nombre = nombre;  // 'this' se refiere al objeto que se esta creando
        this.tipo = tipo;
    }

    // Metodo
    hablar() {
        return `${this.nombre} dice algo`;
    }
}

const gato = new Animal("Michi", "Felino");
console.log(gato.hablar());  // "Michi dice algo"
```

### Herencia

```javascript
class Perro extends Animal {
    constructor(nombre, raza) {
        super(nombre, "Canino");  // Llama al constructor del padre
        this.raza = raza;
    }

    // Metodo propio
    ladrar() {
        return `${this.nombre} dice: Guau!`;
    }

    // Override: sobreescribe el metodo del padre
    hablar() {
        return this.ladrar();
    }
}

const firulais = new Perro("Firulais", "Labrador");
console.log(firulais.hablar());  // "Firulais dice: Guau!"
console.log(firulais.tipo);      // "Canino" (heredado del padre)
```

### Cadena de prototipos (Prototype Chain)

Cuando accedes a una propiedad o metodo de un objeto, JavaScript busca:
1. En el objeto mismo
2. En su prototipo (clase padre)
3. En el prototipo del prototipo
4. ... hasta llegar a `Object.prototype` (null)

```javascript
firulais.ladrar();     // Encontrado en Perro
firulais.hablar();     // Encontrado en Perro (override)
firulais.toString();   // Encontrado en Object.prototype
```

### Archivos que lo demuestran
- `script02.js` -> Clase `Calculadora` y `CalcAvanzada` con herencia usando `extends`

---

## 8. El DOM (Document Object Model)

El DOM es la representacion en memoria de la pagina HTML como un arbol de objetos que JavaScript puede manipular.

### Seleccionar elementos

```javascript
// Por ID (retorna UN elemento o null)
const boton = document.getElementById("mi-boton");

// Por selector CSS (retorna el PRIMERO que coincida)
const boton = document.querySelector("#mi-boton");
const primer_p = document.querySelector("p");
const clase = document.querySelector(".mi-clase");

// Multiples elementos (retorna una coleccion)
const todos_p = document.querySelectorAll("p");
const clases = document.getElementsByClassName("mi-clase");
const divs = document.getElementsByTagName("div");
```

### Modificar contenido

```javascript
const elemento = document.getElementById("titulo");

// Texto plano (seguro contra XSS)
elemento.textContent = "Nuevo titulo";

// HTML (CUIDADO: vulnerable a XSS si el contenido viene del usuario)
elemento.innerHTML = "<strong>Nuevo</strong> titulo";

// Atributos
elemento.setAttribute("class", "destacado");
elemento.id = "nuevo-id";

// Estilos
elemento.style.color = "red";
elemento.style.fontSize = "20px";

// Clases CSS
elemento.classList.add("activo");
elemento.classList.remove("inactivo");
elemento.classList.toggle("visible");
```

### Crear y agregar elementos

```javascript
// Crear un nuevo elemento
const nuevo_p = document.createElement("p");
nuevo_p.textContent = "Parrafo nuevo";
nuevo_p.classList.add("destacado");

// Agregarlo al DOM
document.getElementById("contenedor").appendChild(nuevo_p);

// Alternativa: insertar HTML directamente
document.getElementById("contenedor").insertAdjacentHTML(
    "beforeend",
    "<p class='destacado'>Parrafo nuevo</p>"
);
```

### jQuery vs JavaScript nativo

```javascript
// JQUERY                              // JAVASCRIPT NATIVO
$('#id')                               document.getElementById('id')
$('.clase')                            document.querySelectorAll('.clase')
$('#id').html('<b>Hola</b>')           element.innerHTML = '<b>Hola</b>'
$('#id').text('Hola')                  element.textContent = 'Hola'
$('#id').append('<p>Nuevo</p>')        element.insertAdjacentHTML('beforeend', '<p>Nuevo</p>')
$('#id').empty()                       element.innerHTML = ''
$('#id').remove()                      element.remove()
$('#id').val()                         element.value
$('#id').css('color', 'red')           element.style.color = 'red'
$('#id').addClass('activo')            element.classList.add('activo')
```

### Archivos que lo demuestran
- `Eventos1/eventos.js` -> `document.getElementById()`, `.onclick`
- `PracticaFinalNat/js/index.js` -> `$('#peliculas')`, `.append()`, `.html()`, `.remove()`
- `PracticaFinalNat/js/buscar.js` -> `$('#miLista').empty()`, `.append()` con template literals

---

## 9. Eventos

Los eventos son acciones que ocurren en la pagina. JavaScript puede "escuchar" estos eventos y reaccionar a ellos.

### Tipos de eventos comunes

| Evento | Descripcion |
|---|---|
| `click` | Click del mouse |
| `dblclick` | Doble click |
| `mouseover` | Cursor entra al elemento |
| `mouseout` | Cursor sale del elemento |
| `keydown` | Tecla presionada |
| `keyup` | Tecla soltada |
| `submit` | Formulario enviado |
| `change` | Valor de input/select cambio |
| `input` | Texto en input cambio (tiempo real) |
| `focus` | Elemento recibio el foco |
| `blur` | Elemento perdio el foco |
| `DOMContentLoaded` | HTML cargado y parseado |
| `load` | Todo cargado (imagenes, CSS, etc.) |
| `scroll` | Se hizo scroll en la pagina |

### Asignar eventos

```javascript
// FORMA 1: addEventListener (RECOMENDADA)
// Permite multiples handlers para el mismo evento
boton.addEventListener("click", function(event) {
    console.log("Click!", event.target);
});

// FORMA 2: Propiedad on[evento]
// Solo permite UN handler por evento
boton.onclick = function() {
    console.log("Click!");
};

// FORMA 3: Atributo HTML (NO RECOMENDADA)
// <button onclick="miFuncion()">Click</button>
```

### El objeto Event

Cada handler recibe un objeto `event` con informacion del evento:

```javascript
boton.addEventListener("click", function(event) {
    event.target;          // El elemento que disparo el evento
    event.type;            // "click"
    event.clientX;         // Posicion X del mouse
    event.clientY;         // Posicion Y del mouse
    event.preventDefault(); // Evita el comportamiento por defecto
    event.stopPropagation(); // Detiene el bubbling
});
```

### Event Bubbling (burbujeo)

Cuando haces click en un elemento, el evento "sube" por el arbol del DOM:

```
click en <button>
  -> sube a <div>
    -> sube a <body>
      -> sube a <html>
        -> sube a document
```

Esto permite la **delegacion de eventos**: escuchar en un padre para manejar clicks en hijos dinamicos:

```javascript
// En vez de agregar un listener a cada boton:
document.getElementById("contenedor").addEventListener("click", function(event) {
    if (event.target.matches("button")) {
        console.log("Se hizo click en un boton:", event.target.textContent);
    }
});
```

### DOMContentLoaded

Espera a que el HTML se haya cargado antes de ejecutar JavaScript:

```javascript
document.addEventListener("DOMContentLoaded", function() {
    // Ahora es seguro buscar elementos en el DOM
    const boton = document.getElementById("mi-boton");
    boton.addEventListener("click", miFuncion);
});
```

### Archivos que lo demuestran
- `Eventos1/eventos.js` -> `DOMContentLoaded`, `.onclick`, `.onmouseover`
- `PracticaFinalNat/js/buscar.js` -> `.on("click", ...)` (jQuery)
- `PracticaFinalNat/js/catalogo.js` -> `.on("click", obtenerCatalogo)` funcion nombrada como callback
- `PracticaFinalNat/js/formulario.js` -> Intercepta `submit` via plugin de validacion

---

## 10. Fetch API y AJAX

AJAX (Asynchronous JavaScript And XML) permite hacer peticiones HTTP sin recargar la pagina.

### jQuery $.ajax() (usado en el proyecto)

```javascript
$.ajax({
    url: "https://api.ejemplo.com/datos",
    type: "GET",                    // GET, POST, PUT, DELETE
    dataType: "json",               // Tipo de respuesta esperada
    success: function(data) {       // Si la peticion fue exitosa
        console.log(data);
    },
    error: function(xhr, status) {  // Si hubo un error
        console.log("Error:", status);
    },
    beforeSend: function() {        // Antes de enviar
        console.log("Cargando...");
    }
});
```

### Fetch API (alternativa moderna, sin jQuery)

```javascript
// Forma basica con .then()
fetch("https://api.ejemplo.com/datos")
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP " + response.status);
        }
        return response.json();  // Parsear JSON
    })
    .then(data => {
        console.log(data);      // Usar los datos
    })
    .catch(error => {
        console.log("Error:", error);
    });

// Forma moderna con async/await
async function obtenerDatos() {
    try {
        const response = await fetch("https://api.ejemplo.com/datos");
        if (!response.ok) throw new Error("HTTP " + response.status);
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.log("Error:", error);
    }
}
```

### Promises (Promesas)

Una promesa representa un valor que **aun no esta disponible** pero lo estara en el futuro:

```javascript
// Una promesa tiene tres estados:
// 1. pending (pendiente): Aun no se resolvio
// 2. fulfilled (cumplida): Se resolvio exitosamente
// 3. rejected (rechazada): Hubo un error

const promesa = new Promise((resolve, reject) => {
    setTimeout(() => {
        const exito = true;
        if (exito) {
            resolve("Datos obtenidos!");
        } else {
            reject("Algo fallo");
        }
    }, 2000);
});

promesa
    .then(resultado => console.log(resultado))   // "Datos obtenidos!"
    .catch(error => console.log(error));
```

### Anatomia de una peticion HTTP

```
PETICION (Request):
  GET /3/movie/upcoming?api_key=xxx&language=es HTTP/1.1
  Host: api.themoviedb.org

RESPUESTA (Response):
  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    "page": 1,
    "results": [
      {
        "title": "Pelicula 1",
        "poster_path": "/abc.jpg",
        "overview": "Descripcion..."
      }
    ]
  }
```

### Archivos que lo demuestran
- `PracticaFinalNat/js/index.js` -> `$.ajax()` con callbacks success/error/beforeSend
- `PracticaFinalNat/js/buscar.js` -> `$.ajax()` con parametros dinamicos del usuario
- `PracticaFinalNat/js/catalogo.js` -> `$.ajax()` con setTimeout y animaciones

---

## 11. Patrones comunes en JavaScript

### Template literals para generar HTML

```javascript
// FORMA ANTIGUA (concatenacion con +): dificil de leer
var html = '<div class="card">'
    + '<h2>' + titulo + '</h2>'
    + '<p>' + descripcion + '</p>'
    + '</div>';

// FORMA MODERNA (template literals): legible y limpia
const html = `
    <div class="card">
        <h2>${titulo}</h2>
        <p>${descripcion}</p>
    </div>
`;
```

### Metodos de array para transformar datos

```javascript
const peliculas = respuesta.results;

// Generar HTML para cada pelicula
const htmlCards = peliculas.map(peli => `
    <div class="card">
        <img src="https://image.tmdb.org/t/p/w500${peli.poster_path}" />
        <h3>${peli.title}</h3>
    </div>
`).join('');  // .join('') une el array en un solo string

document.getElementById('contenedor').innerHTML = htmlCards;
```

### Desestructuracion (Destructuring)

```javascript
// Extraer propiedades de un objeto
const pelicula = { title: "Matrix", year: 1999, rating: 8.7 };
const { title, year, rating } = pelicula;
console.log(title);  // "Matrix"

// Extraer elementos de un array
const [primero, segundo, ...resto] = [1, 2, 3, 4, 5];
console.log(primero);  // 1
console.log(resto);    // [3, 4, 5]
```

### Operador spread/rest (...)

```javascript
// Spread: "esparcir" un array/objeto
const original = [1, 2, 3];
const copia = [...original, 4, 5];  // [1, 2, 3, 4, 5]

const persona = { nombre: "Ana", edad: 25 };
const actualizado = { ...persona, edad: 26 };  // { nombre: "Ana", edad: 26 }

// Rest: "recoger" parametros sobrantes
function sumarTodo(...numeros) {
    return numeros.reduce((a, b) => a + b, 0);
}
sumarTodo(1, 2, 3, 4);  // 10
```

### Optional chaining (?.)

```javascript
// Sin optional chaining:
const ciudad = usuario && usuario.direccion && usuario.direccion.ciudad;

// Con optional chaining (moderno):
const ciudad = usuario?.direccion?.ciudad;
// Si alguna propiedad es null/undefined, retorna undefined (sin error)
```

---

## 12. Manejo de errores

### try/catch

```javascript
try {
    // Codigo que podria fallar
    const data = JSON.parse(textoInvalido);
} catch (error) {
    // Se ejecuta si hay un error
    console.log("Error:", error.message);
} finally {
    // Se ejecuta SIEMPRE (haya error o no)
    console.log("Proceso terminado");
}
```

### try/catch con fetch

```javascript
async function obtenerPeliculas() {
    try {
        const response = await fetch("https://api.themoviedb.org/3/movie/upcoming");

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }

        const data = await response.json();
        mostrarPeliculas(data.results);

    } catch (error) {
        if (error instanceof TypeError) {
            console.log("Sin conexion a internet");
        } else {
            console.log("Error:", error.message);
        }
        mostrarMensajeError();
    }
}
```

### Errores comunes y como evitarlos

```javascript
// 1. TypeError: Cannot read properties of null
// CAUSA: getElementById retorna null si no encuentra el elemento
const boton = document.getElementById("no-existe");
boton.onclick = funcion;  // ERROR!
// SOLUCION: Verificar primero
if (boton) { boton.onclick = funcion; }

// 2. ReferenceError: variable is not defined
// CAUSA: La variable no fue declarada
console.log(noExiste);  // ERROR!
// SOLUCION: Siempre declarar con const/let

// 3. SyntaxError: Unexpected token
// CAUSA: Error de sintaxis (falta coma, llave, parentesis)
const obj = { nombre: "Ana" edad: 25 };  // Falta coma!
// SOLUCION: Revisar la sintaxis

// 4. Callback Hell (piramide de la muerte)
// CAUSA: Callbacks anidados
$.ajax({ success: function() {
    $.ajax({ success: function() {
        $.ajax({ success: function() {
            // ... infierno
        }});
    }});
}});
// SOLUCION: Usar async/await o Promises
```

---

## 13. Comparacion JavaScript vs Python

Para los estudiantes que vienen del modulo 11 (Python), esta tabla ayuda a ver las equivalencias:

### Sintaxis basica

| Concepto | Python | JavaScript |
|---|---|---|
| Variable | `x = 5` | `const x = 5;` o `let x = 5;` |
| Imprimir | `print("hola")` | `console.log("hola");` |
| Comentario | `# comentario` | `// comentario` |
| Comentario multi | `""" texto """` | `/* texto */` |
| String format | `f"Hola {nombre}"` | `` `Hola ${nombre}` `` |
| Nulo | `None` | `null` / `undefined` |
| Booleanos | `True`, `False` | `true`, `false` |
| Bloque de codigo | Indentacion | Llaves `{ }` |
| Fin de linea | Nueva linea | `;` (opcional pero recomendado) |

### Estructuras de datos

| Concepto | Python | JavaScript |
|---|---|---|
| Lista/Array | `[1, 2, 3]` | `[1, 2, 3]` |
| Diccionario/Objeto | `{"a": 1, "b": 2}` | `{a: 1, b: 2}` |
| Tupla | `(1, 2, 3)` | No existe (usar Object.freeze) |
| Set | `{1, 2, 3}` | `new Set([1, 2, 3])` |
| Longitud | `len(lista)` | `lista.length` |
| Agregar | `lista.append(4)` | `lista.push(4)` |
| Rebanar | `lista[1:3]` | `lista.slice(1, 3)` |

### Funciones

| Concepto | Python | JavaScript |
|---|---|---|
| Funcion | `def sumar(a, b):` | `function sumar(a, b) { }` |
| Lambda | `lambda x: x * 2` | `x => x * 2` |
| Retorno | `return valor` | `return valor;` |
| Argumentos default | `def f(x=5):` | `function f(x = 5) { }` |
| Args variables | `def f(*args):` | `function f(...args) { }` |

### Clases

| Concepto | Python | JavaScript |
|---|---|---|
| Definir clase | `class Animal:` | `class Animal { }` |
| Constructor | `def __init__(self, nombre):` | `constructor(nombre) { }` |
| Self/This | `self.nombre = nombre` | `this.nombre = nombre;` |
| Herencia | `class Perro(Animal):` | `class Perro extends Animal { }` |
| Super | `super().__init__(nombre)` | `super(nombre);` |
| Instancia | `perro = Animal("Rex")` | `const perro = new Animal("Rex");` |

### Bucles

| Concepto | Python | JavaScript |
|---|---|---|
| For clasico | `for i in range(10):` | `for (let i = 0; i < 10; i++)` |
| For each | `for item in lista:` | `for (const item of lista)` |
| While | `while x < 10:` | `while (x < 10) { }` |
| List comprehension | `[x*2 for x in lista]` | `lista.map(x => x * 2)` |
| Filtrar | `[x for x in l if x > 0]` | `l.filter(x => x > 0)` |

### Asincronia

| Concepto | Python | JavaScript |
|---|---|---|
| HTTP GET | `requests.get(url)` | `fetch(url)` o `$.ajax()` |
| JSON parse | `response.json()` | `response.json()` o `JSON.parse()` |
| Async/Await | `async def f():` | `async function f() { }` |
| Await | `await asyncio.sleep(1)` | `await fetch(url)` |
| Ejecucion | Sincrono por defecto | Asincrono por defecto |

### Diferencia fundamental

```
Python: Sincrono por defecto. El codigo se ejecuta linea por linea.
        Para asincronia se necesita asyncio explicitamente.

JavaScript: Asincrono por defecto. Las operaciones de I/O (red, archivos)
            NO bloquean la ejecucion. Se usan callbacks, promesas o
            async/await para manejar los resultados.
```

---

## 14. Mapa de archivos del modulo

```
12-javascript-fundamentos/
|
|-- CONCEPTOS.md              <- Este archivo
|
|-- script00.js               <- BASICO: Bucles for/while, console.log
|-- script01.js               <- BASICO: Funciones (tradicional, flecha, anonima)
|-- script02.js               <- INTERMEDIO: Clases, herencia, metodos
|
|-- Eventos1/
|   |-- eventos.html          <- INTERMEDIO: HTML con boton e imagen
|   |-- eventos.js            <- INTERMEDIO: Eventos DOM, DOMContentLoaded
|
|-- PracticaFinalNat/          <- AVANZADO: Proyecto completo con API
    |-- index.html             <- Pagina principal (peliculas proximas)
    |-- buscar.html            <- Pagina de busqueda
    |-- catalogo.html          <- Pagina de catalogo
    |-- formulario.html        <- Pagina de registro
    |-- js/
    |   |-- index.js           <- AJAX, generacion de cards, callbacks
    |   |-- buscar.js          <- Busqueda con API, validacion, template literals
    |   |-- catalogo.js        <- Catalogo, modales, closures, animaciones
    |   |-- formulario.js      <- Validacion de formularios con plugin
    |   |-- offcanvas.js       <- Menu lateral (Bootstrap)
    |-- css/
    |   |-- estilo.css         <- Estilos personalizados, selectores, sombras
    |   |-- offcanvas.css      <- Estilos del menu lateral
    |-- images/                <- Imagenes del proyecto
```

### Progresion pedagogica

```
BASICO (script00, script01)
  -> Variables, bucles, funciones, console.log
  -> Se ejecutan en terminal con Node.js

INTERMEDIO (script02, Eventos1)
  -> Clases, herencia, DOM, eventos
  -> Se conecta JavaScript con HTML

AVANZADO (PracticaFinalNat)
  -> API externa, AJAX, JSON, HTML dinamico
  -> Proyecto completo con multiples paginas
  -> Patrones del mundo real
```

---

## 15. Ejercicios de practica

### Nivel basico

**Ejercicio 1: Variables y tipos**
Crea un script que declare variables de cada tipo (string, number, boolean, array, object)
e imprima su tipo con `typeof`.

**Ejercicio 2: Bucles**
Escribe un programa que imprima los numeros del 1 al 100 pero:
- Para multiplos de 3, imprime "Fizz"
- Para multiplos de 5, imprime "Buzz"
- Para multiplos de ambos, imprime "FizzBuzz"

**Ejercicio 3: Funciones**
Crea tres versiones de una funcion que calcule el factorial de un numero:
una tradicional, una flecha y una anonima.

### Nivel intermedio

**Ejercicio 4: Clases**
Crea una clase `Vehiculo` con propiedades (marca, modelo, anio) y un metodo `descripcion()`.
Luego crea una clase `Auto` que herede de `Vehiculo` y agregue la propiedad `puertas`.

**Ejercicio 5: DOM**
Crea una pagina HTML con un input, un boton y una lista `<ul>`. Al hacer click en el boton,
el texto del input se agrega como un nuevo `<li>` a la lista.

**Ejercicio 6: Eventos**
Crea una pagina con un cuadrado de color. Al hacer click, cambia a un color aleatorio.
Al pasar el mouse, muestra las coordenadas. Al presionar una tecla, cambia de tamano.

### Nivel avanzado

**Ejercicio 7: Fetch API**
Usa la API de JSONPlaceholder (https://jsonplaceholder.typicode.com/users) para:
1. Obtener la lista de usuarios
2. Mostrarlos en tarjetas HTML
3. Agregar un buscador que filtre por nombre

**Ejercicio 8: Formulario con validacion**
Crea un formulario de contacto con validacion JavaScript pura (sin plugins):
- Nombre: obligatorio, minimo 3 caracteres
- Email: obligatorio, formato valido
- Mensaje: obligatorio, minimo 10 caracteres
- Muestra errores debajo de cada campo en rojo

**Ejercicio 9: Aplicacion CRUD**
Crea una lista de tareas (todo list) que permita:
- Agregar tareas
- Marcar como completadas
- Eliminar tareas
- Filtrar por estado (todas, activas, completadas)
- Guardar en localStorage para que persistan al recargar

**Ejercicio 10: Reescribir el proyecto**
Toma el proyecto PracticaFinalNat y reescribelo usando:
- `fetch()` en vez de `$.ajax()`
- `async/await` en vez de callbacks
- Template literals en vez de concatenacion con +
- `const/let` en vez de `var`
- JavaScript nativo en vez de jQuery

---

## Recursos adicionales

- [MDN Web Docs - JavaScript](https://developer.mozilla.org/es/docs/Web/JavaScript) - Referencia oficial
- [JavaScript.info](https://javascript.info/) - Tutorial completo y moderno
- [API de TMDB](https://developer.themoviedb.org/docs) - Documentacion de la API usada en el proyecto
- [Can I Use](https://caniuse.com/) - Compatibilidad de funciones con navegadores
- [JSONPlaceholder](https://jsonplaceholder.typicode.com/) - API de prueba gratuita para practicar
