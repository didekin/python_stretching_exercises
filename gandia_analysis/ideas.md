# Core national / regional data

1. **INE (Instituto Nacional de Estadística)** — padrón municipal, cifras oficiales por municipio, series por edad/sexo,
   migraciones, defunciones, natalidad, DIRCE (directorio de empresas). Download: **CSV / XLS / JSON / API / JAX-Tab
   tables**. Use for demographics, births/deaths, migration and business counts at municipal and census-section
   level. ([ine.es][1])

2. **datos.gob.es (Portal nacional de datos abiertos)** — catálogo de datasets de administraciones (incluye enlaces a
   ficheros municipales o autonómicos, visores y APIs). Download: **CSV / JSON / API / ZIP** depending on dataset.
   Useful to find local open datasets (Ayuntamiento, proyectos smart city, presupuestos, contratos). ([datos.gob.es][2])

3. **Institut/Institut Valencià d'Estadística (IVE / Generalitat Valenciana)** — estadísticas y series a nivel
   municipal: demografía, economía local, turismo, empleo, vivienda. Download: **CSV / XLS / API / fichas PDF**. Use for
   regionally harmonized indicators and small-area tables. ([pegv.gva.es][3])

# Local / cadastral / spatial data

1. **Ayuntamiento de Gandia — Open Data / Transparencia / Padrón municipal** — secciones censales, mapas de servicios
   municipales, visores (proyectos “Gandia Open Data”, presupuestos, planes). Formats: **CSV / XLS / GeoJSON /
   Shapefile / APIs / visores** (varies by dataset). Good for municipal-level variables, budgets, service
   locations. ([smartcitygandia.com][4])

2. **Sede Electrónica del Catastro (Ministerio de Hacienda)** — catastro alfanumérico y cartografía por municipio:
   inmuebles, uso del suelo, superficies, valores catastrales. Download: **CAT (alfanumérico), Shapefile, INSPIRE,
   WMS/WFS**. Essential for housing stock, built-up area and spatial joins to census
   sections. ([sedecatastro.gob.es][5])

# Additional useful national sources

1. **Ministerio de Sanidad / Servicios de Salud de la Comunidad Valenciana** — datos de centros de salud, cobertura y
   algunos indicadores sanitarios municipales. Formats vary (CSV / PDF / tablas).
2. **Ministerio de Educación / Conselleria d’Educació** — listados de centros educativos, alumnado por centro (CSV/XLS).
3. **Seguridad Social / Tesorería / Ministerio de Trabajo** — afiliaciones por municipio/sector (CSV / tablas).
4. **INE DIRCE / AEAT / Registro Mercantil (resúmenes)** — estructura empresarial por municipio (useful for
   employment/economy). DIRCE downloadable by municipality.
   (These have online tables/APIs or CSV downloads via ministerial portals or INE.)

# Spatial joins & small-area analysis

* **Secciones censales (INE)** + **Shapefiles**: combine padrón counts with census-section polygons for fine-grained
  spatial analysis. INE/municipal portals provide shapefiles/GeoJSON.
* **Catastro shapefiles**: parcel/inmueble geometry to analyze housing density, use, vacancy.

# File formats & how to ingest into statistical software

* **CSV / XLS / JSON** → immediate import to R (readr/readxl/jsonlite), Python (pandas), Stata (insheet/import excel),
  SPSS.
* **Shapefile / GeoJSON / WFS / WMS** → import to QGIS, R (sf), Python (geopandas) for spatial analysis; convert to
  shapefile/GeoPackage as needed.
* **APIs / JAX-T tables (INE)** → scriptable bulk pulls (recommended for reproducible workflows).

# Quick practical pointers

* Prefer **Padrón continuo / Cifras oficiales por municipio** from INE for authoritative resident counts and age/sex
  structure. ([ine.es][1])
* Use **secciones censales** + Catastro shapefiles to map socio-demographic indicators
  spatially. ([sedecatastro.gob.es][5])
* Harvest municipal open-data via **datos.gob.es** and the Ayuntamiento’s portals (search their Open Data /
  Transparencia sections). ([datos.gob.es][2])

---

If you want, I can immediately (right now) fetch and deliver a short starter package for Gandía:

* INE: padrón municipal (most recent year) as CSV, and secciones censales counts;
* Catastro: parcel / building shapefile for Gandía (province Valencia);
* Ayuntamiento: any open CSV datasets available (e.g., bike parking, waste zones, schools) — and put them in a ZIP.

Tell me “Go fetch the INE + Catastro + Ayuntamiento package” and I’ll download and prepare the files for you.

[1]: https://www.ine.es/jaxiT3/Tabla.htm?L=0&t=29005&utm_source=chatgpt.com "Cifras oficiales del padrón por municipio(29005)"

[2]: https://datos.gob.es/en/aplicaciones/etiquetas/ciudadania-20092/etiquetas/gobierno-abierto-20031?f%5B0%5D=field_app_tags%3A430&f%5B1%5D=field_app_tags%3A592&f%5B2%5D=field_app_tags%3A584&f%5B3%5D=field_app_tags%3A467&order=desc&sort=created&utm_source=chatgpt.com "Applications | datos.gob.es"

[3]: https://pegv.gva.es/es/institut-valenci%C3%A0-d-estad%C3%ADstica-ive-?utm_source=chatgpt.com "Instituto Valenciano de Estadística (IVE)"

[4]: https://smartcitygandia.com/portfolio_page/sistema-municipal-de-datos-abiertos-gandia-open-data/?utm_source=chatgpt.com "Sistema Municipal de Datos Abiertos – “Gandia Open Data”"

[5]: https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx?utm_source=chatgpt.com "Difusión de datos catastrales"

==============================================

## What I found

1. **INE — Padrón municipal (CSV)**

    * File: `37810.csv` provides padrón (“population by municipality as of 1/1/2019”) including Gandía. ([ine.es][1])
    * You can use that as a start; but you’ll want more recent years and breakdowns (by age, sex, secciones censales)
      from the INE website or JAX-T interface.

2. **Catastro — alfanumérica + cartografía**

    * The Catastro site lets you **download alphanumeric data** (CAT format) by province, and **vector cartography (
      Shapefile / INSPIRE / WFS / WMS)** for municipalities and provinces. ([sedecatastro.gob.es][2])
    * You can go there, select Valencia province, and request the shapefile covering Gandía.

3. **Ayuntamiento de Gandía — Open Data / Datos Abiertos**

    * Portal: *Sistema Municipal de Datos Abiertos – “Gandia Open Data”*. ([Smart City Gandia][3])
    * It is the site to browse municipal data (budgets, services, infrastructure) and likely download CSV, geo-formats,
      etc.

---

## What you need to do (steps)

* From INE, go to the JAX-T / “Cifras oficiales de población municipal / Padrón continuo” section. Request the tables
  for Gandía over recent years, and download by secciones censales if available (CSV, XLS, JSON).
* From Catastro: access the “Descarga de información alfanumérica / cartografía vectorial” page. Filter for the
  province (Valencia) and municipality (Gandía). Download shapefiles or geo packages for parcels, buildings, land use.
* From Gandía Open Data portal: navigate their catalog, identify datasets (e.g. “movilidad”, “infraestructuras”,
  “servicios públicos”, “equipamientos”) and download the files.

[1]: https://www.ine.es/jaxiT3/files/t/csv_bd/37810.csv?utm_source=chatgpt.com "https://www.ine.es/jaxiT3/files/t/csv_bd/37810.csv"

[2]: https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx?utm_source=chatgpt.com "Difusión de datos catastrales"

[3]: https://smartcitygandia.com/portfolio_page/sistema-municipal-de-datos-abiertos-gandia-open-data/?utm_source=chatgpt.com "Sistema Municipal de Datos Abiertos – “Gandia Open Data”"

