# STEAM Machine Learning Operations (MLOps)
---
![Portada](../STEAM-MLOps/assets/STEAM_MLOps.png)

## Introducción
---
Para este proyecto se simuló un ambiente de trabajo real en el que la plataforma de distribución digital de videojuegos STEAM necesita un sistema de recomendación de videojuegos para usuarios.

Desarrollé un sistema de recomendación con un análisis completo, desde el ETL, entrenamiento y despliegue del modelo ML. Los datos disponibles requirieron una gran cantidad de trabajo de data engineering para poder usarlos en el modelo.

## Objetivos
---
- `MVP`: Disponibilizar los datos de la plataforma mediante una API desplegada que permite su consumo desde la web.
- Desarrollar un sistema de recomendación de videojuegos.

## Desarrollo
---
![Proceso](..\STEAM-MLOps\assets\process.gif)
Se llevó a cabo los siguietes procesos:
1. `Descripción del Problema`
    - Se presentaron las dificultades encontradas en el desarrollo y actualización de la plataforma.
    - La madurez de los datos es casi nula, datos anidados, no hay procesos automatizados para la actualización de nuevos productos, etc.
    - Se debe hacer el proceso desde 0.

2. `Data engineering`
    - **ETL (Extracción, Transformación y Carga de datos)**: Se realizó la extracción de datos desde su origen, transformación y limpieza para su uso futuro. El proceso de ETL se detalla en este [archivo](..\STEAM-MLOps\test\ETL.ipynb)
    - **Disponibilidad de datos limpios**: 