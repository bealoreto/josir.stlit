import streamlit as st
import pandas as pd

st.write("""
# My first app
Hello *world*
""")

nome = st.text_input('Digite o seu nome: ')
if len(nome) > 0:
  st.write ('Que nome maneiro!')

idade = st.text_input('Digite a sua idade: ')
if len(idade) > 0:
  st.write ('Na flor da idade...')

altura = st.text_input('Digite a sua altura: ')
if len(altura) > 0:
  st.write ('A altura perfeita :)')
