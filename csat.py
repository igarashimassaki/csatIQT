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

def CalculaCSat(Notas1, Notas2, Notas3):
  QTDrespostas = sum(Notas1) + sum(Notas2) + sum(Notas3)
  Ndetratores = Notas1[1] + Notas2[1] + Notas3[1]
  Nsatisfeitos = Notas1[4] + Notas2[4] + Notas3[4] + Notas1[5] + Notas2[5] + Notas3[5]
  PorcentDETRATORES = (Ndetratores/QTDrespostas)*100
  CSatpropotores = (Nsatisfeitos/QTDrespostas)*100
  return CSatpropotores

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
df2 = df.astype(int)
st.write(df)

#print('NOTAS SALGADO: ')
NotaSalgado = []
SalgadoNota0 = df[df['Salgado'].str.contains('0')]
#print("Nota 0 = ", len(SalgadoNota0))
NotaSalgado.append(len(SalgadoNota0))
SalgadoNota1 = df[df['Salgado'].str.contains('1')]
#print("Nota 1 = ", len(SalgadoNota1))
NotaSalgado.append(len(SalgadoNota1))
SalgadoNota2 = df[df['Salgado'].str.contains('2')]
#print("Nota 2 = ", len(SalgadoNota2))
NotaSalgado.append(len(SalgadoNota2))
SalgadoNota3 = df[df['Salgado'].str.contains('3')]
#print("Nota 3 = ", len(SalgadoNota3))
NotaSalgado.append(len(SalgadoNota3))
SalgadoNota4 = df[df['Salgado'].str.contains('4')]
#print("Nota 4 = ", len(SalgadoNota4))
NotaSalgado.append(len(SalgadoNota4))
SalgadoNota5 = df[df['Salgado'].str.contains('5')]
#print("Nota 5 = ", len(SalgadoNota5))
NotaSalgado.append(len(SalgadoNota5))
st.write(NotaSalgado)

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

#print("Nota Final Salgado = ", NotaFinalSalgado)
#print('\nNOTAS REFRI: ')
NotaRefri = []
RefriNota0 = df[df['Refri'].str.contains('0')]
#print("Nota 0 = ", len(RefriNota0))
NotaRefri.append(len(RefriNota0))
RefriNota1 = df[df['Refri'].str.contains('1')]
#print("Nota 1 = ", len(RefriNota1))
NotaRefri.append(len(RefriNota1))
RefriNota2 = df[df['Refri'].str.contains('2')]
#print("Nota 2 = ", len(RefriNota2))
NotaRefri.append(len(RefriNota2))
RefriNota3 = df[df['Refri'].str.contains('3')]
#print("Nota 3 = ", len(RefriNota3))
NotaRefri.append(len(RefriNota3))
RefriNota4 = df[df['Refri'].str.contains('4')]
#print("Nota 4 = ", len(RefriNota4))
NotaRefri.append(len(RefriNota4))
RefriNota5 = df[df['Refri'].str.contains('5')]
#print("Nota 5 = ", len(RefriNota5))
NotaRefri.append(len(RefriNota5))

st.write(NotaRefri)
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

#print("Nota Final Refri = ", NotaFinalRefri)
#print('\nNOTAS BOLO: ')
NotaBolo = []
BoloNota0 = df[df['Bolo'].str.contains('0')]
#print("Nota 0 = ", len(BoloNota0))
NotaBolo.append(len(BoloNota0))
BoloNota1 = df[df['Bolo'].str.contains('1')]
#print("Nota 1 = ", len(BoloNota1))
NotaBolo.append(len(BoloNota1))
BoloNota2 = df[df['Bolo'].str.contains('2')]
#print("Nota 2 = ", len(BoloNota2))
NotaBolo.append(len(BoloNota2))
BoloNota3 = df[df['Bolo'].str.contains('3')]
#print("Nota 3 = ", len(BoloNota3))
NotaBolo.append(len(BoloNota3))
BoloNota4 = df[df['Bolo'].str.contains('4')]
#print("Nota 4 = ", len(BoloNota4))
NotaBolo.append(len(BoloNota4))
BoloNota5 = df[df['Bolo'].str.contains('5')]
#print("Nota 5 = ", len(BoloNota5))
NotaBolo.append(len(BoloNota5))

st.write(NotaBolo)

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

  #print("Nota Final BOlo = ", NotaFinalBolo)

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
  st.write(NotaSalgado)
  st.write(NotaRefri)
  st.write(NotaBolo)
  
  st.write("Desvio Padrão Salgado = ", DesvPAD_Salgado)
  st.write("Desvio Padrão Refri = ", DesvPAD_Refri)
  st.write("Desvio Padrão Bolo = ", DesvPAD_Bolo)
  IQT = round(NotaFinalSalgado/DesvPAD_Salgado + NotaFinalRefri/DesvPAD_Refri + NotaFinalBolo/DesvPAD_Bolo, 3)
  NotaFinalSalgado = round(NotaFinalSalgado/DesvPAD_Salgado, 3)
  st.write(NotaFinalSalgado)
  NotaFinalRefri = round(NotaFinalRefri/DesvPAD_Refri, 3)
  st.write(NotaFinalRefri)
  NotaFinalBolo = round(NotaFinalBolo/DesvPAD_Bolo, 3)
  st.write(NotaFinalBolo)
  CSAT = CalculaCSat(NotaSalgado, NotaRefri, NotaBolo)
  st.write("CSAT = ")
  st.write(CSAT)
