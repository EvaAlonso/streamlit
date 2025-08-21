
# Graficas de barras
 1. Veamos de la documentación de streamlit st.bar_chart
# st.bar_chart

Es un atajo rápido de Streamlit, se usa cuando quieres graficar algo sencillo sin mucho código.Le pasas un DataFrame o una lista y te saca la barra automáticamente.
Su ventaja es que es muy rápido e ideal para prototipos, pero tiene en contra que es muy poco personalizable (colores, ejes, estilos limitados)

st.bar_chart(data=None, *, x=None, y=None, x_label=None, y_label=None, color=None, horizontal=False, stack=None, width=None, height=None, use_container_width=True)

## data
cualquier cosa compatible con st.dataframe. Serán tus datos a graficar

## x (string o none)
Nombre o clave de la columna asociada a los datos del eje x. Si x es Ninguno (predeterminado), Streamlit utiliza el índice de datos para los valores del eje x.

## y (string, secuencia de strings, o ninguno)
Nombre(s) de columna o clave(s) asociada(s) a los datos del eje Y. Si se establece en " Ninguno " (predeterminado), Streamlit representa los datos de todas las columnas restantes como series de datos. Si se establece en " Secuencia de cadenas", Streamlit representa varias series en el mismo gráfico fusionando la tabla de formato ancho en una tabla de formato largo.

## x_label (string o ninguno)
La etiqueta del eje x. Si se establece en "Ninguno " (predeterminado), Streamlit usará el nombre de la columna especificado en "x" si está disponible; de ​​lo contrario, no se mostrará ninguna etiqueta.

## y_label (string o ninguno)
La etiqueta del eje y. Si se establece en "Ninguno " (predeterminado), Streamlit usará el nombre de la columna especificada en "y " si está disponible; de ​​lo contrario, no se mostrará ninguna etiqueta.

## color (string, tupla, secuencia de strings, secuencia de tupla o ninguna)
El color a utilizar para las diferentes series en este gráfico.

Para un gráfico de barras con solo una serie, esto puede ser:

Ninguno, para utilizar el color predeterminado.
Una cadena hexadecimal como "#ffaa00" o "#ffaa0088".
Una tupla RGB o RGBA con los componentes rojo, verde, azul y alfa especificados como números enteros de 0 a 255 o números flotantes de 0,0 a 1,0.
Para un gráfico de barras con múltiples series, donde el marco de datos está en formato largo (es decir, y es Ninguno o solo una columna), esto puede ser:

Ninguno, para utilizar los colores predeterminados.

El nombre de una columna del conjunto de datos. Los puntos de datos se agruparán en series del mismo color según el valor de esta columna. Además, si los valores de esta columna coinciden con uno de los formatos de color anteriores (cadena hexadecimal o tupla de color), se utilizará ese color.

Por ejemplo: si el conjunto de datos tiene 1000 filas, pero esta columna solo contiene los valores "adulto", "niño" y "bebé", entonces esos 1000 puntos de datos se agruparán en tres series cuyos colores se seleccionarán automáticamente de la paleta predeterminada.

Pero, si para el mismo conjunto de datos de 1000 filas, esta columna contuviera los valores "#ffaa00", "#f0f", "#0000ff", entonces esos 1000 puntos de datos todavía estarían agrupados en 3 series, pero sus colores serían "#ffaa00", "#f0f", "#0000ff" esta vez.

Para un gráfico de barras con múltiples series, donde el marco de datos está en formato ancho (es decir, y es una secuencia de columnas), esto puede ser:

Ninguno, para utilizar los colores predeterminados.
Una lista de colores de cadena o tuplas de colores que se usarán para cada serie del gráfico. Esta lista debe tener la misma longitud que el número de valores y (p. ej., color=["#fd0", "#f0f", "#04f"] para tres líneas).
Puede configurar los colores predeterminados en la opción de configuración theme.chartCategoryColors .

## horizontal (bool)
Si se apilan las barras. Si es Ninguno (predeterminado), Streamlit usa el valor predeterminado de Vega. Otros valores pueden ser los siguientes:

Verdadero : las barras forman una pila aditiva sin superposición dentro del gráfico.
Falso : Las barras se muestran una al lado de la otra.
"en capas" : las barras se superponen entre sí sin apilarse.
"normalizar" : las barras se apilan y la altura total se normaliza al 100% de la altura del gráfico.
"centro" : las barras se apilan y se desplazan para centrar la altura total alrededor de un eje.

## stack (bool, "normalize", "center", "layered", or None)
Si se apilan las barras. Si es Ninguno (predeterminado), Streamlit usa el valor predeterminado de Vega. Otros valores pueden ser los siguientes:

Verdadero : las barras forman una pila aditiva sin superposición dentro del gráfico.
Falso : Las barras se muestran una al lado de la otra.
layered "en capas" : las barras se superponen entre sí sin apilarse.
normalize "normalizar" : las barras se apilan y la altura total se normaliza al 100% de la altura del gráfico.
center "centro" : las barras se apilan y se desplazan para centrar la altura total alrededor de un eje.

## width (int o none)

Ancho deseado del gráfico, expresado en píxeles. Si el ancho es Ninguno (predeterminado), Streamlit ajusta el ancho del gráfico para que se ajuste a su contenido según la biblioteca de gráficos, hasta el ancho del contenedor principal. Si el ancho es mayor que el ancho del contenedor principal, Streamlit ajusta el ancho del gráfico para que coincida con el ancho del contenedor principal.

Para utilizar ancho , debes establecer use_container_width=False .

## height (int o none)
Altura deseada del gráfico, expresada en píxeles. Si la altura es Ninguna (predeterminada), Streamlit la ajusta para que se ajuste a su contenido según la biblioteca de gráficos.

## use_container_width (bool)
Si se debe sobrescribir el ancho con el ancho del contenedor principal. Si `use_container_width` es `true` (valor predeterminado), Streamlit establece el ancho del gráfico para que coincida con el ancho del contenedor principal. Si ` use_container_width` es `false` , Streamlit establece el ancho del gráfico según `width` .

### ver ejemplos y caso de añadir más datos en https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart

# st.altair_chart
## puedes usar st.altair_chart https://docs.streamlit.io/develop/api-reference/charts/st.altair_chart

Aquí se le pasa un objeto de Altair y te da acceso a toda la API de Altair que es mucho más flexible
Necesitas construir la gráfica antes y luego mostrarla con st.altair_chart
Tiene la ventaja de que es mucho más personalizable pero necesitas más código y aprender Altair https://altair-viz.github.io/user_guide/marks/bar.html
