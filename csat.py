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

class CSatIQT:
  def __init__(self, url="https://docs.google.com/spreadsheets/d/1qjfkA6CiKu47ys1B7NhV1FYx4VlW67ZEHwKg9GRvQPw/pub?gid=1171079915&single=true&output=csv"):
    self.url = url
    rD = requests.get(self.url)
    dataD = rD.content
    db = pd.read_csv(BytesIO(dataD), index_col=0)
    db.columns = ['ID', 'N1', 'N2', 'N3', 'N4']
    db['ID'].fillna('', inplace=True)
    db['N1'].fillna('', inplace=True)
    db['N2'].fillna('', inplace=True)
    db['N3'].fillna('', inplace=True)
    db['N4'].fillna('', inplace=True)
    self.DATAFRAME = db

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

    NotaFinalSalgado = 0
    for i in range(len(NotaSalgado)):
      if i == 0:
        NotaFinalSalgado += (0*NotaSalgado[0])
      elif i == 1:
        NotaFinalSalgado += (1*NotaSalgado[1])
      elif i == 2:
        NotaFinalSalgado +=  (2*NotaSalgado[2])
      elif i == 3:
        NotaFinalSalgado += (3*NotaSalgado[3])
      elif i == 4:
        NotaFinalSalgado += (4*NotaSalgado[4])
      elif i == 5:
        NotaFinalSalgado += (5*NotaSalgado[5])

    #print('\nNOTAS REFRI: ')
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

    NotaFinalRefri = 0
    for i in range(len(NotaRefri)):
      if i == 0:
        NotaFinalRefri += (0*NotaRefri[0])
      elif i == 1:
        NotaFinalRefri += (1*NotaRefri[1])
      elif i == 2:
        NotaFinalRefri +=  (2*NotaRefri[2])
      elif i == 3:
        NotaFinalRefri += (3*NotaRefri[3])
      elif i == 4:
        NotaFinalRefri += (4*NotaRefri[4])
      elif i == 5:
        NotaFinalRefri += (5*NotaRefri[5])

    #print('\nNOTAS BOLO: ')
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

    NotaFinalBolo = 0
    for i in range(len(NotaBolo)):
      if i == 0:
        NotaFinalBolo += (0*NotaBolo[0])
      elif i == 1:
        NotaFinalBolo += (1*NotaBolo[1])
      elif i == 2:
        NotaFinalBolo +=  (2*NotaBolo[2])
      elif i == 3:
        NotaFinalBolo += (3*NotaBolo[3])
      elif i == 4:
        NotaFinalBolo += (4*NotaBolo[4])
      elif i == 5:
        NotaFinalBolo += (5*NotaBolo[5])

    df2 = df.astype(int)

    DesvPAD_Salgado = df2['Salgado'].std()
    if DesvPAD_Salgado == 0.0:
      DesvPAD_Salgado = 0.1
    DesvPAD_Refri = df2['Refri'].std()
    if DesvPAD_Refri == 0.0:
      DesvPAD_Refri = 0.1
    DesvPAD_Bolo = df2['Bolo'].std()
    if DesvPAD_Bolo == 0.0:
      DesvPAD_Bolo = 0.1

  def ExibirDF(self):
    display(self.DATAFRAME)

  def NotaSalgado(self):
    return NotaSalgado

  def NotaRefri(self):
    return NotaRefri

  def NotaBolo(self):
    return NotaBolo

  def DesvPAD_Salgado(self):
    return DesvPAD_Salgado

  def DesvPAD_Refri(self):
    return DesvPAD_Refri

  def DesvPAD_Bolo(self):
    return DesvPAD_Bolo

  def CalcularIQT(self):
    return round(NotaFinalSalgado/DesvPAD_Salgado + NotaFinalRefri/DesvPAD_Refri + NotaFinalBolo/DesvPAD_Bolo, 3)

  def NotaFinalSalgado(self):
    return round(NotaFinalSalgado/DesvPAD_Salgado, 3)

  def NotaFinalRefri(self):
    return round(NotaFinalRefri/DesvPAD_Refri, 3)

  def NotaFinalBolo(self):
    return round(NotaFinalBolo/DesvPAD_Bolo, 3)


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
st.dataframe(db) 
Csat = CSatIQT("https://docs.google.com/spreadsheets/d/1qjfkA6CiKu47ys1B7NhV1FYx4VlW67ZEHwKg9GRvQPw/pub?gid=1171079915&single=true&output=csv")
st.write(Csat.NotaSalgado())
st.write(Csat.NotaRefri())
st.write(Csat.NotaBolo())
