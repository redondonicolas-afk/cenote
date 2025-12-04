# 💻 SETUP LAPTOP NUEVA - GUÍA COMPLETA

## 🎯 OBJETIVO
Clonar el repositorio CENOTE en tu laptop nueva y poder trabajar desde cualquier lado.

---

## 📋 PREREQUISITOS

### 1. Instalar Git
- Descargar: https://git-scm.com/download/win
- Instalar con opciones por defecto
- Verificar: Abrir CMD y escribir `git --version`

### 2. Configurar Git (Primera vez)
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### 3. Conectar con GitHub
**Opción A: HTTPS (más fácil)**
- Te va a pedir usuario y contraseña cada vez que pushees
- Recomendado: Usar Personal Access Token

**Opción B: SSH (más seguro, una sola vez)**
```bash
# Generar clave SSH
ssh-keygen -t ed25519 -C "tu@email.com"

# Copiar la clave pública
cat ~/.ssh/id_ed25519.pub

# Agregarla en GitHub:
# GitHub → Settings → SSH and GPG keys → New SSH key
```

---

## 🚀 CLONAR EL REPOSITORIO

### Paso 1: Elegir ubicación
```bash
# Ejemplo: crear carpeta Proyectos en Documents
cd C:\Users\TuUsuario\Documents
mkdir Proyectos
cd Proyectos
```

### Paso 2: Clonar
```bash
# HTTPS (reemplazar con tu username)
git clone https://github.com/redondonicolas-afk/cenote.git

# O SSH (si configuraste)
git clone git@github.com:redondonicolas-afk/cenote.git
```

### Paso 3: Verificar
```bash
cd cenote
dir
# Deberías ver todas las carpetas: 01_DOCUMENTOS_MAESTROS, 02_ANALISIS_FINANCIERO, etc.
```

---

## 📂 ESTRUCTURA QUE VAS A TENER

```
C:\Users\TuUsuario\Documents\Proyectos\CENOTE\
├── 01_DOCUMENTOS_MAESTROS/
├── 02_ANALISIS_FINANCIERO/
├── 03_ESTRUCTURA_ORGANIZACIONAL/
├── 04_RECURSOS_HUMANOS/
├── 05_PRESENTACIONES_SOCIOS/
├── 06_PRESENTACIONES_HTML/
├── 07_DATOS_VENTAS_RAW/
├── BOT_LUCHADORES_ESTRUCTURA.md ⭐ NUEVO
├── NEGOCIO_RECLAMOS_CAMARAS_TRANSFORMADORAS.md ⭐ NUEVO
├── DESARROLLADORES_ZONA_NORTE_TARGET.md ⭐ NUEVO
├── CLAUDE.md
└── README.md
```

---

## 🔄 WORKFLOW DIARIO

### Antes de empezar a trabajar:
```bash
cd C:\Users\TuUsuario\Documents\Proyectos\CENOTE
git pull
```
☝️ Esto baja los cambios más recientes de GitHub

### Después de trabajar:
```bash
# Ver qué cambió
git status

# Agregar cambios
git add .

# Commitear
git commit -m "Descripción de lo que hiciste"

# Subir a GitHub
git push
```

---

## 🎯 PROYECTOS ACTUALES

### 1. 🤖 BOT LUCHADORES
**Archivos principales:**
- `BOT_LUCHADORES_ESTRUCTURA.md`
- Carpeta: `01_DOCUMENTOS_MAESTROS/` (documentos de Luchadores)

**Para trabajar en esto, decile a Claude:**
> "Trabajemos en el Bot Luchadores"

### 2. ⚡ CÁMARAS TRANSFORMADORAS
**Archivos principales:**
- `NEGOCIO_RECLAMOS_CAMARAS_TRANSFORMADORAS.md`
- `DESARROLLADORES_ZONA_NORTE_TARGET.md`
- `06_PRESENTACIONES_HTML/presentacion_camaras_transformadoras.html`

**Para trabajar en esto, decile a Claude:**
> "Trabajemos en Cámaras Transformadoras"

### 3. 🍽️ CENOTE / AGAVE (Principal)
**Archivos principales:**
- `01_DOCUMENTOS_MAESTROS/💙_CENOTE_DOCUMENTO_MAESTRO.md`
- Todo en `02_ANALISIS_FINANCIERO/`
- Todo en `06_PRESENTACIONES_HTML/`

**Para trabajar en esto, decile a Claude:**
> "Trabajemos en CENOTE" o "Necesito actualizar el dashboard de octubre"

---

## 🆘 PROBLEMAS COMUNES

### "Permission denied" al hacer push
**Solución:** Configurar SSH keys o usar Personal Access Token

### "Your branch is behind"
**Solución:**
```bash
git pull
# Si hay conflictos, resolverlos manualmente
git push
```

### "Changes not staged for commit"
**Solución:**
```bash
git add .
git commit -m "Tu mensaje"
git push
```

### Quiero descartar cambios locales
```bash
git restore .
# O para un archivo específico:
git restore archivo.md
```

---

## 📱 TRABAJAR DESDE MÚLTIPLES DISPOSITIVOS

### PC Escritorio (la que tenés ahora):
1. Hacés cambios
2. `git add . && git commit -m "mensaje" && git push`

### Laptop Nueva:
1. `git pull` (bajar cambios del escritorio)
2. Trabajar
3. `git add . && git commit -m "mensaje" && git push`

### Volvés al Escritorio:
1. `git pull` (bajar cambios de la laptop)
2. Seguir trabajando

**⚠️ IMPORTANTE:** Siempre hacer `git pull` ANTES de empezar a trabajar

---

## 🎨 BONUS: HERRAMIENTAS ÚTILES

### VS Code (Editor recomendado)
- Descargar: https://code.visualstudio.com/
- Tiene integración Git visual
- Abrís la carpeta CENOTE y ves todo

### GitHub Desktop (Si no te gusta la terminal)
- Descargar: https://desktop.github.com/
- Interfaz visual para Git
- Más fácil para ver cambios y hacer commits

---

## ✅ CHECKLIST PRIMER DÍA CON LAPTOP NUEVA

- [ ] Instalar Git
- [ ] Configurar usuario y email
- [ ] Clonar repositorio
- [ ] Verificar que todo esté (hacer `dir` o `ls`)
- [ ] Hacer un cambio de prueba y pushear
- [ ] Verificar en GitHub que se subió
- [ ] Volver al escritorio y hacer `git pull` para confirmar sincronización

---

## 🚀 LISTO PARA TRABAJAR

Ahora podés:
- Trabajar desde cualquier compu
- Todo está sincronizado en GitHub
- Claude sabe dónde buscar cada proyecto
- No perdés nada si se rompe una compu

**Comando mágico cuando tengas dudas:**
```bash
git status
```
☝️ Te dice TODO lo que está pasando

---

**¿Alguna duda? Preguntale a Claude! 😄**
