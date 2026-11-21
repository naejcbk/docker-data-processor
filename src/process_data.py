import os
import sys
import pandas as pd

def main():
    input_path = os.getenv("INPUT_PATH", "/app/data/input.csv")
    output_path = os.getenv("OUTPUT_PATH", "/app/output/resumen.csv")

    print(f"[INFO] Leyendo datos desde: {input_path}")

    if not os.path.exists(input_path):
        print(f"[ERROR] No se encontró el archivo de entrada en {input_path}")
        sys.exit(1)

    df = pd.read_csv(input_path)
    filas_iniciales = len(df)

    # Limpieza: eliminar duplicados y filas con valores nulos
    df_clean = df.drop_duplicates().dropna().copy()
    filas_limpias = len(df_clean)

    # Cálculo de métricas por categoría
    df_clean["total_venta"] = df_clean["cantidad"] * df_clean["precio_unitario"]
    resumen = (
        df_clean.groupby("categoria", as_index=False)
        .agg(
            productos_unicos=("producto", "count"),
            unidades_totales=("cantidad", "sum"),
            ingresos_totales=("total_venta", "sum"),
            precio_promedio=("precio_unitario", "mean"),
        )
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    resumen.to_csv(output_path, index=False)

    print(f"[INFO] Filas iniciales: {filas_iniciales} | Filas válidas: {filas_limpias}")
    print(f"[OK] Resumen guardado exitosamente en: {output_path}")
    print("\n--- Vista previa del resultado ---")
    print(resumen.to_string(index=False))

if __name__ == "__main__":
    main()