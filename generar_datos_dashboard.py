import csv
import json

# Leer Martínez
productos_mz = []
with open('07_DATOS_VENTAS_RAW/2025/ranking_martinez_2025.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['nombre'] and row['nombre'].strip() and row['nombre'] != 'Art. Inexistente':
            try:
                venta = float(row['venta'].replace(',', '.'))
                unidades = float(row['unidades'].replace(',', '.'))
                productos_mz.append({
                    'nombre': row['nombre'].strip(),
                    'categoria': row['nomrub'].strip(),
                    'unidades': unidades,
                    'venta': venta
                })
            except:
                pass

# Leer Núñez
productos_nu = []
with open('07_DATOS_VENTAS_RAW/2025/ranking_nunez_2025.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['nombre'] and row['nombre'].strip() and row['nombre'] != 'Art. Inexistente':
            try:
                venta = float(row['venta'].replace(',', '.'))
                unidades = float(row['unidades'].replace(',', '.'))
                productos_nu.append({
                    'nombre': row['nombre'].strip(),
                    'categoria': row['nomrub'].strip(),
                    'unidades': unidades,
                    'venta': venta
                })
            except:
                pass

# Guardar como JSON
with open('productos_mz.json', 'w', encoding='utf-8') as f:
    json.dump(productos_mz, f, ensure_ascii=False, indent=2)

with open('productos_nu.json', 'w', encoding='utf-8') as f:
    json.dump(productos_nu, f, ensure_ascii=False, indent=2)

print(f"✅ Productos MZ: {len(productos_mz)}")
print(f"✅ Productos NU: {len(productos_nu)}")
print(f"✅ Archivos JSON generados")
