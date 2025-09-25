import streamlit as st

mph = st.number_input("Digite o valor da sua hora: ", min_value=0.0)
hpm = st.number_input("Digite quantas horas você trabalhou esse mes: ", min_value=0.0)


btn_calcular = st.button("Calcular")
if btn_calcular:
    calc = mph * hpm
    st.text_area("")