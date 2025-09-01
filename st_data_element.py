import streamlit as st
import pandas as pd

# Title
st.title("Data Element")

st.subheader("Data Pegawai")
df = pd.DataFrame({
    'Name': ["Farhan", "Rizky", "Dani", "Agus"],
    'Age': [20, 21, 19, 22],
    'Job Role': ["Data Scientist", "Data Analyst", "Data Engineer", "ML Engineer"] 
})

st.dataframe(df, hide_index=True)


st.subheader("Data Siswa")
df = pd.DataFrame({
    'Name': ["Rina", "Jeki", "Dewi", "Farhan"],
    'NISN': [123423,423142,532434,235342],
})
df_editable = st.data_editor(df, hide_index=True)
print(df_editable)

st.subheader("Data Mahasiswa")
df = pd.DataFrame({
    'Name': ["Jaka", "raihana", "peka", "rara"],
    'NISN': [433243123,653243123,1232467123,123262863],
})
st.table(df)

# Metric
st.subheader("Metric")
st.metric("Temperature", "70 °F", "-1.2 °F")

# Metric
st.subheader("Data JSON")
st.json({
    "name": "Farhan",
    "age": 20,
    "city": "Jakarta"
})
