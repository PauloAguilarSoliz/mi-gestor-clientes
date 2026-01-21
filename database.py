import sqlite3

def crear_base_datos():
    conexion = sqlite3.connect("proyectos.db")
    cursor = conexion.cursor()
    
    # Tabla Maestra de Clientes
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            servicio TEXT,
            presupuesto REAL
        )
    ''')
    
    # Tabla Relacionada de Pagos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pagos (
            id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER,
            monto_pago REAL,
            fecha TEXT,
            FOREIGN KEY (id_cliente) REFERENCES clientes (id)
        )
    ''')
    
    conexion.commit()
    conexion.close()
