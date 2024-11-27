import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar archivo
path = "E:\\TripleTen\\Data Scients\\Sprint_7\\Proyecto\\"
archivo = path + 'vehicles_us.csv'

# Manejo de errores al cargar el archivo
try:
    data_base = pd.read_csv(archivo)
except FileNotFoundError:
    st.error("El archivo no se encuentra en la ruta especificada.")
    st.stop()
except pd.errors.EmptyDataError:
    st.error("El archivo está vacío.")
    st.stop()
except Exception as e:
    st.error(f"Ocurrió un error al cargar el archivo: {e}")
    st.stop()

# Título de la aplicación
st.title("Análisis de Vehículos Usados")
st.write("Explora el conjunto de datos mediante gráficos interactivos.")

# Marcador de posición para los gráficos
placeholder = st.empty()

# Selección de columnas para el histograma
columnas_disponibles = [col for col in data_base.columns if data_base[col].dtype in ['int64', 'float64']]
odometer_column = st.selectbox('Selecciona la columna para el histograma:', columnas_disponibles)

# Botón para construir un histograma
if st.button('Construir Histograma'):
    st.write('Creación de histograma para el conjunto de datos')
    fig = px.histogram(data_base, x=odometer_column, title=f"Histograma de {odometer_column}")
    placeholder.plotly_chart(fig, use_container_width=True)


# Botón para limpiar gráficos
if st.button('Limpiar Gráficos'):
    placeholder.empty()
    st.write("¡Gráficos limpiados!")

# Instrucciones para el usuario
st.write("Utiliza los botones para generar diferentes gráficos a partir del conjunto de datos.")
