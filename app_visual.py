import streamlit as st
import logic
from database import crear_base_datos

# Configuración de la página
st.set_page_config(page_title="Mi Gestor Tech", layout="centered")
crear_base_datos()

st.title("🚀 Mi Gestor de Clientes")
st.write("Bienvenido a tu aplicación profesional de portafolio.")

# --- BARRA LATERAL (MENÚ) ---
menu = st.sidebar.selectbox(
    "Selecciona una opción",
    ["Ver Clientes", "Registrar Nuevo", "Modificar/Eliminar", "Reportes"],
)

# --- LÓGICA DE LAS OPCIONES ---
if menu == "Ver Clientes":
    st.header("📋 Lista de Clientes")
    clientes = logic.obtener_clientes()
    if clientes:
        # Mostramos los datos en una tabla visual hermosa
        st.table(clientes)
    else:
        st.warning("No hay clientes registrados.")

elif menu == "Registrar Nuevo":
    st.header("📝 Registro")
    with st.form("form_registro"):
        nombre = st.text_input("Nombre del Cliente")
        servicio = st.text_input("Servicio")
        presupuesto = st.number_input("Presupuesto", min_value=0.0)
        btn_guardar = st.form_submit_button("Guardar Cliente")

        if btn_guardar:
            if logic.registrar_cliente(nombre, servicio, presupuesto):
                st.success(f"¡{nombre} registrado con éxito!")
            else:
                st.error("Error al guardar.")

elif menu == "Modificar/Eliminar":
    st.header("⚙️ Gestión de Datos")
    id_cliente = st.number_input("Ingresa el ID del cliente", step=1)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Eliminar Cliente"):
            if logic.borrar_cliente(id_cliente):
                st.success("Cliente eliminado.")
    with col2:
        st.info(
            "Para modificar, usa la opción de Registro y luego borra el anterior (v1.1)"
        )

elif menu == "Reportes":
    st.header("📊 Generar Reporte")
    if st.button("Descargar Reporte TXT"):
        if logic.generar_reporte_txt():
            st.success("Reporte generado en la carpeta del proyecto.")
