from fastapi import FastAPI
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:123456789@localhost:3306/EDA_BD', pool_recycle=3600)

conn = engine.connect()

def Query1_min(cnxn, anio, plataf):
    query = f"SELECT title, time_of FROM datos WHERE time_of = (SELECT MAX(time_of) FROM datos WHERE release_year = {anio} and plataf = '{plataf}') and min_season = 'min' and release_year = {anio} and plataf = '{plataf}'"
    df = pd.read_sql(query, cnxn)
    return df

def Query1_season(cnxn, anio, plataf):
    query = f"SELECT title, time_of FROM datos WHERE time_of = (SELECT MAX(time_of) FROM datos WHERE release_year = {anio} and plataf = '{plataf}') and min_season = 'season' and release_year = {anio} and plataf = '{plataf}'"
    df = pd.read_sql(query, cnxn)
    return df

def Query2(cnxn, plataf):
    query_tv = f"select count(plataf) as 'TV Show' from datos where plataf = '{plataf}' and min_season = 'min'"
    query_mov = f"select count(plataf) as 'Movie' from datos where plataf = '{plataf}' and min_season = 'season'"
    df1 = pd.read_sql(query_tv, cnxn)
    df2 = pd.read_sql(query_mov, cnxn)
    df = pd.concat([df1, df2], axis = 1)
    return df

def Query3(cnxn, gene):
    query_amazon = f"select genero, count(genero) as Cant_veces, plataforma from generos where Plataforma = 'Amazon' and genero = '{gene}' group by genero order by Cant_veces desc;"
    query_netflix = f"select genero, count(genero) as Cant_veces, plataforma from generos where Plataforma = 'Netflix' and genero = '{gene}' group by genero order by Cant_veces desc;"
    query_hulu = f"select genero, count(genero) as Cant_veces, plataforma from generos where Plataforma = 'Hulu' and genero = '{gene}' group by genero order by Cant_veces desc;"
    df_a = pd.read_sql(query_amazon, cnxn)
    df_n = pd.read_sql(query_netflix, cnxn)
    df_h = pd.read_sql(query_hulu, cnxn)
    df = pd.concat([df_a, df_n, df_h], axis = 0)
    return df

def Query4(cnxn, plataf, anio):
    query = f"select actor, anio, count(actor) as Cant_veces from casting where actor <> 'Unknown' and plataforma = '{plataf}' and Anio = {anio} group by actor order by Cant_veces desc;"
    df = pd.read_sql(query, cnxn)
    return df


app = FastAPI(
    title='API de consultas.',
    description='API de consultas para plataformas Amazon, Netflix y Hulu.',
    version='0.0.1',
    openapi_tags=[{
        "name":"Querys",
        "description":"Consultas permitidas para el usuario."
        }]
)

@app.get("/")
def read_root():
    return {"Estado": "Lista !!!"}

@app.get("/user_query_1/",tags=["Querys"])
def get_max_duration(anio, plataforma, min_season):
    '''Máxima duración según tipo de film (película/serie), por plataforma y por año: El request debe ser: get_max_duration(año, plataforma, [min o season])'''
    if min_season.lower() == 'min':
        df = Query1_min(conn, anio, plataforma.capitalize())
        return df.to_dict('r')
    elif min_season.lower() == 'season':
        df = Query1_season(conn, anio, plataforma.capitalize())
        return df.to_dict('r')

@app.get("/user_query_2/",tags=["Querys"])
def get_count_plataform(plataforma):
    '''Cantidad de películas y series (separado) por plataforma El request debe ser: get_count_plataform(plataforma)'''
    df = Query2(conn, plataforma.capitalize())
    return df.to_dict('r')

@app.get("/user_query_3/",tags=["Querys"])
def get_listedin(genero):
    '''Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo. El request debe ser: get_listedin('genero')'''
    df = Query3(conn, genero.capitalize())
    df = df.to_dict('r')
    list_df = [df[i]['Cant_veces'] for i in range(len(df))]
    idx = list_df.index(max(list_df))
    return [{'Cantidad':df[idx]['Cant_veces'],'Plataforma':df[idx]['plataforma']}]

@app.get("/user_query_4/",tags=["Querys"])
def get_actor(plataforma, anio):
    '''Actor que más se repite según plataforma y año. El request debe ser: get_actor(plataforma, año)'''
    df = Query4(conn, plataforma.capitalize(), anio)
    df = df.to_dict('r')
    return df[0]
