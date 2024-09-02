import streamlit as st
#from streamlit_text_rating.st_text_rater import st_text_rater
import sqlite3
import pandas as pd
import numpy as np
import time
import datetime
import requests
from io import BytesIO
import urllib3
from urllib3 import request
#from PIL import Image # Lib para carregar imagem no Streamlit

resp = None
LIKED = 0
DISLIKED = 0
    
#MENU E CONFIGURAÇÕES DA PÁGINA
ajuda = "https://docs.streamlit.io" 
bug = "mailto:massaki.igarashi@sp.senai.br"
sobre = '''      
        **Desenvolvido por Massaki Igarashi**
               
        DICAS DE UTILIZAÇÃO:
               
        **- Passo 1:**  Responda a Pesquisa de Satisfação   
        **- Passo 2:**  Acesse o Painel Analítico do
                        Índice de Qualidade da Taioba - IQT                                                        
        '''
                
icone = "©️"
st.set_page_config(layout="wide", 
page_title="IQT SENAI R. MANGE",
initial_sidebar_state = "auto",
menu_items={'Get Help': (ajuda),
            'Report a bug': (bug),
            'About': (sobre)},
            page_icon=icone)

st.title("Índice de Qualidade da Taioba - IQT")