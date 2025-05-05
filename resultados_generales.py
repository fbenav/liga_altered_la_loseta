import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Resultados Generales",
    page_icon="🏆"
)

data_05_02 = {
    "Position": [1, 2, 3, 4],
    "Player": ["Darkshadow - Fen", "ZarpMH - Afanas", "Tharmys - no participa de liga", "Mattstrife - afanas"],
    "Record": ["2 - 1 - 0", "2 - 1 - 0", "1 - 2 - 0", "1 - 2 - 0"],
    "OMW%": [44.44, 44.44, 55.56, 55.56],
    "GW%": [66.67, 66.67, 33.33, 33.33],
    "OGW%": [44.44, 44.44, 55.56, 55.56]
}

df = pd.DataFrame(data_05_02)
df['Heroe'] = df['Player'].apply(lambda x: x.split('-')[-1].strip())
df['Player'] = df['Player'].apply(lambda x: x.split('-')[0].strip())

st.header('🏆 Liga la Loseta: Resultados Generales')

st.sidebar.success("Elije una jornada arriba!")

st.dataframe(df[['Position','Player']], column_config={'_index': None})
