import streamlit as st

flag
if flag != False:
  lista = []
valor = st.number_input("Digite um numero")
if st.button("Inserir"):
  flag = False
  lista.append(valor)
st.write(lista)
