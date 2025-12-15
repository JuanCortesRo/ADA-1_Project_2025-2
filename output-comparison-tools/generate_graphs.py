"""
Nombre: Juan José Cortés Rodríguez
Codigo: 2325109
Materia: Analísis y Diseño de Algoritmos I

Problema: Asociación de Deportes 
Archivo: generate_graphs.py
Descripción: Genera gráficos de análisis de complejidad a partir de benchmark_results.csv

Diciembre 2025
"""

import os
import matplotlib.pyplot as plt
import csv
import math

def leer_resultados():
    """Lee los resultados del benchmark desde el archivo CSV."""
    n_values = []
    tiempos_primera = []
    tiempos_segunda = []
    
    input_dir = os.path.dirname(__file__)
    input_file = os.path.join(input_dir, "benchmark_results.csv")
    with open(input_file, "r", encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            n_values.append(int(row['n']))
            tiempos_primera.append(float(row['tiempo_primera_ms']))
            tiempos_segunda.append(float(row['tiempo_segunda_ms']))
    
    return n_values, tiempos_primera, tiempos_segunda


def grafico_comparacion_tiempos():
    """Gráfico 1: Comparación de tiempos entre ambas soluciones."""
    n_values, tiempos_primera, tiempos_segunda = leer_resultados()
    
    plt.figure(figsize=(12, 7))
    plt.plot(n_values, tiempos_primera, 'b-o', label='Primera Solución (Red-Black Trees)', linewidth=2, markersize=8)
    plt.plot(n_values, tiempos_segunda, 'r-s', label='Segunda Solución (Merge+Insertion)', linewidth=2, markersize=8)
    
    plt.xlabel('Tamaño de entrada (n = número de jugadores)', fontsize=13)
    plt.ylabel('Tiempo de ejecución (milisegundos)', fontsize=13)
    plt.title('Comparación de Tiempos de Ejecución\nPrimera vs Segunda Solución', fontsize=15, fontweight='bold')
    plt.legend(fontsize=11, loc='upper left')
    plt.grid(True, alpha=0.3, linestyle='--')
    # plt.xlim(0, 4000)
    
    # Escala logarítmica si hay variación grande
    if max(tiempos_primera + tiempos_segunda) > 10 * min(tiempos_primera + tiempos_segunda):
        plt.yscale('log')
        plt.ylabel('Tiempo de ejecución (ms) - Escala logarítmica', fontsize=13)
    
    plt.tight_layout()
    output_dir = os.path.dirname(__file__)
    output_file = os.path.join(output_dir, 'grafico_comparacion.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()



def grafico_complejidad_teorica():
    """Gráfico 2: Complejidad teórica vs real para ambas soluciones."""
    n_values, tiempos_primera, tiempos_segunda = leer_resultados()
    
    # ========================================================================
    # PRIMERA SOLUCIÓN: Escalar O(n log n) al tiempo real máximo
    # ========================================================================
    factor_primera = tiempos_primera[-1] / (n_values[-1] * math.log2(n_values[-1]))
    teorico_primera = [n * math.log2(n) * factor_primera for n in n_values]
    
    # ========================================================================
    # SEGUNDA SOLUCIÓN: Escalar usando n=100 (no n=20000)
    # ========================================================================
    n_referencia_idx = 3  # n=100
    factor_segunda = tiempos_segunda[n_referencia_idx] / (n_values[n_referencia_idx] * math.log2(n_values[n_referencia_idx]))
    teorico_segunda_nlogn = [n * math.log2(n) * factor_segunda for n in n_values]
    
    # Curva O(n log n + k²) escalada desde n=100
    def complejidad_real_segunda(n):
        k = n // 4
        
        # Calcular factor usando n=100 (no n=20000)
        n_ref = n_values[n_referencia_idx]
        k_ref = n_ref // 4
        valor_teorico_ref = n_ref * math.log2(n_ref) + k_ref**2
        factor_ajuste = tiempos_segunda[n_referencia_idx] / valor_teorico_ref
        
        return (n * math.log2(n) + k**2) * factor_ajuste
    
    teorico_segunda_completo = [complejidad_real_segunda(n) for n in n_values]
    
    # ========================================================================
    # GRÁFICOS
    # ========================================================================
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # --- Subplot 1: Primera solución ---
    ax1.plot(n_values, tiempos_primera, 'b-o', label='Tiempo Real', linewidth=2, markersize=8, zorder=3)
    ax1.plot(n_values, teorico_primera, 'g--', label='O(n log n) - Teórico', linewidth=2, zorder=2)
    ax1.set_xlabel('Tamaño de entrada (n)', fontsize=12)
    ax1.set_ylabel('Tiempo (ms)', fontsize=12)
    ax1.set_title('Primera Solución: Complejidad Teórica vs Real\n(Árboles Rojinegros)', fontsize=13, fontweight='bold')
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    
    # --- Subplot 2: Segunda solución (CORREGIDO) ---
    ax2.plot(n_values, tiempos_segunda, 'r-s', label='Tiempo Real', linewidth=2.5, markersize=8, zorder=3)
    ax2.plot(n_values, teorico_segunda_nlogn, 'g--', label='O(n log n) - Sin término k²', linewidth=2, zorder=2)
    ax2.plot(n_values, teorico_segunda_completo, 'orange', linestyle=':', 
             label='O(n log n + k²) - Predicción teórica', linewidth=2.5, zorder=1)
    
    # ax2.set_ylim(0, 20000)
    
    ax2.set_xlabel('Tamaño de entrada (n)', fontsize=12)
    ax2.set_ylabel('Tiempo (ms)', fontsize=12)
    ax2.set_title('Segunda Solución: Complejidad Teórica vs Real\n(Merge Sort + Insertion Sort)', fontsize=13, fontweight='bold')
    ax2.legend(fontsize=10, loc='upper left')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    # plt.show()
    output_dir = os.path.dirname(__file__)
    output_file = os.path.join(output_dir, 'grafico_complejidad_teorica.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    plt.close()


def grafico_diferencia_porcentual():
    """Gráfico 3: Diferencia porcentual entre soluciones."""
    n_values, tiempos_primera, tiempos_segunda = leer_resultados()
    
    diferencias = []
    for t1, t2 in zip(tiempos_primera, tiempos_segunda):
        if t1 < t2:
            dif = ((t2 - t1) / t1) * 100
            diferencias.append(dif)
        else:
            dif = -((t1 - t2) / t2) * 100
            diferencias.append(dif)
    
    plt.figure(figsize=(12, 7))
    colors = ['green' if d > 0 else 'red' for d in diferencias]
    bars = plt.bar(range(len(n_values)), diferencias, color=colors, alpha=0.7, edgecolor='black')
    plt.xticks(range(len(n_values)), n_values)
    
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.8)
    plt.xlabel('Tamaño de entrada (n)', fontsize=13)
    plt.ylabel('Diferencia porcentual (%)', fontsize=13)
    plt.title('Diferencia Porcentual de Tiempos\n(Valores positivos: Primera más rápida | Valores negativos: Segunda más rápida)', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    # Agregar leyenda
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='green', alpha=0.7, label='Primera solución más rápida'),
        Patch(facecolor='red', alpha=0.7, label='Segunda solución más rápida')
    ]
    plt.legend(handles=legend_elements, fontsize=11)
    
    plt.tight_layout()
    output_dir = os.path.dirname(__file__)
    output_file = os.path.join(output_dir, 'grafico_diferencia.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    plt.close()


if __name__ == "__main__":
    grafico_comparacion_tiempos()
    grafico_complejidad_teorica()
    grafico_diferencia_porcentual()
    print("\nGraficos listos")