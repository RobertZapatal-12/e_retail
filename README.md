# Massive E-Commerce Database Performance Lab

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
