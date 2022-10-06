import streamlit as st

if 'flag' not in st.session_state:
  lista = []
valor = st.number_input("Digite um numero")
if st.button("Inserir"):
  st.session_state['flag'] = False
  lista.append(valor)
st.write(lista)
