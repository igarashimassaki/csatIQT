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

def exibir():
    conn = sqlite3.connect('bdCSatIQT.db')
    cursor = conn.execute(""" SELECT * FROM BDIQT""")
    rows = cursor.fetchall()
    VetorDados = []
    for row in cursor:
       #st.write("ID: ", row[0])
       #st.write("LIKED: ", row[1])
       #st.write("DISLIKED: ", row[2])
       VetorDados.append(row[0])
       VetorDados.append(row[1])
       VetorDados.append(row[2])
    if len(rows) != 0:
        db = pd.DataFrame(rows)    
        db.columns = ['ID' , 'LIKED' , 'DISLIKED']
        #st.dataframe(db)
        QTDlike = sum(db['LIKED'])
        QTDdisliked = sum(db['DISLIKED'])
        PorcentLIKE = round(100*QTDlike/(QTDlike+QTDdisliked), 1)
        PorcentDISLIKE = round(100*QTDdisliked/(QTDlike+QTDdisliked), 1)
        colA, colB, colC, colD = st.columns(4)
        with colA:
            st.write('')
        with colB:        
            #st.write(QTDlike, " Gostaram do IQT")
            st.write(QTDlike, "(", PorcentLIKE, "% )", "Gostaram")
        with colC:
            st.write(QTDdisliked, "(", PorcentDISLIKE, "% )", "Não Gostaram")
        with colD:
            st.write('')
    conn.close()
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
urlCSV = "https://docs.google.com/spreadsheets/d/1qjfkA6CiKu47ys1B7NhV1FYx4VlW67ZEHwKg9GRvQPw/pub?gid=1171079915&single=true&output=csv"
rD = requests.get(urlCSV)
dataD = rD.content
db = pd.read_csv(BytesIO(dataD), index_col=0)
#st.dataframe(db) 

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.write('')
with col2:
    st.write('')
with col3:
    resp = st_text_rater("Gostou?")
#st.write(f"Resposta: {resp}")
if resp == "liked":
    LIKED = 1
else:
    DISLIKED = 1
with col4:
    st.write('')
with col5:
    st.write('')
#1º)Para criar um banco de dados SQL , usamos o seguinte comando:
conn = sqlite3.connect('bdCSatIQT.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS BDIQT(ID INT PRIMARY KEY NOT NULL, 
                                                    LIKED INT NOT NULL,
                                                    DISLIKED INT NOT NULL);''')
conn.close()

#2º)INSERT data and READ this data
#Following Python program shows how to create records in the COMPANY table created in the above example.
conn = sqlite3.connect('bdCSatIQT.db')
#if st.button('Salvar'):
if resp !=None:
    current_datetime = datetime.datetime.now()
    timestamp = current_datetime.timestamp()
    conn.execute("""INSERT INTO BDIQT (ID, LIKED, DISLIKED) \
                                        VALUES (?,?,?)
                                        """, (timestamp, LIKED, DISLIKED))
    conn.commit()
    #st.write("Records created successfully")
    conn.close()
    exibir() 
