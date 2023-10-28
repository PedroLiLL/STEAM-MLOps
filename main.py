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
