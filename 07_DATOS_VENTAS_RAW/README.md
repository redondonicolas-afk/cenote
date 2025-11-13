# 📊 DATOS DE VENTAS - RAW DATA

Esta carpeta contiene los archivos originales de ventas exportados del sistema.

## 📁 Estructura

### **2025/**
Datos del año 2025 completo (Enero - Octubre + parcial Noviembre)

#### Archivos de Transacciones:
- `venta_martinez_2025.csv` - Todas las transacciones de Martínez 2025 (18.302 registros)
- `venta_nunez_2025.csv` - Todas las transacciones de Núñez 2025 (8.978 registros)

#### Archivos de Ranking de Productos:
- `ranking_martinez_2025.csv` - Ranking productos vendidos Martínez 2025 (194 productos)
- `ranking_nunez_2025.csv` - Ranking productos vendidos Núñez 2025 (206 productos)

## 📋 Estructura de Archivos

### Ventas (transacciones):
```
turno, comprobant, hora, tipo, mesa, mozo, cub, cobro, cod_cobro,
importe, total, descuento, clinombre, clirazon, clicuit, fecha,
cod_suc, nombresuc
```

### Ranking (productos):
```
id, rubro, nomrub, subrubro, nomsub, codigo, nombre, unidades,
precio, venta
```

## 🔍 Análisis Generados

Los análisis basados en estos datos se encuentran en:
- `02_ANALISIS_FINANCIERO/ANALISIS_VENTAS_MARTINEZ_2025_REAL.md`
- `06_PRESENTACIONES_HTML/analisis_ventas_mz_2025.html`
- `06_PRESENTACIONES_HTML/comparativo_mz_nunez_2025.html`
- `06_PRESENTACIONES_HTML/dashboard_ranking_productos_2025.html`

## 📅 Última Actualización

**Fecha:** 4 Noviembre 2025
**Período:** Enero - Octubre 2025 (10 meses completos)
**Fuente:** Sistema de ventas Maxirest

## ⚠️ Notas Importantes

- Estos archivos son CONFIDENCIALES
- NO commitear a repositorios públicos
- Mantener backup actualizado
- Actualizar mensualmente con nuevos datos

---

**Próxima actualización:** Diciembre 2025 (datos completos año 2025)
