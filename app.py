from flask import Flask
import psycopg2
import os

app = Flask(__name__)

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def conectar():
    return psycopg2.connect(
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

@app.route('/')
def home():
    try:
        conn = conectar()
        estado = "Conectado a PostgreSQL"
        conn.close()
    except:
        estado = "Error de conexión"

    return f"""
    <h1>{APP_NAME}</h1>
    <h2>Versión: {APP_VERSION}</h2>
    <h3>{estado}</h3>
    """

@app.route('/productos')
def productos():

    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM productos")
    datos = cur.fetchall()

    html = "<h1>Lista de Productos</h1><ul>"

    for p in datos:
        html += f"""
        <li>
        {p[0]} - {p[1]}
        Precio: ${p[2]}
        Stock: {p[3]}
        </li>
        """

    html += "</ul>"

    cur.close()
    conn.close()

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)