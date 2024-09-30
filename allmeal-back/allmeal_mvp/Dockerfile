# Dockerfile

# Usa la imagen base de Python
FROM python:3.12

# Establece el directorio de trabajo en /code
WORKDIR /code

# Copia el archivo de dependencias
COPY requirements.txt /code/

# Instala las dependencias
RUN pip install -r requirements.txt

# Copia el código fuente a la imagen
COPY . /code/

# Expone el puerto 8000 para el servidor de Django
EXPOSE 8000

# Comando para ejecutar el servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
