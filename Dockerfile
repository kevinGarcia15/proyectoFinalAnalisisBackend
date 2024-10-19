# syntax=docker/dockerfile:1
FROM python:3.6-alpine

# Configuración para que Python no genere archivos bytecode
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dotenv para la configuración de variables de entorno
RUN pip install python-dotenv

# Actualizar los paquetes e instalar las dependencias necesarias
RUN apk update \
  # Dependencias para compilar y MySQL
  && apk add --virtual build-deps gcc python3-dev musl-dev \
  && apk add mariadb-dev \
  # Dependencias de Pillow
  && apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev \
  # Dependencias de CFFI (si las necesitas)
  && apk add libffi-dev py-cffi \
  # Dependencias de traducción
  && apk add gettext \
  # Cliente MySQL opcional (para ejecutar comandos MySQL desde el contenedor)
  && apk add mysql-client

# Establecer el directorio de trabajo en /code
WORKDIR /code

# Copiar el archivo de requisitos
COPY requirements/requirements_local.txt /code/

# Instalar las dependencias desde requirements_local.txt
RUN python -m pip install -r requirements_local.txt

# Copiar el resto del código al contenedor
COPY . /code/
