import streamlit as st
import funcoes

st.image("https://us-tuna-sounds-images.voicemod.net/6e51eaf0-b3e3-4969-b1ea-cac8c98b3544-1666472596440.jpg")
st.title("Meu site ❤️😊")
st.subheader("Criado com Streamlit")

st.markdown("""
# Bem Vindo ao meu site 😊\n
*Feito em Python*\n
**Dps vai ser em Javascript kkkkk** """)
st.title("Calculadora IMC")
massa = st.number_input("Digite sua massa",min_value=0.0)
altura = st.number_input("Digite sua altura",min_value=0.0)
btn_calcular = st.button("Calcular")
if btn_calcular:
    imc = funcoes.calcular_imc(massa, altura)
    st.success(imc)
if btn_calcular:
    st.success("Peso normal 😊")