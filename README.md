# Procesador de Datos en Docker

Contenedor Docker que ejecuta un script en Python (`pandas`) para limpiar un archivo CSV (eliminando filas duplicadas y valores nulos) y generar un resumen estadístico por categoría.

## Variables de entorno

| Variable | Descripción | Valor por defecto | Requerida |
| :--- | :--- | :--- | :--- |
| `INPUT_PATH` | Ruta del archivo CSV de entrada dentro del contenedor | `/app/data/input.csv` | No |
| `OUTPUT_PATH` | Ruta donde se guardará el CSV procesado dentro del contenedor | `/app/output/resumen.csv` | No |

## Puertos
Esta aplicación es un proceso por lotes (batch) y **no expone puertos**.

## Volúmenes

* **Entrada (`/app/data`)**: Carpeta local que contiene el archivo CSV de entrada (montada en modo solo lectura `:ro`).
* **Salida (`/app/output`)**: Carpeta local donde el contenedor escribirá el archivo `resumen.csv`.

## Construcción local

```bash
docker build -t jeancarloscb/data-processor:1.0.0 .