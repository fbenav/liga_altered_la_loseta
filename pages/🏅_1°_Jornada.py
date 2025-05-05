import pandas as pd
import plotly.express as px
import streamlit as st

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

df['Victorias'] = df['Record'].apply(lambda x: x.split('-')[0].strip()).astype(int)
df['Derrotas'] = df['Record'].apply(lambda x: x.split('-')[1].strip()).astype(int)
df['Empates'] = df['Record'].apply(lambda x: x.split('-')[2].strip()).astype(int)

df['Heroe'] = ['Fen', 'Afanas', 'Fen', 'Afanas']

uso_heroes = df.groupby('Heroe')['Victorias'].count().reset_index()
uso_heroes.columns = ['heroe', 'uso']


st.header('Liga Altered La loseta 02-05-2025')

st.dataframe(df.drop(columns = 'Record'), column_config={'_index': None})

fig = px.pie(uso_heroes, names="heroe", values="uso", title="Heroes utilizados en la jornada")

st.plotly_chart(fig, use_container_width=True)


