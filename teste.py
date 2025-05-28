import pandas as pd
import streamlit as st
import requests 
import json

st.write ("""
# Oportunidades para dançarinos 
Você vive da dança e quer encontrar oportunidade de trabalho? Aqui é *seu lugar*!
""")
cidade = st.text_input('Digite o código da cidade: ')
if len(cidade) > 0:
  st.write ('Ok!')
data = st.text_input('Digite o período de interesse: ')
if len(data) > 0:
    st.write ('Ok!')


url= 'https://queridodiario.ok.org.br/api/gazettes?territory_ids=3304557&published_since=2025-01-01&querystring=dan%C3%A7a&excerpt_size=1000&number_of_excerpts=1&pre_tags=&post_tags=&size=10&sort_by=relevance'
response = requests.get(url)

st.subheader(f'Foram encontrados {response.json()["total_gazettes"]} entradas no diário oficial')

st.write(response.json())


for resultado in response.json()['gazettes'][:10]:
    st.write("Data:", resultado["date"])
    for excerpt in resultado['excerpts']:
        st.write(excerpt)
        st.write('---')
