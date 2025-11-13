# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a business documentation repository for CENOTE, a restaurant franchise company based in Argentina. The repository contains comprehensive business documentation in Spanish outlining investment proposals, financial analysis, and expansion strategies for their Mexican food restaurant chain.

## Repository Structure

### 📁 01_DOCUMENTOS_MAESTROS/
- `💙_CENOTE_DOCUMENTO_MAESTRO.md` - Master consolidated document containing complete company information, investment proposals, financial projections, and strategic planning for CENOTE restaurant franchise
- `CLAUDE.md` - Project guidance for Claude Code
- `❓_GUIA_PREGUNTAS_CLAUDE.md` - Question guide for Claude interactions
- `📅_FRAMEWORK_REUNIONES_SEMANALES.md` - Weekly meeting framework
- `📊_DASHBOARD_EJECUTIVO_CENOTE.md` - Executive dashboard documentation
- `📋_SISTEMA_UPDATES_SEMANALES.md` - Weekly updates system
- `🔄_TEMPLATE_MEJORA_CONTINUA.md` - Continuous improvement template
- `🚀_RESUMEN_SISTEMA_COMPLETO.md` - Complete system summary
- `⏱️_REGISTRO_TIEMPO_TRABAJO_CLAUDE.md` - Time tracking log for Claude work sessions
- `📋_ORGANIZACION_TEMAS_REUNIONES_NOV.md` - Meeting topics organized by department

### 📁 02_ANALISIS_FINANCIERO/
- `ANALISIS_ESTRUCTURA_ACCIONARIA_DETALLADO.md` - Detailed shareholder structure analysis
- `ESTRUCTURA_OPERATIVA_GANANCIAS.md` - Operational structure and earnings documentation
- `VALUACION_5_ANOS_ESCENARIOS.md` - 5-year valuation scenarios analysis
- `VALUACION_REALISTA_FINAL.md` - Final realistic valuation document
- `ANALISIS_VENTAS_MARTINEZ_2025_REAL.md` - Real sales analysis for Martínez location 2025 (Jan-Oct)

### 📁 03_ESTRUCTURA_ORGANIZACIONAL/
- `ESTRUCTURA_OFICINAS_CENOTE_OPERATIVA.md` - Operational office structure and protocols documentation
- `ESTRUCTURA_DEPARTAMENTAL_COMPLETA_CENOTE.md` - Comprehensive departmental structure analysis with responsibilities and personnel assignments
- `ESTRUCTURA_DEPARTAMENTAL_RESUMEN_1HOJA.md` - One-page summary of departmental structure
- `PROCEDIMIENTOS_CONTROL_COSTOS_PRODUCTIVOS.md` - Production cost control procedures

### 📁 04_RECURSOS_HUMANOS/
- `PLAN_TRABAJO_MATI_PRIMERAS_SEMANAS.md` - Operations manager work plan for initial weeks
- `GUIA_ENTREVISTA_MATI_OPERATIONS.md` - Interview guide for Operations Manager position

### 📁 05_PRESENTACIONES_SOCIOS/
- `PRESENTACION_SOCIOS_20MIN.md` - 20-minute partner presentation materials
- `REUNION_TEQUILA_DF_PREPARACION.md` - Preparation materials for Tequila DF supplier meeting and negotiation strategy
- `PLAN_DE_NEGOCIOS_INVERSORES.md` - Comprehensive investment proposal and business plan for investors
- `AGENDA_REUNION_CENOTE_5NOV.md` - Meeting agenda for CENOTE team meetings
- `AGENDA_REUNION_ARQUITECTOS_5NOV.md` - Meeting agenda for architecture team
- `AGENDA_REUNION_MERCHANDISING_RODRIGO.md` - Meeting agenda for merchandising discussions
- `MAIL_DANI_MKT_PROPUESTA.md` - Marketing proposal for Dani
- `ORGANIGRAMA_CENOTE.md` - CENOTE organizational chart
- `PROPUESTA_REESTRUCTURACION_CENOTE.md` - Company restructuring proposal

### 📁 06_PRESENTACIONES_HTML/
- `presentacion_cenote.html` - HTML presentation for investors
- `plan_negocios_inversores.html` - Investment proposal and business plan HTML presentation
- `estructura_departamental_visual.html` - Visual departmental structure presentation
- `plan_trabajo_mati_visual.html` - Visual work plan presentation
- `plan_trabajo_mati_completo.html` - Complete work plan presentation
- `dashboard_cenote_personal.html` - Interactive personal dashboard with calendar, timeline, and meeting tracking
- `dashboard_ejecutivo_socios.html` - Executive dashboard for partners with key metrics
- `dashboard_agave_socios.html` - AGAVE brand dashboard for partners
- `reunion_cenote_5nov.html` - CENOTE meeting presentation (landscape format for projection)
- `reunion_arquitectos_5nov.html` - Architecture meeting presentation (landscape format)
- `reunion_merchandising_rodrigo.html` - Merchandising meeting presentation
- `analisis_ventas_mz_2025.html` - Visual analysis of Martínez sales 2025
- `comparativo_mz_nunez_2025.html` - Comparative analysis Martínez vs Núñez with interactive charts
- `dashboard_ranking_productos_2025.html` - Product ranking dashboard with 8 interactive charts
- `dashboard_ranking_productos_2025_interactivo.html` - Interactive product ranking (latest version with full data)

### 📁 07_DATOS_VENTAS_RAW/
- `2025/` - Raw sales data for 2025
  - `venta_martinez_2025.csv` - All Martínez transactions 2025 (18,302 records)
  - `venta_nunez_2025.csv` - All Núñez transactions 2025 (8,978 records)
  - `ranking_martinez_2025.csv` - Martínez product ranking (194 products)
  - `ranking_nunez_2025.csv` - Núñez product ranking (206 products)
- `README.md` - Documentation of data structure and sources


## Content Summary

The repository focuses on:
- Business investment opportunities ($1M USD for 33% equity)
- Financial analysis of existing restaurant locations (Martínez and Núñez)
- Expansion plans for 3 additional CABA locations
- Long-term vision including technology platform development ("Luchadores" subscription model)
- Revenue models and franchise structure
- Market analysis and competitive positioning
- Organizational structure and departmental responsibilities
- Operational procedures and cost control systems
- Personnel management and work planning

## Development Context

This repository is primarily a business documentation repository with auxiliary analysis scripts. Development work includes:
- Document editing and formatting
- Business plan updates
- Financial model revisions
- Strategic planning documentation
- Organizational structure documentation
- Operational procedure documentation
- HTML presentation generation and updates
- Sales data analysis using Python and PowerShell scripts

### Data Analysis Scripts

**Data Processing Pipeline:**
The analysis workflow follows: CSV data → Python/PowerShell processing → JSON temp files → Node.js dashboard injection → HTML dashboards

**Python Scripts:**
- `analizar_ventas_mz.py` - Detailed sales analysis from CSV data
  - Usage: `python analizar_ventas_mz.py`
  - Generates comprehensive monthly breakdowns with channel, shift, and payment method analysis
  - Reads CSV file from hardcoded path (update path in script as needed)

- `generar_datos_dashboard.py` - Generates JSON data files for dashboards
  - Processes CSV rankings into `productos_mz_temp.json` and `productos_nu_temp.json`
  - These JSONs are then injected into HTML dashboards by Node.js script

**PowerShell Scripts:**
- `analizar_ventas_mz.ps1` - PowerShell version of sales analysis
- `analisis_simple_mz.ps1` - Simplified analysis script
- `analisis_nunez.ps1` - Núñez location-specific analysis
- `analisis_ranking_completo.ps1` - Complete product ranking analysis
- `generar_dashboard_completo.ps1` - Dashboard generation orchestration
- Usage: Run directly in PowerShell terminal

**Node.js Scripts:**
- `generar_dashboard_final.js` - Injects JSON data into HTML dashboard templates
  - Usage: `node generar_dashboard_final.js`
  - Reads `productos_mz_temp.json` and `productos_nu_temp.json`
  - Updates `dashboard_ranking_productos_2025_interactivo.html` with current data
  - Handles BOM removal and proper JSON formatting

**Data Sources:**
- Raw sales data located in `07_DATOS_VENTAS_RAW/2025/`
- Transaction CSVs: `venta_martinez_2025.csv` (18,302 records), `venta_nunez_2025.csv` (8,978 records)
- Product rankings: `ranking_martinez_2025.csv` (194 products), `ranking_nunez_2025.csv` (206 products)
- See `07_DATOS_VENTAS_RAW/README.md` for detailed data structure

**Opening HTML Dashboards:**
To open generated HTML dashboards in browser (Windows):
```bash
start "" "C:\Users\PC acer\Desktop\Proyectos\CENOTE\06_PRESENTACIONES_HTML\dashboard_ejecutivo_socios.html"
start "" "C:\Users\PC acer\Desktop\Proyectos\CENOTE\06_PRESENTACIONES_HTML\dashboard_agave_socios.html"
start "" "C:\Users\PC acer\Desktop\Proyectos\CENOTE\06_PRESENTACIONES_HTML\dashboard_ranking_productos_2025_interactivo.html"
```

## Common Tasks

When working with this repository, you will typically be asked to:
- Update financial projections and business metrics
- Modify organizational structure documents
- Create or update presentation materials (both markdown and HTML)
- Analyze business data and create reports
- Update master documents with new information
- Generate HTML presentations from markdown content
- Create meeting agendas and track action items
- Update time tracking logs for work sessions
- Organize departmental topics and priorities
- Run sales analysis scripts on raw CSV data
- Generate comparative reports between locations (Martínez vs Núñez)
- Create product ranking dashboards

## Key Files for Quick Reference

- **Master Document**: `01_DOCUMENTOS_MAESTROS/💙_CENOTE_DOCUMENTO_MAESTRO.md` - Contains all consolidated company information including investment proposals, financial projections, expansion timeline, and strategic vision
- **Time Tracking**: `01_DOCUMENTOS_MAESTROS/⏱️_REGISTRO_TIEMPO_TRABAJO_CLAUDE.md` - Track all work sessions with Nico
- **System Templates**: `01_DOCUMENTOS_MAESTROS/` - Contains meeting frameworks, dashboards, and improvement templates
- **Financial Analysis**: `02_ANALISIS_FINANCIERO/` - Detailed financial projections and valuation scenarios
- **Organizational Structure**: `03_ESTRUCTURA_ORGANIZACIONAL/` - Company structure, procedures, and departmental organization
- **Presentations**: `05_PRESENTACIONES_SOCIOS/` and `06_PRESENTACIONES_HTML/` - Meeting agendas, investor materials, and interactive dashboards

## Languages and Content

- **Primary language**: Spanish
- **Content type**: Business documentation, financial projections, strategic planning, meeting agendas, time tracking
- **Format**: Markdown documentation with interactive HTML presentations

## Important Context

### Timeline and Current Status
- **M0 (Mayo 2024)**: Start of 60-month expansion plan with Núñez opening
- **M18 (Noviembre 2025)**: CURRENT MONTH - 30% of plan completed
- **M60 (Mayo 2029)**: Target completion date for full expansion
- **Current locations**: Martínez (casa matriz) + Núñez
- **Planned expansion**: 3 additional CABA locations
- **Key milestones**: M29 (local 3), M37 (local 4), M47 (local 5), M53 (plataforma tech), M60 (consolidación)

### Investment Proposal
- **Amount**: $1,000,000 USD
- **Equity**: 33% for investor
- **Target ROI**: 15% annual sustainable return
- **Use of funds**: Expansion of 3 new CABA locations + CENOTE consolidation

### HTML Presentation Guidelines
When creating HTML presentations:
- Use landscape format (apaisado) for projection
- 2-column grid layout when possible
- Avoid scrolling - fit content on single screen
- Include interactive elements (calendars, timelines, forms) when relevant
- Use localStorage for data persistence in dashboards
- Color coding: Arquitectos (orange), CENOTE (cyan), Merchandising (purple)

**Interactive Dashboard Features:**
- `dashboard_cenote_personal.html` includes:
  - Interactive monthly calendar with week numbers (week starts Sunday)
  - Event management system with 4 event types (Feriado, Día Gastronómico, Reunión, Tarea)
  - 60-month expansion timeline with progress bar (M0 to M60)
  - All events persist via localStorage
  - Meeting tracking with departmental color coding
- `dashboard_ranking_productos_2025_interactivo.html` includes:
  - 8 interactive charts comparing Martínez vs Núñez
  - Product category analysis (Tacos, Burritos, Cocktails, Desserts, etc.)
  - Top performers and comparison metrics
  - Powered by Chart.js for visualizations

### Meeting Tracking
- Always update `⏱️_REGISTRO_TIEMPO_TRABAJO_CLAUDE.md` when starting/ending work sessions
- Track: start time, end time, tasks completed, files modified, decisions made
- Default session duration: 2 hours if not specified

# important-instruction-reminders
Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files. Only create documentation files if explicitly requested by the User.