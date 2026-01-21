import sqlite3

def crear_base_datos():
    # Conecta (o crea) el archivo. No consume RAM extra.
    conexion = sqlite3.connect("proyectos.db")
    cursor = conexion.cursor()
    
    # Creamos la tabla si no existe
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            servicio TEXT,
            presupuesto REAL
        )
    ''')
    
    conexion.commit()
    conexion.close()
    print("Base de datos e infraestructura lista.")