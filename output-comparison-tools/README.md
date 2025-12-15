# Output Comparison Tools

Esta carpeta contiene herramientas para analizar y comparar el desempeño de ambas soluciones del proyecto.

## Contenido

- **`benchmark.py`**: Script para medir tiempos de ejecución de ambas soluciones con diferentes tamaños de entrada.
- **`generate_graphs.py`**: Script para generar gráficos comparativos basados en los resultados del benchmark.
- **`benchmark_results.csv`**: Resultados del benchmark (tiempos de ejecución para cada tamaño de entrada).
- **Gráficos PNG**: Visualizaciones generadas a partir de los resultados.

---

## Cómo usar

### 1. Ejecutar el Benchmark

Para medir los tiempos de ejecución de ambas soluciones:

```bash
cd ADA-Project/output-comparison-tools
python [benchmark.py](http://_vscodecontentref_/6)
```
Nota: El archivo benchmark_results.csv actual contiene los resultados oficiales utilizados en el informe. Si deseas preservarlos, haz una copia de seguridad antes de ejecutar el script.

### 2. Generar Gráficos

Para generar los gráficos comparativos a partir de los resultados del benchmark:

```bash
cd ADA-Project/output-comparison-tools
python generate_graphs.py
```

#### Advertencia
Este script generará/sobreescribirá los siguientes archivos:

- grafico_comparacion.png
- grafico_complejidad_teorica.png
- grafico_diferencia.png

Si deseas preservar los gráficos originales, haz una copia de seguridad antes de ejecutar el script.

### Requisitos
- Bibliotecas requeridas:

```bash
pip install matplotlib
```