# Tp_Progrmacion_Ventas

## 👥 Integrantes del Equipo
*   **Crespi, Claudio Sebastian**

---

## 🏢 Escenario Elegido
El proyecto se ambienta en el contexto de un comercio minorista de productos tecnológicos y periféricos informáticos. 

El objetivo principal es resolver la falta de herramientas automatizadas para el seguimiento comercial mediante el procesamiento y análisis de las transacciones. Con este desarrollo en Python se busca procesar el historial de operaciones, calcular métricas de facturación y generar reportes visuales automatizados que muestren de forma clara el rendimiento de las ventas a lo largo del tiempo.

---

## 📊 Descripción del Dataset Utilizado
Para el desarrollo de la solución se utilizó un conjunto de datos estructurado que recopila la información histórica de las transacciones del comercio.

*   **Origen de los datos:** Archivo local de registro de transacciones comerciales.
*   **Formato original:** CSV (ubicado en la ruta del proyecto como `datos/ventas.csv`).
*   **Volumen:** El archivo contiene un total de 6 registros (filas) y 4 variables (columnas).
*   **Variables disponibles (columnas):**
    *   `producto`: Nombre o descripción del artículo electrónico comercializado (ej. Teclado Mecánico, Ratón Gamer).
    *   `cantidad`: Unidades adquiridas en la transacción (valor entero).
    *   `precio`: Costo unitario del producto en base a la moneda de facturación.
    *   `fecha`: Registro temporal del momento exacto de la compra (formato `AAAA-MM-DD`).

*Nota: El dataset se procesa mediante código para asegurar la correcta interpretación de los tipos de datos numéricos y el orden cronológico de las fechas antes de generar las salidas visuales.*

---

## 🚀 Instrucciones Básicas para Ejecutar el Script

Siga estos pasos para configurar el entorno y ejecutar el código de manera local desde la raíz del proyecto:

### 1. Requisitos Previos
Asegúrese de tener instalado **Python 3.x** en su sistema. Puede verificarlo en su terminal con el comando:
```bash
python --version
```

### 2. Instalación de Dependencias
Abra la terminal en la carpeta raíz del proyecto (`TP_Programacion_Ventas`) e instale las librerías necesarias ejecutando:
```bash
pip install pandas matplotlib openpyxl
```

### 3. Estructura de Archivos del Proyecto
Para el correcto funcionamiento del script, el proyecto debe mantener la siguiente estructura jerárquica:
*   📁 `datos/` ➔ Contiene el archivo de origen `ventas.csv`.
*   📁 `resultados/` ➔ Almacena el gráfico generado `evolucion_ventas.png`.
*   📁 `scripts/` ➔ Contiene el código ejecutable `analisis_ventas.py`.

### 4. Ejecución del Script
Ejecute el programa corriendo el siguiente comando en la consola (respetando la ruta de la carpeta `scripts`):
```bash
python scripts/analisis_ventas.py
```
*(Nota: El script procesará automáticamente los datos de origen y actualizará el gráfico `evolucion_ventas.png` dentro de la carpeta `/resultados`).*
