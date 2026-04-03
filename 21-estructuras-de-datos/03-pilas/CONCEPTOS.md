# Pilas (Stacks)

## Que es

Una **pila** (stack) es una estructura de datos lineal que sigue el principio **LIFO** (Last In, First Out): el ultimo elemento en entrar es el primero en salir. Imagina una pila de platos: solo puedes poner o quitar platos por arriba.

## Diagrama

### Estructura basica

```
        ┌───────┐
        │  40   │  ← tope (top) - ultimo en entrar, primero en salir
        ├───────┤
        │  30   │
        ├───────┤
        │  20   │
        ├───────┤
        │  10   │  ← fondo (base)
        └───────┘
```

### Operacion push (apilar)

```
push(50):
                    ┌───────┐
                    │  50   │ ← nuevo tope
        ┌───────┐  ├───────┤
        │  40   │  │  40   │
        ├───────┤  ├───────┤
        │  30   │  │  30   │
        ├───────┤  ├───────┤
        │  20   │  │  20   │
        └───────┘  └───────┘
         Antes      Despues
```

### Operacion pop (desapilar)

```
pop() → retorna 40:

        ┌───────┐
        │  40   │ ← se extrae     ┌───────┐
        ├───────┤                  │  30   │ ← nuevo tope
        │  30   │                  ├───────┤
        ├───────┤                  │  20   │
        │  20   │                  └───────┘
        └───────┘
         Antes                      Despues
```

## Operaciones principales

| Operacion | Complejidad | Descripcion                              |
|-----------|-------------|------------------------------------------|
| push(x)   | O(1)        | Agregar elemento al tope                 |
| pop()     | O(1)        | Remover y retornar el elemento del tope  |
| peek/top()| O(1)        | Ver el elemento del tope sin removerlo   |
| is_empty()| O(1)        | Verificar si la pila esta vacia          |
| size()    | O(1)        | Obtener el numero de elementos           |

## Como funciona

### Call Stack (pila de llamadas)

El uso mas fundamental de una pila es la **pila de llamadas** del sistema operativo:

```
def main():
    resultado = calcular(5)

def calcular(n):
    return factorial(n)

def factorial(n):
    if n <= 1: return 1
    return n * factorial(n-1)

Pila de llamadas durante la ejecucion:

        ┌──────────────┐
        │ factorial(1)  │  ← retorna 1
        ├──────────────┤
        │ factorial(2)  │  ← retorna 2*1
        ├──────────────┤
        │ factorial(3)  │  ← retorna 3*2
        ├──────────────┤
        │ factorial(4)  │  ← retorna 4*6
        ├──────────────┤
        │ factorial(5)  │  ← retorna 5*24
        ├──────────────┤
        │ calcular(5)   │
        ├──────────────┤
        │ main()        │
        └──────────────┘
```

### Verificacion de parentesis balanceados

```
Expresion: "({[]})"

Paso 1: '(' → push   Pila: [(]
Paso 2: '{' → push   Pila: [(, {]
Paso 3: '[' → push   Pila: [(, {, []
Paso 4: ']' → pop '[' ← coincide con ']'  Pila: [(, {]
Paso 5: '}' → pop '{' ← coincide con '}'  Pila: [(]
Paso 6: ')' → pop '(' ← coincide con ')'  Pila: []

Pila vacia al final → parentesis balanceados ✓
```

### Operacion Undo/Redo

```
Acciones del usuario:           Pila Undo        Pila Redo

1. Escribir "Hola"             [Hola]            []
2. Escribir " mundo"           [Hola, mundo]     []
3. Undo                        [Hola]            [mundo]
4. Undo                        []                [mundo, Hola]
5. Redo                        [Hola]            [mundo]
```

## Cuando usarla

**Usar pilas cuando:**
- Necesitas revertir un orden (invertir cadenas, Undo)
- Hay operaciones anidadas (parentesis, HTML tags)
- Implementas recorridos en profundidad (DFS)
- Necesitas convertir recursion a iteracion
- Evaluas expresiones aritmeticas (notacion postfija)

**NO usar pilas cuando:**
- Necesitas acceso a elementos que no estan en el tope
- Necesitas procesamiento en orden de llegada (usar cola)
- Necesitas busqueda eficiente (usar tabla hash o arbol)

## Casos de uso en el mundo real

- **Navegador web**: boton "atras" (pila de paginas visitadas)
- **Editores de texto**: Ctrl+Z (deshacer)
- **Compiladores**: analisis sintactico y evaluacion de expresiones
- **Algoritmos**: DFS, backtracking, Torres de Hanoi
- **Gestion de memoria**: call stack de cada hilo de ejecucion

## Errores comunes

1. **Stack overflow**: recursion infinita o muy profunda que desborda la pila del sistema.
2. **Pop en pila vacia**: siempre verificar `is_empty()` antes de hacer `pop()`.
3. **Confundir LIFO con FIFO**: si necesitas orden de llegada, usa una cola, no una pila.
4. **No limpiar la pila**: en verificacion de parentesis, al terminar de recorrer la cadena hay que verificar que la pila quede vacia.
5. **Usar lista como pila con operaciones incorrectas**: en Python, usar `append()` y `pop()` (final), nunca `insert(0)` y `pop(0)` (eso es una cola ineficiente).
