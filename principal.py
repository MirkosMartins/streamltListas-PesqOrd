import streamlit as st

lista = []
valor = st.number_input("Digite um numero")
if st.button("Inserir"):
  lista.append(valor)
st.write(lista)
