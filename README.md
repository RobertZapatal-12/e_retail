# Massive E-Commerce Database Performance Lab

## Interfaz de ingreso de datos

Aplicación de escritorio en español, con diseño minimalista y controles rectangulares.
Incluye formularios para catálogo, inventario, clientes, pedidos, envíos, promociones
y pagos, usando los métodos de inserción existentes.

Desde la carpeta del proyecto, en Windows:

```powershell
py -m pip install -r requirements.txt
py -m app.gui
```

También puedes abrir `iniciar.bat` con doble clic, ejecutar `py main.py`,
`py -m app` o `py app/main.py`. Los scripts pueden iniciarse por su ruta absoluta
desde otra carpeta. `app/main.py` abre la interfaz por defecto; para ejecutar
la generación masiva de datos explícitamente, usa `py main.py --seed`.
Comprueba las dependencias e importaciones con `py main.py --check`.

Requiere Python con Tkinter y PostgreSQL con la base `e_retail` y sus tablas ya
creadas. La interfaz no crea tablas ni ejecuta la generación masiva de datos.
La conexión utiliza la configuración existente de `connection/database.py`.
Puedes personalizarla con las variables de entorno `PGHOST`, `PGPORT`,
`PGDATABASE`, `PGUSER` y `PGPASSWORD` antes de iniciar la aplicación.

Selecciona un módulo y un tipo de registro, completa los campos obligatorios y
pulsa **Guardar registro** (o **Ctrl + Enter**). Los ID se ingresan manualmente:
deben ser únicos y las referencias deben existir previamente. Por ejemplo, crea
una marca antes de insertar su producto. Las fechas usan `AAAA-MM-DD HH:MM`.
Los importes aceptan punto o coma decimal. Si falla el guardado, se conservan los
valores para corregirlos; al guardar correctamente, el formulario se limpia.
Al cambiar de formulario se descartan los valores que no se hayan guardado.

Verificación sin insertar datos reales:

```powershell
py -m unittest discover -s tests
```

Proyecto enfocado en la ingeniería y optimización de bases de datos para un entorno de e-commerce de alta escala. Se desarrolla un backend simulado capaz de generar y gestionar millones de registros relacionados con inventario, pedidos, clientes, pagos y carritos de compra abandonados, reproduciendo escenarios cercanos a sistemas utilizados en plataformas de comercio electrónico de gran volumen.

El objetivo principal es analizar el comportamiento de consultas SQL complejas sobre grandes volúmenes de datos y aplicar técnicas avanzadas de optimización para reducir drásticamente los tiempos de ejecución. Para ello se emplean herramientas como `EXPLAIN ANALYZE`, índices compuestos, índices GIN, vistas materializadas y estrategias de reescritura de consultas, documentando el impacto de cada mejora hasta alcanzar reducciones de rendimiento superiores al 90% en los casos analizados.

El proyecto también incorpora un entorno completamente dockerizado para garantizar la reproducibilidad del sistema, facilitando su despliegue y ejecución en cualquier equipo con una configuración mínima.

## Objetivos

* Simular un e-commerce de gran escala con millones de transacciones.
* Analizar consultas SQL de alta complejidad sobre grandes volúmenes de información.
* Optimizar consultas mediante análisis de planes de ejecución (`EXPLAIN ANALYZE`).
* Implementar índices compuestos y GIN para acelerar búsquedas y filtros.
* Diseñar y utilizar vistas materializadas para mejorar consultas analíticas.
* Comparar métricas de rendimiento antes y después de cada optimización.
* Ejecutar todo el ecosistema mediante Docker y Docker Compose.

## Tecnologías

* PostgreSQL
* SQL Avanzado
* Docker
* Docker Compose
* Python (generación masiva de datos)
* Faker
* psycopg2

## Conceptos aplicados

* Query Optimization
* Database Performance Tuning
* Query Planning
* Indexing Strategies
* Materialized Views
* Bulk Data Generation
* Transaction Processing
* Execution Plan Analysis
* Relational Database Design
* High-Volume Data Simulation
