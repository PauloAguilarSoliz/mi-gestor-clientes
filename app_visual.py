import streamlit as st
import logic
from database import crear_base_datos

st.set_page_config(page_title="Gestor Tech Pro", layout="wide")
crear_base_datos()

st.title("🚀 Sistema de Gestión Empresarial")

menu = st.sidebar.selectbox(
    "Menú Principal",
    ["Dashboard Clientes", "Registrar Pago", "Reportes y Configuración"],
)

if menu == "Dashboard Clientes":
    col1, col2 = st.columns([2, 1])

    with col1:
        st.header("👥 Clientes Activos")
        clientes = logic.obtener_clientes()
        st.dataframe(
            clientes,
            column_config={
                "0": "ID",
                "1": "Nombre",
                "2": "Servicio",
                "3": "Presupuesto",
            },
            use_container_width=True,
        )

    with col2:
        st.header("➕ Nuevo Cliente")
        with st.form("reg"):
            nom = st.text_input("Nombre")
            ser = st.text_input("Servicio")
            pre = st.number_input("Presupuesto", min_value=0.0)
            if st.form_submit_button("Registrar"):
                logic.registrar_cliente(nom, ser, pre)
                st.rerun()

elif menu == "Registrar Pago":
    st.header("💰 Gestión de Pagos Relacionados")
    c1, c2 = st.columns(2)

    with c1:
        with st.form("pago"):
            id_c = st.number_input("ID del Cliente", step=1)
            mon = st.number_input("Monto del Pago", min_value=0.0)
            fec = st.date_input("Fecha")
            if st.form_submit_button("Vincular Pago"):
                if logic.registrar_pago(id_c, mon, str(fec)):
                    st.success("Pago registrado")

    with c2:
        st.subheader("Historial de Pagos (INNER JOIN)")
        pagos = logic.obtener_pagos_detallados()
        st.table(pagos)

elif menu == "Reportes y Configuración":
    if st.button("Generar Reporte Maestro .txt"):
        logic.generar_reporte_txt()
        st.success("Archivo generado en el servidor.")

    st.divider()
    id_del = st.number_input("ID para eliminar cliente", step=1)
    if st.button("Eliminar permanentemente"):
        logic.borrar_cliente(id_del)
        st.warning("Cliente eliminado.")
