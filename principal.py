import streamlit as st

if flag != True:
  lista = []
valor = st.number_input("Digite um numero")
if st.button("Inserir"):
  flag = True
  lista.append(valor)
st.write(lista)
