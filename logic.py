import sqlite3


# --- FUNCIONES DE CLIENTES ---
def registrar_cliente(nombre, servicio, presupuesto):
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, servicio, presupuesto) VALUES (?, ?, ?)",
            (nombre, servicio, presupuesto),
        )
        conexion.commit()
        conexion.close()
        return True
    except:
        return False


def obtener_clientes():
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        filas = cursor.fetchall()
        conexion.close()
        return filas
    except:
        return []


def borrar_cliente(id_cliente):
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        conexion.commit()
        conexion.close()
        return True
    except:
        return False


# --- FUNCIONES DE PAGOS (RELACIONALES) ---
def registrar_pago(id_cliente, monto, fecha):
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO pagos (id_cliente, monto_pago, fecha) VALUES (?, ?, ?)",
            (id_cliente, monto, fecha),
        )
        conexion.commit()
        conexion.close()
        return True
    except:
        return False


def obtener_pagos_detallados():
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()
        # Une las tablas para mostrar el NOMBRE del cliente en lugar de solo su ID
        query = """
            SELECT clientes.nombre, pagos.monto_pago, pagos.fecha
            FROM pagos
            INNER JOIN clientes ON pagos.id_cliente = clientes.id
        """
        cursor.execute(query)
        filas = cursor.fetchall()
        conexion.close()
        return filas
    except:
        return []


# --- REPORTE ---
def generar_reporte_txt():
    try:
        clientes = obtener_clientes()
        with open("reporte_clientes.txt", "w", encoding="utf-8") as f:
            f.write("REPORTE PROFESIONAL DE CLIENTES\n\n")
            for c in clientes:
                f.write(f"ID: {c[0]} | Cliente: {c[1]} | Presupuesto: ${c[3]}\n")
        return True
    except:
        return False


def obtener_pagos_detallados():
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()
        query = """
            SELECT clientes.nombre, pagos.monto_pago, pagos.fecha
            FROM pagos
            INNER JOIN clientes ON pagos.id_cliente = clientes.id
        """
        cursor.execute(query)
        filas = cursor.fetchall()
        conexion.close()
        return filas
    except:
        return []
