import streamlit as st
import pandas as pd


st.title("Сравнение саммаризации")
st.write("Для саммаризации использовалась модель YandexGPT c промптом `Сократи дневниковую запись`")

df = pd.read_csv(st.secrets["db_link"])


row_selection = st.selectbox('Выберите строку', df.index)
selected_row = df.loc[row_selection]

st.write(f"### id записи {selected_row['id']}")

col1, col2 = st.columns(2)

with col1:
    st.write(f"#### Оригинальный текст")
    st.write(selected_row['text'])
with col2:
    st.write(f"#### Текст после суммаризации")
    st.write(selected_row['summary'])   

