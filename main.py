from fastapi import FastAPI
import pandas as pd

# Instanciamos un objeto de la clase fastapi para construir la aplicación
app = FastAPI(title='STEAM Games: Consultas', description='Esta aplicación permite realizar consultas sobre videojuegos, reseñas de usuarios, recomendaciones y más')

# cargamos las tablas limpias en .parquet
items_games = pd.read_parquet('items_games.parquet')
reviews_games = pd.read_parquet('reviews_games.parquet')

# ruta inicial
@app.get("/")
async def index():
    mensaje = 'Bienvenidx a mi API para consultas sobre videojuegos, reseñas de usuarios y recomendaciones de la plataforma STEAM'
    return {'Mensaje': mensaje}


@app.get("/Play-Time-Genre/{genero}", name="Tiempo de juego por género")
def PlayTimeGenre(genero: str):
    '''
    devuelve el año con mas horas jugadas para dicho género

    Args: 
        genero (str): género del juego

    return:
        dict: diccionario con el género X y el año de lanzamiento con más horas jugadas
    
    '''
    # Filtramos el dataframe 'items_games' respecto al parámetro genero
    df_util = items_games[items_games['genres']== genero]
    
    # Agrupamos el dataframe anterior por año de lanzamiento, suma de minutos de juego y ordenamos en forma descendente
    agrupado = df_util.groupby('year_release')['playtime_forever'].sum().sort_values(ascending=False)

    # El valor máximo tendrá índice [0]
    anio = agrupado.index[0]
    
    return {f"Año de lanzamiento con más horas jugadas para el género {genero}": int(anio)}


@app.get("/User-For-Genre/{genero}", name="Usuario con mas horas jugadas para un género")
def UserForGenre(genero: str):
    '''
    devuelve el usuario con mas horas jugadas para dicho género

    Args: 
        genero (str): género del juego

    return:
        dict: diccionario con el género X y el usuario con más horas jugadas
    
    '''
    # Filtramos el dataframe 'items_games' respecto al parámetro genero
    df_util = items_games[items_games['genres']== genero]

    # Agrupamos el dataframe anterior por usuario, suma de minutos de juego y ordenamos en forma descendente
    agrupado = df_util.groupby('user_id')['playtime_forever'].sum().sort_values(ascending=False)

    # El valor máximo tendrá índice [0]
    user = agrupado.index[0]

    # tomamos las filas del dataframe util que contengan su repsectivo usuario (user)
    df_genero_user = df_util[df_util['user_id']==user]

    # agrupamos respecto a los años y suma de minutos de juego y convertimos a horas de juego
    horas_jugadas = round(df_genero_user.groupby('year_release')['playtime_forever'].sum()/60, 3)

    # Guardamos la serie 'horas_jugadas' en una lista
    lista_horas_jugadas = [f'Año: {int(anio)}, Horas: {horas}' for anio, horas in horas_jugadas.items()]

    return {f"Usuario con más horas jugadas para género {genero}": user, "Horas jugadas": lista_horas_jugadas}


@app.get("/User-Recommend/{anio}", name="Top 3 de juegos MÁS recomendados por usuarios por año")
def UserRecommend(anio: int):
    '''
    devuelve el top 3 de juegos MÁS recomendados por usuarios para el año dado.
    
    Args: 
        anio (int): año de consulta

    return:
        dict: diccionario con los 3 juegos más recomendados por usuarios
        ->  reviews['recommend'] = True(1)
        ->  comentarios positivos(2) o neutros(1)

    '''
    # Si el año de lanzamiento(year_release) no coincide con alguno de los años en los que se hace una reseña(year_posted), se retorna un mensaje de erro
    if anio not in reviews_games['year_posted'].unique():
        return f"Año fuera de rango, ingrese un año válido"
    
    else:
        # Filtramos el dataframe con las filas cuyo año de posteo(year_posted) es mayor o igual al año de publicación(year_release)
        df = reviews_games[reviews_games['year_posted']>=reviews_games['year_release']]
        
        # Filtramos el dataframe 'df' para el año parámetro y la columna sentiment_analysis sea positivo(2) o neutro(1)
        df_anio_dado = df[(df['year_posted']==anio) & (df['sentiment_analysis'].isin([1,2]))]

        # Agrupamos el dataframe 'df_anio_dado' por título del juego ('title'), sumamos las recomendaciones('recommend') para tener los juegos más recomendados y ordenamos de forma descendente
        top = df_anio_dado.groupby('title')['recommend'].sum().sort_values(ascending=False)

        # Construimos el top3
        top3 = [{"Puesto 1": top.index[0]}, {"Puesto 2": top.index[1]}, {"Puesto 3": top.index[2]}]

    return top3


@app.get("/Users-Not-Recommend/{anio}", name="Top 3 de juegos MENOS recomendados por usuarios por año")
def UsersNotRecommend(anio: int):
    '''
    devuelve el top 3 de juegos MENOS recomendados por usuarios para el año dado.
    
    Args: 
        anio (int): año de consulta

    return:
        dict: diccionario con los 3 juegos menos recomendados por usuarios
        ->  reviews['recommend'] = False(0)
        ->  comentarios negativos(reviews['sentiment_analysis']==0)

    '''
    # Si el año de lanzamiento(year_release) no coincide con alguno de los años en los que se hace una reseña(year_posted), se retorna un mensaje de erro
    if anio not in reviews_games['year_posted'].unique():
        return f"Año fuera de rango, ingrese un año válido"
    
    else:
        # Filtramos el dataframe con las filas cuyo año de posteo(year_posted) es mayor o igual al año de publicación(year_release)
        df = reviews_games[reviews_games['year_posted']>=reviews_games['year_release']]

        #Ahora filtramos por el año parámetro, recomendaciones negativas(0) y comentarios negativos (0)
        df_anio_dado = df[(df['year_posted']==anio) & (df['recommend']==0) & (df['sentiment_analysis']==0)]

        # Agrupamos respecto al año título del juego, contamos las recomendaciones('recommend') para tener los juegos con más reseñas negtivas y ordenamos de forma descendente
        grupo = df_anio_dado.groupby('title')['recommend'].count().sort_values(ascending=False)

        # Contruimos el top3
        top3 = [{"Puesto 1": grupo.index[0]}, {"Puesto 2": grupo.index[1]}, {"Puesto 3": grupo.index[2]}]

        return top3


@app.get('/sentiment-analysis/{anio}', name='lista con la cantidad de registros de reseñas de usuarios')
def sentiment_analysis(anio: int):
    '''
    Según el año de lanzamiento, devuelve una lista con la cantidad de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento

    Args: 
        anio (int): año de lanzamiento (year_release)

    return:
        list: lista con la cantidad de registros de reseñas de usuarios categorizados

    '''
    # Si el año de lanzamiento(year_release) no coincide con alguno de los años en los que se hace una reseña(year_posted), se retorna un mensaje de erro
    if anio not in reviews_games['year_posted'].unique():
        return f"Año fuera de rango, ingrese un año válido"
    
    else:
        # Filtramos el dataframe con las filas cuyo año de posteo(year_posted) es mayor o igual al año de publicación(year_release)
        df = reviews_games[reviews_games['year_posted']>=reviews_games['year_release']]

        # Filtramos el dataframe 'df' para el año parámetro
        df_anio = df[df['year_release'] == anio]

        # Contamos las filas del dataframe 'df_anio' respecto a los valores únicos de la columna 'sentiment_analysis' {0,1,2} y los guardamos en sus respectivos sentimientos
        positivos = df_anio[df_anio['sentiment_analysis']==2].shape[0] # número de filas de sentimientos positivos(2)
        neutros = df_anio[df_anio['sentiment_analysis']==1].shape[0] # número de filas de sentimientos nneutros(1)
        negativos = df_anio[df_anio['sentiment_analysis']==0].shape[0] # número de filas de sentimientos negativos(0)

        return {'Negative': negativos, 'Neutral': neutros, 'Positive': positivos}
