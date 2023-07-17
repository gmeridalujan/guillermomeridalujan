# Pruebas

import streamlit as st
import pandas as pd
import numpy as np

# Generar datos simulados
np.random.seed(42)
data = pd.DataFrame({
    'Fecha': pd.date_range('2023-01-01', '2023-12-31', freq='D'),
    'Ventas': np.random.randint(100, 1000, size=365),
    'Ganancias': np.random.uniform(500, 5000, size=365)
})

# Convertir el tipo de dato de la columna 'Fecha' a date
data['Fecha'] = data['Fecha'].dt.date

# Configurar la barra lateral
st.sidebar.title('Opciones')
filtro_fecha = st.sidebar.date_input('Seleccionar fecha', [data['Fecha'].min(), data['Fecha'].max()])

# Filtrar los datos según la fecha seleccionada
data_filtrada = data[(data['Fecha'] >= filtro_fecha[0]) & (data['Fecha'] <= filtro_fecha[1])]

# Mostrar los datos filtrados en una tabla
st.write('## Datos Filtrados')
st.dataframe(data_filtrada)

# Gráfico de ventas diarias
st.write('## Ventas Diarias')
st.line_chart(data_filtrada['Ventas'])

# Gráfico de ganancias diarias
st.write('## Ganancias Diarias')
st.line_chart(data_filtrada['Ganancias'])