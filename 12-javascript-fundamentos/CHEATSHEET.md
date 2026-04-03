# Cheatsheet — JavaScript Fundamentos

## Variables

| Palabra clave | Reasignable | Scope    | Usar cuando...            |
|---------------|-------------|----------|---------------------------|
| `const`       | No          | Bloque   | Por defecto (siempre)     |
| `let`         | Si          | Bloque   | El valor va a cambiar     |
| `var`         | Si          | Funcion  | **Nunca** (legacy)        |

## Tipos de datos

| Tipo        | Ejemplo                        | typeof          |
|-------------|--------------------------------|-----------------|
| string      | `"Hola"`, `` `Hola ${x}` ``   | `"string"`      |
| number      | `42`, `3.14`, `NaN`            | `"number"`      |
| boolean     | `true`, `false`                | `"boolean"`     |
| undefined   | `let x;`                       | `"undefined"`   |
| null        | `null`                         | `"object"` (!)  |
| object      | `{ a: 1 }`, `[1,2]`           | `"object"`      |
| function    | `() => {}`                     | `"function"`    |

**Falsy:** `false`, `0`, `""`, `null`, `undefined`, `NaN`. Todo lo demas es truthy.

## Operadores

```
===  comparacion estricta (valor + tipo)  SIEMPRE usar este
==   comparacion debil (convierte tipos)  EVITAR
!==  diferente estricto
&&   AND logico       ||   OR logico       !   NOT
??   nullish coalescing (null/undefined)   ?.  optional chaining
```

## Funciones

```javascript
// Declaracion clasica
function sumar(a, b) { return a + b; }

// Arrow function
const sumar = (a, b) => a + b;

// Callback: funcion como argumento
boton.addEventListener("click", () => { /* ... */ });
```

## Destructuring y template literals

```javascript
const { nombre, edad } = persona;       // objetos
const [primero, ...resto] = arreglo;    // arrays
const msg = `Hola ${nombre}, edad: ${edad}`;  // template literal
```

## Arrays — metodos clave

```javascript
arr.map(x => x * 2)          // transforma cada elemento -> nuevo array
arr.filter(x => x > 3)       // filtra por condicion     -> nuevo array
arr.reduce((acc, x) => acc + x, 0) // acumula en un valor
arr.find(x => x > 3)         // primer elemento que cumple condicion
arr.forEach(x => console.log(x))   // recorre (sin retornar)
arr.push(val)                 // agrega al final
arr.includes(val)             // retorna true/false
```

## Objetos

```javascript
const persona = { nombre: "Ana", edad: 20 };
persona.nombre          // acceso con punto
persona["edad"]         // acceso con corchetes
Object.keys(persona)    // ["nombre", "edad"]
Object.values(persona)  // ["Ana", 20]
{ ...persona, rol: "admin" }  // spread: copia + agrega
```

## Clases (ES6)

```javascript
class Animal {
    constructor(nombre) { this.nombre = nombre; }
    hablar() { return `${this.nombre} dice algo`; }
}
class Perro extends Animal {
    constructor(nombre, raza) {
        super(nombre);  // llama al constructor padre
        this.raza = raza;
    }
}
```

## DOM — referencia rapida

```javascript
document.querySelector("#id")         // seleccionar uno
document.querySelectorAll(".clase")   // seleccionar varios
document.createElement("div")        // crear elemento
padre.appendChild(hijo)              // agregar al DOM
el.textContent = "texto"             // texto seguro
el.innerHTML = "<b>html</b>"         // HTML (cuidado XSS)
el.classList.add("activo")           // agregar clase CSS
el.classList.toggle("visible")       // alternar clase CSS
el.setAttribute("src", "img.png")   // cambiar atributo
```

## Eventos

```javascript
el.addEventListener("click", (event) => {
    event.target              // elemento que disparo el evento
    event.preventDefault()    // cancela comportamiento por defecto
});
// Esperar a que el DOM cargue:
document.addEventListener("DOMContentLoaded", () => { /* ... */ });
```

Eventos comunes: `click`, `submit`, `input`, `change`, `keydown`, `mouseover`, `DOMContentLoaded`

## Fetch / async-await

```javascript
// Con async/await (moderno)
async function obtenerDatos() {
    try {
        const res = await fetch("https://api.ejemplo.com/datos");
        if (!res.ok) throw new Error("HTTP " + res.status);
        const data = await res.json();
        console.log(data);
    } catch (err) {
        console.error("Error:", err);
    }
}

// Con .then()
fetch(url)
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
```

## Errores comunes

| Error                            | Causa                                      | Solucion                            |
|----------------------------------|--------------------------------------------|-------------------------------------|
| `5 + "3"` da `"53"`             | `+` concatena si hay string                | Convertir: `Number("3")` o `+"3"`  |
| `== true` da resultados raros   | Comparacion debil convierte tipos           | Usar siempre `===`                  |
| `Cannot read property of null`  | `querySelector` no encontro el elemento     | Verificar que el ID/clase exista    |
| Script no encuentra elementos   | JS se ejecuta antes de que cargue el DOM    | Usar `DOMContentLoaded` o `defer`   |
| `this` es `undefined`           | Arrow function no tiene su propio `this`    | Usar function clasica en metodos    |
| Array original se modifica      | `push/splice` mutan; `map/filter` no mutan  | Elegir el metodo segun la necesidad |
