# <div align="center">**STEAM Machine Learning Operations (MLOps)**</div>

![Portada](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/assets/STEAM_MLOps.png?raw=true)

## Introducción

<table><tr><td valign="top" width="50%">

Para este proyecto se simuló un ambiente de trabajo real en el que la plataforma de distribución digital de videojuegos STEAM necesita un sistema de recomendación de videojuegos para usuarios.

Desarrollé un sistema de recomendación con un análisis completo, desde el ETL, entrenamiento y despliegue del modelo ML. Los datos disponibles requirieron una gran cantidad de trabajo de data engineering para poder usarlos en el modelo.

</td><td valign="top" width="50%">

<div align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png" align="center" style="width: 100%" />
</div>  


</td></tr></table>  


## Objetivos

- `MVP` Disponibilizar los datos de la plataforma mediante una API desplegada que permite su consumo desde la web.
- Desarrollar un sistema de recomendación de videojuegos.

## Desarrollo

![Proceso](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/assets/process.gif?raw=true)
Se llevó a cabo los siguietes procesos:
1. `Descripción del Problema`
    - Se presentaron las dificultades encontradas en el desarrollo y actualización de la plataforma.
    - La madurez de los datos es casi nula, datos anidados, no hay procesos automatizados para la actualización de nuevos productos, etc.
    - La [fuente de datos](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj) posee archivos con información acerca de videojuegos; títulos, usuarios y distintos atributos de los mismos.

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
    - **Entrenamiento**: Se entrenaron modelos detallados en el notebook [ML](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/test/ML.ipynb) para luego mandarlo al archivo **main.py**. Más información sobre el entrenamiento en la carpeta [test](https://github.com/PedroLiLL/STEAM-MLOps/tree/main/test).

## Tecnología y herramientas

1. **`Lenguajes`** Python fue el lenguaje principal utilizado para este proyecto.

<div align="center">
    <a href="https://www.python.org/" target="_blank">
        <img style="margin: 30px" src="https://profilinator.rishav.dev/skills-assets/python-original.svg" alt="Python" height="50"/>
    </a>
</div>

2. **`Librerías y frameworks`**
    - **pandas** y **numpy** para la manipulación y procesamiento de datos.
    - **os**, **datetime**, **gzip** y **json** para tareas del EDA como manipulación de estructuras de datos, carga de dataframes, entre otroas.
    - **nltk** para el análisis de sentimiento.
    - **psutil** para optimizar el consumo de memoria de la API.
    - **scikit-learn** para el entrenamiento y modelado del sistema de recomendación de videojuegos.
    - Framework **FastAPI** de python para consumir la API.
    - Servicio en la nube **Render** para implementar la API.
    - **Virtualenv** para crear el entorno virtual de python, instalar y manejar dependencias de manera aislada útiles para la creación de la API.

<div align="center">  
    <a style="padding: 10px" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/22/Pandas_mark.svg/1200px-Pandas_mark.svg.png" alt="Pandas" height="40"/>
    </a>  
    <a style="padding: 10px" target="_blank">
        <img src="https://cdn-images-1.medium.com/max/502/1*l0u9VaJUCE9kNcSqWVbsVA.png" alt="Numpy" height="40"/>
    </a>
    <a style="padding: 10px" target="_blank">
        <img src="https://miro.medium.com/v2/resize:fit:592/0*zKRz1UgqpOZ4bvuA" alt="NLTK" height="40"/>
    </a>
    <a style="padding: 10px" target="_blank">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" alt="scikit" height="35"/>
    </a>
    <a style="padding: 10px" target="_blank">
        <img src="https://www.ccw.sk/files/img/images/5f493b167e5dc864a0265b30_json-logo.png" alt="json" height="35"/>
    </a>
    <a style="padding: 10px" target="_blank">
        <img src="https://cdn.worldvectorlogo.com/logos/fastapi.svg" alt="fastapi" height="35"/>
    </a>
    <a style="padding: 10px" target="_blank">
        <img  src="https://avatars.githubusercontent.com/u/42682871?s=280&v=4" alt="render" height="40"/>
    </a>
</div>

## API

![api](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/assets/1_UaJYVrKSAEXLLYvpppNeOg.gif?raw=true)

Se desarrolló una API para disponibilizar los datos de la empresa a través del framework `FastAPI` compuesta de 6 endpoints (5 métodos y 1 modelo de recomendación) detalladas en el archivo [main.py](https://github.com/PedroLiLL/STEAM-MLOps/blob/main/main.py). Dichos endpoints son:

- `PlayTimeGenre(genero)` Devuelve el año con más horas jugadas para el género de entrada.

    ```
    return {Año de lanzamiento con más horas jugadas para género: año}
    ```

- `UserForGenre(genero)` Devuelve el usuario con mas horas jugadas para el género de entrada.

    ```
    return {Usuario con más horas jugadas para género: user, Horas jugadas: lista_horas_jugadas}
    ```

- `UserRecommend(año)` Devuelve el top 3 de juegos MÁS recomendados por usuarios para el año de entrada.

    ```
    return [{Puesto 1: juego1}, {Puesto 2: juego2}, {Puesto 3: juego3}]
    ```

- `UsersNotRecommend(anio)` Devuelve el top 3 de juegos MENOS recomendados por usuarios para el año de entrada.

    ```
    return [{Puesto 1: juego1}, {Puesto 2: juego2}, {Puesto 3: juego3}]
    ```

- `Sentiment_analysis(anio)` Según el año de entrada, devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento.

    ```
    return {'Negative': cantidad_negativos, 'Neutral': cantidad_neutros, 'Positive': cantidad_positivos}
    ```

- `Recomendacion_juego(id_producto)` Se ingresa el id de un producto y retorna una lista con 5 juegos recomendados similares al ingresado.

Esta API le permitirá a al equipo de STEAM hacer solicitudes para obtener información o realizar acciones específicas.

![DeployMail](../STEAM-MLOps/assets/main.png)
![DeployDocs](../STEAM-MLOps/assets/docs.png)