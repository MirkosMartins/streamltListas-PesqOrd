import streamlit as st

if 'flag' not in st.session_state:
  lista = []
valor = st.number_input("Digite um numero")
if st.button("Inserir"):
  lista = st.session_state['lista']#lendo a lista
  st.session_state['flag'] = False
  lista.append(valor)
  st.session_state['lista'] = lista #guardando a lista
st.write(lista)
