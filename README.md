
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>

<p align="center">
<img src="/img_/portada_github.png"  height=300>
</p>

En esta ocasión, se hará un trabajo situándose en el rol de un ***Data Engineer***. 

## **Introducción**

La idea de este proyecto es lograr internalizar los conocimientos requeridos para la elaboración y ejecución de una API.

`Application Programming Interface` es una interfaz que permite que dos aplicaciones se comuniquen entre sí, independientemente de la infraestructura subyacente. Son herramientas muy versátiles y fundamentales para la creación de, por ejemplo, pipelines, ya que permiten mover y brindar acceso simple a los datos que se quieran disponibilizar a través de los diferentes endpoints, o puntos de salida de la API.

Hoy en día contamos con **FastAPI**, un web framework moderno y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = '/img_/imagen_api.png' height=250><p>
  
## **Tecnologías usadas**
<!--- https://github.com/alexandresanlim/Badges4-README.md-Profile#-analytics- -->
![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Pandas](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![FastAPI](https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)

## **Librerías:**
<ul>
    <li><strong>pandas</strong>: Es una herramienta de análisis y manipulación de datos de código abierto rápida, potente, flexible y fácil de usar, construido sobre el lenguaje de programación Python.</li>
    <li><strong>pymysql</strong>: Es un paquete para la interacción con bases de datos MySQL escrito completamente en Python.</li>
    <li><strong>sqlalchemy</strong>: Es un ORM (Asignador Relacional de Objetos) que brinda a los desarrolladores de aplicaciones todo el poder y la flexibilidad de SQL.</li>
    <li><strong>fastAPI</strong>: Es un web framework moderno y rápido (de alto rendimiento) para construir APIs con Python 3.6+ basado en las anotaciones de tipos estándar de Python..</li>
    <li><strong>uvicorn</strong>: Una librería que funciona como servidor, permite que cualquier computadora se convierta en servidor..</li>
</ul>
  
## **Propuesta de trabajo**

El proyecto consiste en realizar una ingesta de datos desde diversas fuentes, posteriormente aplicar las transformaciones que consideren pertinentes, y luego disponibilizar los datos limpios para su consulta a través de una API. Esta API deberán construirla en un entorno virtual dockerizado.

Los datos serán provistos en archivos de diferentes extensiones, como *csv* o *json*. Se espera que realicen un EDA para cada dataset y corrijan los tipos de datos, valores nulos y duplicados, entre otras tareas. Posteriormente, tendrán que relacionar los datasets así pueden acceder a su información por medio de consultas a la API.

Las consultas a realizar son:

+ Máxima duración según tipo de film (película/serie), por plataforma y por año:
    El request debe ser: get_max_duration(año, plataforma, [min o season])

+ Cantidad de películas y series (separado) por plataforma
    El request debe ser: get_count_plataform(plataforma)  
  
+ Cantidad de veces que se repite un género y plataforma con mayor frecuencia del mismo.
    El request debe ser: get_listedin('genero')  
    Como ejemplo de género pueden usar 'comedy', el cuál deberia devolverles un cunt de 2099 para la plataforma de amazon.

+ Actor que más se repite según plataforma y año.
  El request debe ser: get_actor(plataforma, año)
  
## **Pasos del proyecto**

<p align=center>
<img src = '/img_/pipeline.png' height = 200></p>

1. Ingesta y procesamiento de datos: <a href="https://github.com/JozCrzBrgn/ProyectoIndividual_01/blob/main/Ingesta_Transformacion_Carga.ipynb">[Jupyter Notebook]</a>
  
2. Relacionar el conjunto de datos en MySQL Workbench y crear la base de datos y las tablas necesaria para realizar consultas. <a href="https://github.com/JozCrzBrgn/ProyectoIndividual_01/blob/main/MyBaseDeDatos.sql">[Consultas SQL]</a>

3. Crear la API en un entorno Docker: <a href="https://github.com/JozCrzBrgn/ProyectoIndividual_01/tree/main/fastapi">[API dockerizada]</a>

4. Realizar consultas solicitadas.

5. Video demostrativo: <a href="https://drive.google.com/file/d/1QyQmycHrteeUarGeMLTDkZjfKdvx2WzQ/view?usp=sharing">[Link al video]</a>

