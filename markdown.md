# Esto es un encabezado <h1> de primer nivel
## Esto es un encabezado <h2> de segundo nivel

***
---
___

Esto es un **texto en negrita**.
Esto es un texto parcialmente en ne**gri**ta.

Esto es un __texto en negrita__.
Esto es un texto parcialmente en ne__gri__ta.

Esto es un *texto en cursiva*.
Esto es un texto parcialmente en cu*rsi*va.

Esto es un _texto en cursiva_.
Esto es un texto parcialmente en cu_rsi_va.

Esto es un ***texto en negrita y cursiva***.
Esto es un ___texto en negrita y cursiva___.
Esto es un texto parcialmente en ne***grita y cursi***va.
Esto es un texto parcialmente en ne___grita y cursi___va.

Esto es un __*texto en negrita y cursiva*__.
Esto es un **_texto en negrita y cursiva_**.
Esto es un texto parcialmente en ne__*grita y cursi*__va.
Esto es un texto parcialmente en ne**_grita y cursi_**va.

Cambia de directorio con el comando `cd`
``let str = `texto de la cadena`;``

Me gusta el editor [Editor Markdown](https://editormarkdown.com)

Enlace a la sección [Encabezados](#encabezados)
# 📄 Markdown Cheatsheet Completo

## 🔤 Encabezados

```markdown
# Título H1
## Título H2
### Título H3
#### Título H4
##### Título H5
###### Título H6

✍️ Estilos de texto

Texto *cursiva*
Texto _cursiva_
Texto **negrita**
Texto __negrita__
Texto ***negrita y cursiva***
Texto ~~tachado~~
Texto `código inline`

📦 Citas

> Esto es una cita
>> Cita anidada

📋 Listas
✅ Listas con viñetas

- Ítem 1
- Ítem 2
  - Subítem
    - Sub-subítem
* También se puede usar asterisco

🔢 Listas numeradas

1. Primer ítem
2. Segundo ítem
   1. Subítem

✅ Tareas o checklists

- [x] Tarea completada
- [ ] Tarea pendiente

🔗 Enlaces

[Texto del enlace](https://www.ejemplo.com)

[Enlace con título](https://www.ejemplo.com "Título al pasar el mouse")

🖼️ Imágenes

![Texto alternativo](https://www.ejemplo.com/imagen.png)

![Imagen con título](https://www.ejemplo.com/imagen.png "Título al pasar el mouse")

👨‍💻 Código
Inline

Esto es `código inline`

Bloques de código

```python
def hola():
    print("Hola mundo")

echo "Hola desde la terminal"

console.log("Hola JS");


---

## 📊 Tablas

```markdown
| Nombre  | Edad | País     |
|---------|------|----------|
| Ana     | 23   | España   |
| Juan    | 34   | México   |
| Sakura  | 29   | Japón    |

Alineación:

| Izquierda | Centro | Derecha |
|:----------|:------:|--------:|
| texto     | texto  | texto   |

🔁 Saltos de línea

    Dos espacios al final de línea → salto de línea

    Línea en blanco entre párrafos → nuevo párrafo

🧱 Separador horizontal

---
***
___

🧩 HTML en Markdown

<b>Negrita en HTML</b>
<i>Cursiva</i>
<sub>Subíndice</sub>
<sup>Superíndice</sup>
<br>
<p>párrafo</p>

📚 Referencias de enlace

[Google][1]
[OpenAI][2]

[1]: https://www.google.com
[2]: https://www.openai.com

🔒 Escapar caracteres especiales

\*no es cursiva\*
\# no es encabezado

📎 Colapsar secciones

<details>
<summary>Haz clic para ver más</summary>

Contenido oculto aquí...

</details>