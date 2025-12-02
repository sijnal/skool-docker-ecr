# Usa una imagen base oficial de Python para la construcción
FROM python:3.13.7-alpine3.22

# Establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de dependencias (en este caso, requirements.txt)
COPY requirements.txt .

# Instala las dependencias en un entorno temporal
RUN pip install --no-cache-dir -r requirements.txt --target=/app/deps

# Establece la variable de entorno para que Python pueda encontrar las dependencias
ENV PYTHONPATH=/app/deps

# Copia el resto de la aplicación
COPY app.py /app/app.py

# Copia la carpeta de plantillas
COPY templates /app/templates

# Exponer el puerto en el que la aplicación escuchará
EXPOSE 80

# Define el comando por defecto para ejecutar el script
CMD ["python", "/app/app.py"]
