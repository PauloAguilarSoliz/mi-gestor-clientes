import sqlite3


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
    except Exception as e:
        print(f"Error al registrar: {e}")
        return False


def obtener_clientes():
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM clientes")
        filas = cursor.fetchall()
        conexion.close()
        return filas
    except Exception as e:
        print(f"Error al consultar: {e}")
        return []


def borrar_cliente(id_cliente):
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()
        # Eliminamos basándonos en el ID único
        cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al borrar: {e}")
        return False


def modificar_cliente(id_cliente, nuevo_nombre, nuevo_servicio, nuevo_presupuesto):
    try:
        conexion = sqlite3.connect("proyectos.db")
        cursor = conexion.cursor()

        # El comando UPDATE cambia los valores en la fila donde coincida el ID
        cursor.execute(
            """
            UPDATE clientes 
            SET nombre = ?, servicio = ?, presupuesto = ? 
            WHERE id = ?
        """,
            (nuevo_nombre, nuevo_servicio, nuevo_presupuesto, id_cliente),
        )

        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print(f"Error al modificar: {e}")
        return False


def generar_reporte_txt():
    try:
        clientes = obtener_clientes()
        # "w" significa write (escribir). Crea el archivo si no existe.
        with open("reporte_clientes.txt", "w", encoding="utf-8") as archivo:
            archivo.write("===========================================\n")
            archivo.write("   REPORTE DE CLIENTES - PORTAFOLIO\n")
            archivo.write("===========================================\n\n")
            archivo.write(f"{'ID':<5} {'NOMBRE':<20} {'SERVICIO':<15} {'MONTO':<10}\n")
            archivo.write("-" * 55 + "\n")

            total_presupuesto = 0
            for c in clientes:
                archivo.write(f"{c[0]:<5} {c[1]:<20} {c[2]:<15} ${c[3]:<10.2f}\n")
                total_presupuesto += c[3]

            archivo.write("\n" + "-" * 55 + "\n")
            archivo.write(
                f"TOTAL DE PRESUPUESTOS ACUMULADOS: ${total_presupuesto:.2f}\n"
            )
            archivo.write("\nGenerado automáticamente por GestorTech v1.1")
        return True
    except Exception as e:
        print(f"Error al generar reporte: {e}")
        return False
