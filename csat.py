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
from PIL import Image # Lib para carregar imagem no Streamlit

def AtribuiNota(Csat):
  if Csat == 'Gosto Horrível':
    return '1'
  elif Csat == 'Não Gostei':
    return '2'
  elif Csat == 'Indiferente':
    return '3'
  elif Csat == 'Gostei':
    return '4'
  elif Csat == 'Amei':
    return '5'
  else:
    return '0'

def NotaPrazo(resp):
  if resp == 'Sim':
    return '5'
  else:
    return '0'

def CalculaCSat(Notas1, Notas2, Notas3):
  QTDrespostas = sum(Notas1) + sum(Notas2) + sum(Notas3)
  #print("QTDrespostas = ", QTDrespostas)
  Ndetratores = Notas1[1] + Notas2[1] + Notas3[1]
  #print("Ndetratores = ", Ndetratores)
  Nsatisfeitos = Notas1[4] + Notas2[4] + Notas3[4] + Notas1[5] + Notas2[5] + Notas3[5]
  #print("Nsatisfeitos = ", Nsatisfeitos)
  PorcentDETRATORES = (Ndetratores/QTDrespostas)*100
  CSatpropotores = round((Nsatisfeitos/QTDrespostas)*100, 3)
  return CSatpropotores, Nsatisfeitos, Ndetratores, QTDrespostas

def IQT_CSat_Taioba(urlCSV = "https://docs.google.com/spreadsheets/d/1qjfkA6CiKu47ys1B7NhV1FYx4VlW67ZEHwKg9GRvQPw/pub?gid=1171079915&single=true&output=csv"):
  rD = requests.get(urlCSV)
  dataD = rD.content
  db = pd.read_csv(BytesIO(dataD), index_col=0)
  db.columns = ['ID', 'N1', 'N2', 'N3', 'N4']
  db['ID'].fillna('', inplace=True)
  db['N1'].fillna('', inplace=True)
  db['N2'].fillna('', inplace=True)
  db['N3'].fillna('', inplace=True)
  db['N4'].fillna('', inplace=True)
  n = len(db)
  Salgado = []
  Refi = []
  Bolo = []
  Prazo = []
  for i in range(n):
    Salgado.append(AtribuiNota(db.iloc[i,1]))
    Refi.append(AtribuiNota(db.iloc[i,2]))
    Bolo.append(AtribuiNota(db.iloc[i,3]))
    Prazo.append(NotaPrazo(db.iloc[i,4]))
  df = pd.DataFrame({'Salgado': Salgado, 'Refri': Refi, 'Bolo': Bolo, 'Prazo': Prazo})

  NotaSalgado = []
  SalgadoNota0 = df[df['Salgado'].str.contains('0')]
  NotaSalgado.append(len(SalgadoNota0))
  SalgadoNota1 = df[df['Salgado'].str.contains('1')]
  NotaSalgado.append(len(SalgadoNota1))
  SalgadoNota2 = df[df['Salgado'].str.contains('2')]
  NotaSalgado.append(len(SalgadoNota2))
  SalgadoNota3 = df[df['Salgado'].str.contains('3')]
  NotaSalgado.append(len(SalgadoNota3))
  SalgadoNota4 = df[df['Salgado'].str.contains('4')]
  NotaSalgado.append(len(SalgadoNota4))
  SalgadoNota5 = df[df['Salgado'].str.contains('5')]
  NotaSalgado.append(len(SalgadoNota5))

  NotaRefri = []
  RefriNota0 = df[df['Refri'].str.contains('0')]
  NotaRefri.append(len(RefriNota0))
  RefriNota1 = df[df['Refri'].str.contains('1')]
  NotaRefri.append(len(RefriNota1))
  RefriNota2 = df[df['Refri'].str.contains('2')]
  NotaRefri.append(len(RefriNota2))
  RefriNota3 = df[df['Refri'].str.contains('3')]
  NotaRefri.append(len(RefriNota3))
  RefriNota4 = df[df['Refri'].str.contains('4')]
  NotaRefri.append(len(RefriNota4))
  RefriNota5 = df[df['Refri'].str.contains('5')]
  NotaRefri.append(len(RefriNota5))

  NotaBolo = []
  BoloNota0 = df[df['Bolo'].str.contains('0')]
  NotaBolo.append(len(BoloNota0))
  BoloNota1 = df[df['Bolo'].str.contains('1')]
  NotaBolo.append(len(BoloNota1))
  BoloNota2 = df[df['Bolo'].str.contains('2')]
  NotaBolo.append(len(BoloNota2))
  BoloNota3 = df[df['Bolo'].str.contains('3')]
  NotaBolo.append(len(BoloNota3))
  BoloNota4 = df[df['Bolo'].str.contains('4')]
  NotaBolo.append(len(BoloNota4))
  BoloNota5 = df[df['Bolo'].str.contains('5')]
  NotaBolo.append(len(BoloNota5))

  CSAT, Nsat, Ndet, QTDresp = CalculaCSat(NotaSalgado, NotaRefri, NotaBolo)

  return CSAT, Nsat, Ndet, QTDresp

def main():
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
  st.set_page_config(layout="centered", 
  page_title="IQT SENAI R. MANGE",
  initial_sidebar_state = "auto",
  menu_items={'Get Help': (ajuda),
              'Report a bug': (bug),
              'About': (sobre)},
              page_icon=icone)
  
  st.title("Índice de Qualidade da Taioba - IQT")

  IQT, Nsat, Ndet, QTDresp = IQT_CSat_Taioba(urlCSV = "https://docs.google.com/spreadsheets/d/1qjfkA6CiKu47ys1B7NhV1FYx4VlW67ZEHwKg9GRvQPw/pub?gid=1171079915&single=true&output=csv")
  tab1, tab2 = st.tabs(["Indicador", "Auditar Dados"])
  image = Image.open('FUNDO.png')   
  with tab1:
    ColunasA = st.columns(3) 
    with ColunasA[0]:
      with st.container(height=None, border=True):
        st.metric("Nª Satisfeitos", Nsat, "Satisfeitos")
    with ColunasA[1]:
      with st.container(height=None, border=True):
        st.metric("IQT", IQT, "Índice de Qualidade da Taioba")
    with ColunasA[2]:
      with st.container(height=None, border=True):
        st.metric("Nª Insatisfeitos", Ndet, "-Insatisfeitos")  
    
    ColunasB = st.columns(3)  
    with ColunasB[0]:
      st.write("")
    with ColunasB[1]:
      st.write("TOTAL de respondentes = ", QTDresp)    
    with ColunasB[2]:
      st.write("") 
    st.image(image, width=680, caption='')
  with tab2:   
    st.title("Auditoria dos Dados")
  
if __name__ == '__main__':
	main()
