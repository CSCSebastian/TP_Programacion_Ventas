import os
import csv
import matplotlib.pyplot as plt

def analizar_datos():
    ruta_csv = os.path.join("datos", "ventas.csv")
    
    if not os.path.exists(ruta_csv):
        print(f"Error: No se encontró el archivo en {ruta_csv}")
        return

    ventas_totales = 0
    conteo_productos = {}
    ventas_por_mes = {}

    with open(ruta_csv, mode="r", encoding="utf-8") as archivo:
        lector_csv = csv.DictReader(archivo)
        
        for fila in lector_csv:
            nombre_producto = fila["producto"]
            cantidad = int(fila["cantidad"])
            precio = float(fila["precio"])
            fecha = fila["fecha"]
            
            subtotal = cantidad * precio
            ventas_totales += subtotal
            
            if nombre_producto in conteo_productos:
                conteo_productos[nombre_producto] += cantidad
            else:
                conteo_productos[nombre_producto] = cantidad
                
            mes = fecha[:7]
            if mes in ventas_por_mes:
                ventas_por_mes[mes] += subtotal
            else:
                ventas_por_mes[mes] = subtotal

    producto_mas_vendido = max(conteo_productos, key=conteo_productos.get)
    cantidad_maxima = conteo_productos[producto_mas_vendido]

    # --- IMPRIMIR RESULTADOS EN CONSOLA ---
    print(f"Indicador 1 - Ventas Totales: ${ventas_totales:.2f}")
    print(f"Indicador 2 - Producto Más Vendido: {producto_mas_vendido} ({cantidad_maxima} unidades)")
    
    print("\nIndicador 3 - Ventas por Mes:")
    meses_ordenados = sorted(ventas_por_mes.keys())
    totales_ordenados = [ventas_por_mes[m] for m in meses_ordenados]
    
    for m, t in zip(meses_ordenados, totales_ordenados):
        print(f"  * Mes {m}: ${t:.2f}")

    # --- GENERAR Y GUARDAR EL GRÁFICO ---
    plt.figure(figsize=(8, 5))
    plt.bar(meses_ordenados, totales_ordenados, color="royalblue", edgecolor="black")
    
    # Títulos y etiquetas del gráfico
    plt.title("Evolución Mensual de Ventas", fontsize=14, fontweight="bold")
    plt.xlabel("Meses (Año-Mes)", fontsize=11)
    plt.ylabel("Ingresos Totales ($)", fontsize=11)
    plt.grid(axis="y", linestyle="--", alpha=0.7)

    # Asegurar que la carpeta de destino exista
    carpeta_resultados = "resultados"
    if not os.path.exists(carpeta_resultados):
        os.makedirs(carpeta_resultados)

    # Ruta exacta para guardar la imagen según pide el TP
    ruta_grafico = os.path.join(carpeta_resultados, "evolucion_ventas.png")
    plt.savefig(ruta_grafico, bbox_inches="tight")
    plt.close()
    
    print(f"\n[OK] Gráfico generado con éxito en: {ruta_grafico}")

if __name__ == "__main__":
    print("--- Iniciando Análisis de Ventas ---")
    analizar_datos()
