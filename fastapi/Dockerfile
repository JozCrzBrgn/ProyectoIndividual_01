#FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10
#COPY ./app /app

FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

# Virtual -> python -m virtualenv venv
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
# .\venv\Scripts\activate
# Istalamos todos los paquetes pip install $$$$$
# pip freeze > "requirements.txt"

# conda -> conda activate fastapi-mysql
# conda -> code .

# VS -> uvicorn app.main:app --reload

# MySQL -> mysql -u root -p
# MySQL -> select user, host from mysql.user;
# MySQL -> show grants for root
# MySQL -> show databases;
# MySQL -> grant all on eda_bd.* to 'root'@'localhost';
# MySQL -> show grants for root@localhost;

# docker build -t my_fastapi .
# docker run -d --name my_dockerfastapi -p 8000:8000 my_fastapi
#   docker run --add-host=“eda_bd:127.0.0.1” --name my_dockerfastapi -p 5000:5000 my_fastapi

# docker stop $(docker ps -a -q)
# docker rm $(docker ps -a -q)
