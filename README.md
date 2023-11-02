# STEAM Machine Learning Operations (MLOps)

![Portada](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/assets/STEAM_MLOps.png?raw=true)

## Introducción

Para este proyecto se simuló un ambiente de trabajo real en el que la plataforma de distribución digital de videojuegos STEAM necesita un sistema de recomendación de videojuegos para usuarios.

Desarrollé un sistema de recomendación con un análisis completo, desde el ETL, entrenamiento y despliegue del modelo ML. Los datos disponibles requirieron una gran cantidad de trabajo de data engineering para poder usarlos en el modelo.

## Objetivos

- `MVP`: Disponibilizar los datos de la plataforma mediante una API desplegada que permite su consumo desde la web.
- Desarrollar un sistema de recomendación de videojuegos.

## Desarrollo

![Proceso](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/assets/process.gif?raw=true)
Se llevó a cabo los siguietes procesos:
1. `Descripción del Problema`
    - Se presentaron las dificultades encontradas en el desarrollo y actualización de la plataforma.
    - La madurez de los datos es casi nula, datos anidados, no hay procesos automatizados para la actualización de nuevos productos, etc.
    - Se debe hacer el proceso desde 0.

2. `Data engineering`
    - **ETL (Extracción, Transformación y Carga de datos)**: Se realizó la extracción de datos desde su origen, transformación y limpieza para su uso futuro. El proceso de ETL se detalla en este [archivo](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/test/ETL.ipynb) y en general, todos los procesos de ingeniería de datos están detallados en esta [carpeta](https://github.com/PedroLiLL/STEAM-MLOps/tree/main/test)
    - **Disponibilidad de datos limpios**: Los datos procesados y limpios se pusieron a disposición en diferentes archivos:
        - Las tablas originales se procesaron y se guardaron disjuntamente en formato `.parquet` en la carpeta [Dataset](https://github.com/PedroLiLL/STEAM-MLOps/tree/main/Dataset)
        - Las tablas mergeadas; que son las que mayoritariamente se utilizaron para análisis posteriores se guardaron el formato `.parquet` en el repositorio principal, entre ellos:   <br>
        [items_games.parquet](https://github.com/PedroLiLL/STEAM-MLOps/tree/main), [items_games_util.parquet](https://github.com/PedroLiLL/STEAM-MLOps/tree/main), [reviews_games.parquet](https://github.com/PedroLiLL/STEAM-MLOps/tree/main) y [steam_games_ml.parquet](https://github.com/PedroLiLL/STEAM-MLOps/tree/main)

3. `DevOps`
    - **Desarrollo de la API**: Se desarrolló un conjunto de funciones que permiten el acceso y consulta de datos disponibles. El código de la API se encuentra en el siguiente archivo [main](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/main.py)
    - **Deployment**: Se realizó la virtualización y despliegue de la estructura de la API para que sea consumible desde la web. La API se desplegó en el siguiente enlace:

        👉[**PieroLi-STEAM-MLOps**](https://piero-li-api-steam-mlops-x825.onrender.com/docs)
    
4. `Machine learning`
    - **EDA y toma de desiciones**: Se llevó a cabo un análisis exploratorio de datos, entender qué dicen las columnas de los datos y tomar desiciones sobre las columnas necesarias para el entrenamiento del modelo.
    - **Entrenamiento**: 