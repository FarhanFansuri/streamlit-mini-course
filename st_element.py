import streamlit as st

st.write("Halo, ini teks biasa.")
st.write(12345)
st.write({"nama": "Farhan", "usia": 23})

st.title("Judul Utama")       # Ukuran paling besar
st.header("Header")           # Lebih kecil dari title
st.subheader("Subheader")     # Lebih kecil lagi

st.text("Ini teks plain.")

st.markdown("**Tebal**, *Miring*, [Link](https://streamlit.io)")
st.markdown("""
- List item 1
- List item 2
""")

st.caption("Ini caption atau catatan kecil.")

st.code("print('Hello World')", language="python")

st.latex(r"E = mc^2")
st.latex(r"\frac{a}{b} = c")
