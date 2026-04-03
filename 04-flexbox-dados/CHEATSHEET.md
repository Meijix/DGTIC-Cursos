# Cheatsheet — Modulo 04: Flexbox

## Modelo mental: Container vs Items

```
  .padre { display: flex; }       <-- CONTENEDOR (propiedades del padre)
  |
  +-- .hijo-1                     <-- ITEM flex (hijo directo)
  +-- .hijo-2                     <-- ITEM flex (hijo directo)
  +-- .hijo-3                     <-- ITEM flex (hijo directo)

  SOLO los hijos directos son items flex. Los nietos NO.
```

## Ejes: Main Axis vs Cross Axis

```
  flex-direction: row (defecto)         flex-direction: column

  MAIN AXIS (horizontal)                CROSS AXIS (horizontal)
  ───────────────────────►              ───────────────────────►

  | +------+ +------+ +------+         | +---------------------+
  | | A    | | B    | | C    |         | |         A           |
  | +------+ +------+ +------+         | +---------------------+
  |                                     | +---------------------+
  v CROSS AXIS (vertical)              | |         B           |
                                        | +---------------------+
  justify-content = horizontal          v MAIN AXIS (vertical)
  align-items     = vertical
                                        justify-content = vertical
                                        align-items     = horizontal
```

## Referencia rapida: propiedades del CONTENEDOR

| Propiedad         | Valores principales                       | Efecto                            |
|--------------------|-------------------------------------------|-----------------------------------|
| `display`          | `flex`, `inline-flex`                     | Activa Flexbox                    |
| `flex-direction`   | `row`, `row-reverse`, `column`, `column-reverse` | Direccion del eje principal |
| `flex-wrap`        | `nowrap`, `wrap`, `wrap-reverse`          | Permite saltos de linea           |
| `justify-content`  | `flex-start`, `center`, `flex-end`, `space-between`, `space-around`, `space-evenly` | Distribuye en eje principal |
| `align-items`      | `stretch`, `flex-start`, `center`, `flex-end`, `baseline` | Alinea en eje cruzado |
| `align-content`    | Igual que justify-content                 | Distribuye lineas (solo con wrap) |
| `gap`              | `10px`, `10px 20px`                       | Espacio ENTRE items               |

## Referencia rapida: propiedades de cada ITEM

| Propiedad     | Defecto | Efecto                                       |
|---------------|---------|----------------------------------------------|
| `flex-grow`   | `0`     | Cuanto espacio sobrante absorbe (0 = no crece)|
| `flex-shrink` | `1`     | Cuanto se encoge si falta espacio             |
| `flex-basis`  | `auto`  | Tamano inicial antes de grow/shrink           |
| `flex`        | —       | Shorthand: `flex: 1` = `1 1 0%`              |
| `align-self`  | `auto`  | Sobreescribe align-items para ESTE item       |
| `order`       | `0`     | Cambia orden visual sin tocar HTML            |

## justify-content visual

```
  flex-start:     |[A] [B] [C]                    |
  flex-end:       |                    [A] [B] [C]|
  center:         |         [A] [B] [C]           |
  space-between:  |[A]         [B]         [C]    |  bordes = 0
  space-around:   |  [A]     [B]     [C]  |         bordes = 1/2
  space-evenly:   |   [A]   [B]   [C]   |           bordes = iguales
```

## El shorthand flex

```
  flex: <grow> <shrink> <basis>

  flex: 1;         -->  flex: 1 1 0%      (crece y se encoge, base 0)
  flex: auto;      -->  flex: 1 1 auto    (crece y se encoge, base auto)
  flex: none;      -->  flex: 0 0 auto    (tamano fijo, no se adapta)
  flex: 0 0 200px; -->  exactamente 200px, no crece ni encoge
```

## Ejemplo rapido: centrar un elemento

```css
.contenedor {
    display: flex;
    justify-content: center;  /* centra horizontal */
    align-items: center;      /* centra vertical */
    height: 100vh;
}
```

## Errores comunes

| Error | Problema | Solucion |
|-------|----------|----------|
| Poner `justify-content` en el item | No tiene efecto | Ponerlo en el **contenedor** (padre) |
| Olvidar `display: flex` | Los hijos no se alinean | Siempre declarar `display: flex` en el padre |
| Esperar layout 2D con Flexbox | Flexbox es 1 dimension | Usar CSS Grid para filas Y columnas |
| Usar `margin` para separar items | Margenes dobles entre items | Usar `gap` en el contenedor |
| `align-items` sin altura en el padre | No se ve efecto vertical | Darle `height` o `min-height` al contenedor |
| Confundir `flex-basis` con `width` | Comportamiento distinto en column | `flex-basis` respeta el eje del flex |
| Olvidar `flex-wrap: wrap` | Items se comprimen en 1 linea | Agregar `wrap` si necesitas multi-linea |
