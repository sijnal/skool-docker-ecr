from flask import Flask, render_template
import os
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Configuración de la conexión a la base de datos
def get_db_connection():
    db_host = os.getenv('DB_HOST', 'localhost')
    
    # Solo se conecta si el host no es 'localhost'
    if db_host != 'localhost':
        conn = mysql.connector.connect(
            host=db_host,
            port=os.getenv('DB_PORT', '3306'),
            user=os.getenv('DB_USER', 'db_user'),
            password=os.getenv('DB_PASSWORD', 'db_password'), 
            database=os.getenv('DB_NAME', 'db_name')
        )
        return conn
    else:
        return None
    
# Ruta principal (index)
@app.route('/')
def index():
    title = os.getenv('TITLE', 'Not-Title')
    microservice = os.getenv('MICROSERVICIO', 'Not-Microservice')
    hostname = os.getenv('HOSTNAME', 'localhost')
    environment = os.getenv('ENVIRONMENT', 'development')
    version = os.getenv('VERSION', '1.0.0')
    
    # Obtenemos la hora actual
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Intentamos conectarnos a la base de datos
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")  # Consulta SQL para mostrar tablas en MySQL
        tables = cursor.fetchall()
        table_list = [table[0] for table in tables]  # Extraer los nombres de las tablas
        cursor.close()
        conn.close()
    else:
        table_list = []  # No hay tablas si no hay conexión a la BD

    # Renderizamos la plantilla HTML y le pasamos los valores
    return render_template('index.html', 
                           title=title, 
                           microservice=microservice, 
                           hostname=hostname, 
                           current_time=current_time,
                           db_host=os.getenv('DB_HOST', 'localhost'),
                           db_port=os.getenv('DB_PORT'),
                           db_user=os.getenv('DB_USER'),
                           db_name=os.getenv('DB_NAME'),
                           tables=table_list,
                           environment=environment,
                           version=version)

# Ruta para manejar errores HTTP con números
@app.route('/error/<int:error_code>')
def handle_error(error_code):
    error_messages = {
        400: {'message': '400 Bad Request', 'description': 'Hola a todos, soy un tipo chill v2'},
        401: {'message': '401 Unauthorized', 'description': 'Authentication failed or user does not have permissions for the desired action.'},
        403: {'message': '403 Forbidden', 'description': 'Access denied due to insufficient privileges.'},
        404: {'message': '404 Not Found', 'description': 'The requested resource could not be found.'},
        409: {'message': '409 Conflict', 'description': 'A conflict occurred with the current state of the resource.'},
        500: {'message': '500 Internal Server Error', 'description': 'An unexpected error occurred on the server.'},
        501: {'message': '501 Not Implemented', 'description': 'The server does not support the functionality required to fulfill the request.'},
        502: {'message': '502 Bad Gateway', 'description': 'The server received an invalid response from an upstream server.'},
        503: {'message': '503 Service Unavailable', 'description': 'The server is currently unable to handle the request due to a temporary overload or maintenance.'},
        504: {'message': '504 Gateway Timeout', 'description': 'The server did not receive a timely response from an upstream server.'}
    }

    error = error_messages.get(error_code, {'message': 'Unknown Error', 'description': 'An unknown error occurred.'})
    
    return render_template('error.html', error_code=error_code, message=error['message'], description=error['description']), error_code


# Hacer que cualquier otra ruta devuelva el mismo contenido que el index
@app.route('/<path:path>')
def catch_all(path):
    return index()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
