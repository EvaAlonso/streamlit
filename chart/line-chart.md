# st.line_chart
https://docs.streamlit.io/develop/api-reference/charts/st.line_chart

🎨 Personalización:

Limitada. Está pensada para mostrar datos rápido.

No puedes controlar colores, leyendas, tooltips, estilos, títulos, ni interactividad avanzada.

No puedes combinar varios gráficos ni ajustar escalas.

✅ ¿Cuándo usarlo?

Cuando quieres una visualización rápida.

Para prototipos, dashboards simples o exploración rápida de datos.

# st.altair_chart


| Personalizable                 | ¿Se puede? | Ejemplo                                   |
| ------------------------------ | ---------- | ----------------------------------------- |
| Títulos                        | ✅          | `.properties(title="Mi título")`          |
| Ejes                           | ✅          | `.configure_axis(labelFontSize=12)`       |
| Colores                        | ✅          | `.mark_line(color="green")`               |
| Tooltips                       | ✅          | `.encode(tooltip=["col1", "col2"])`       |
| Leyendas                       | ✅          | `.configure_legend(position='top-right')` |
| Interactividad (zoom, filtros) | ✅          | `.interactive()`, `selection`, etc.       |
| Capas / combinaciones          | ✅          | `.layer()`, `.concat()`                   |
| Filtros por selección          | ✅          | `.transform_filter()`                     |
| Gráficos múltiples             | ✅          | `.facet()` o `.repeat()`                  |

ver más en la documentacion de Vega-Altair https://altair-viz.github.io/user_guide/marks/line.html