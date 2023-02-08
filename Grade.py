# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 10:17:07 2021

@author: Andi5
"""
import streamlit as st
import time
import pandas as pd
#import plotly.express as px
#import plotly.graph_objects as go
from  PIL import Image

def Modelagem_dados():
    global Base_Oficial
    global Setores
    global Base
    global Base_tubo
    Base = pd.read_excel("https://docs.google.com/spreadsheets/d/1Vn_Dvy59N45ZJ6cVOIZHG1LcHChLMORqYduuLMrRajM/export?format=xlsx",sheet_name="Expedição")
    Index_Tubo = ['Data Coleta','Planilha','Hora Coleta','Veículo','Modal','Transportadora','Volumes']
    Base_tubo =Base
    Base_tubo[['Planilha','Volumes Secos','Volumes Inflamável','Volumes Biológico','Volumes Aftosa','Volumes Climatizado I','Volumes Criogênico']]=Base_tubo[['Planilha','Volumes Secos','Volumes Inflamável','Volumes Biológico','Volumes Aftosa','Volumes Climatizado I','Volumes Criogênico']].fillna(0)
    Base_tubo[['Planilha','Volumes','Volumes Secos','Volumes Inflamável','Volumes Biológico','Volumes Aftosa','Volumes Climatizado I','Volumes Criogênico']] =Base_tubo[['Planilha','Volumes','Volumes Secos','Volumes Inflamável','Volumes Biológico','Volumes Aftosa','Volumes Climatizado I','Volumes Criogênico']].astype(int)
    Base_tubo= Base_tubo.loc[(Base_tubo['Veículo']!='EXPORTAÇÃO')&(Base_tubo['Veículo']!='HUMANA')&(Base_tubo['Veículo']!='HUMANA')
               &(Base_tubo['Veículo']!='CLIENTE RETIRA')&(Base_tubo['Planilha']!=0)]
#     Base =Base[Index_Tubo]
#     Base['Planilha'] = Base['Planilha'].fillna(0)
#     Base[['Planilha','Volumes']] =Base[['Planilha','Volumes']].astype(int)
#     Base= Base.loc[(Base['Veículo']!='EXPORTAÇÃO')&(Base['Veículo']!='HUMANA')&(Base['Veículo']!='HUMANA')
#                &(Base['Veículo']!='CLIENTE RETIRA')&(Base['Planilha']!=0)]
#     file ='C:/Users/luan.carvalho/OneDrive - Solistica/GESTÃO DE PEDIDOS/Aderencia de Grade/345.xlsx'
#     Base345 =  pd.read_excel(file)
#     Base345['VOL./ST.'] =Base345['VOL./ST.'].fillna(0)
#     Base345[['Planilha','CTE','Nota/Pedido','VOL./ST.']] = Base345[['Planilha','CTE','Nota/Pedido','VOL./ST.']].astype(int)
#     Base_Oficial=  pd.merge(Base,Base345,on="Planilha",how="left")
#     #Base_Oficial.columns
#     Base_Oficial['Data Coleta'] =Base_Oficial['Data Coleta'].dt.strftime('%d/%m/%Y')
#     index_Base_ofocial= ['Data Coleta', 'Planilha', 'Hora Coleta', 'Veículo', 'Modal',
#        'Desc C.c', 'Nota/Pedido','Transportadora','Desc_Status', 'Setores','VOL./ST.']
#     Base_Oficial=Base_Oficial[index_Base_ofocial]
#     Setores =Base_Oficial.groupby(['Planilha','Data Coleta', 'Hora Coleta','Modal','Transportadora','Setores','Desc_Status'
#                              ],as_index=False)['VOL./ST.'].sum()
#     Setores =Setores.pivot_table(values= 'VOL./ST.',index=['Planilha','Data Coleta', 'Hora Coleta','Modal','Transportadora','Setores'],columns='Desc_Status',fill_value=0).reset_index()

Modelagem_dados()
st.set_page_config(page_title='Tubo De PCP',  layout='wide', page_icon=':ambulance:')

#this is the header

t1, t2 = st.columns((0.1,1)) 
logo = Image.open(r"C:\Users\luan.carvalho\Solistica\Torre de Controle - Transportes WHS-BR - Diretório_Operacionais\PROCESSOS E SISTEMAS\LOGOS SOLISTICA IMAGENS\Elemento-Logo.png")
t1.image(logo, width = 74)
t2.title("Tubo de Expedição e Produção")
t2.markdown(":blue[Desenvolvido pro Luan Carvalho]")

m1,m2,m3,m4,m5,m6,m7,m8,m9 = st.columns((5,3,3,3,3,3,3,3,3))
m1.metric(label='Total',value=Base_tubo['Volumes'].sum(),delta=57828 -round(Base_tubo['Volumes'].sum()))
m2.metric(label='Secos',value=Base_tubo['Volumes Secos'].sum(),delta=20514- round(Base_tubo['Volumes Secos'].sum()))
m3.metric(label='Inflamável',value=Base_tubo['Volumes Inflamável'].sum(),delta=12250- round(Base_tubo['Volumes Inflamável'].sum()))
m4.metric(label='Biológico',value=Base_tubo['Volumes Biológico'].sum(),delta=3800- round(Base_tubo['Volumes Biológico'].sum()))
m5.metric(label='Aftosa',value=Base_tubo['Volumes Aftosa'].sum(),delta=2700- round(Base_tubo['Volumes Aftosa'].sum()))
m6.metric(label='Climatizado I',value=Base_tubo['Volumes Climatizado I'].sum(),delta=18564- round(Base_tubo['Volumes Climatizado I'].sum()))
m7.metric(label='Criogênico',value=Base_tubo['Volumes Criogênico'].sum())
m8.metric(label='Veículos',value=Base_tubo['Planilha'].min())

#m3.metric(label=':orange[Vol. Produzidos]',value=Setores['Vol. Produzidos'].sum())

## Data

with st.spinner('Carregando as Tabelas'):
     time.sleep(3)
     st.success('Dados Carregados')



# import pandas as pd
# import streamlit as st
# Base = pd.read_excel("https://docs.google.com/spreadsheets/d/1Vn_Dvy59N45ZJ6cVOIZHG1LcHChLMORqYduuLMrRajM/export?format=xlsx",sheet_name="Expedição")
# Index_Tubo = ['Data Coleta','Planilha','Hora Coleta','Veículo','Modal','Transportadora']
# Base =Base[Index_Tubo]
# Base['Planilha'] = Base['Planilha'].fillna(0)
# Base['Planilha'] =Base['Planilha'].astype(int)
# Base= Base.loc[(Base['Veículo']!='EXPORTAÇÃO')&(Base['Veículo']!='HUMANA')&(Base['Veículo']!='HUMANA')
#                &(Base['Veículo']!='CLIENTE RETIRA')&(Base['Planilha']!=0)]
# file ='C:/Users/luan.carvalho/OneDrive - Solistica/GESTÃO DE PEDIDOS/Aderencia de Grade/345.xlsx'
# Base345 =  pd.read_excel(file)
# Base345['VOL./ST.'] =Base345['VOL./ST.'].fillna(0)
# Base345[['Planilha','CTE','Nota/Pedido','VOL./ST.']] = Base345[['Planilha','CTE','Nota/Pedido','VOL./ST.']].astype(int)
# Base_Oficial=  pd.merge(Base,Base345,on="Planilha",how="left")
# #Base_Oficial.columns
# Base_Oficial['Data Coleta'] =Base_Oficial['Data Coleta'].dt.strftime('%d/%m/%Y')
# index_Base_ofocial= ['Data Coleta', 'Planilha', 'Hora Coleta', 'Veículo', 'Modal',
#        'Desc C.c', 'Nota/Pedido','Transportadora','Desc_Status', 'Setores','VOL./ST.']
# Base_Oficial=Base_Oficial[index_Base_ofocial]
# Setores =Base_Oficial.groupby(['Planilha','Data Coleta', 'Hora Coleta','Modal','Transportadora','Setores','Desc_Status'
#                              ],as_index=False)['VOL./ST.'].sum()
# Setores =Setores.pivot_table(values= 'VOL./ST.',index=['Planilha','Data Coleta', 'Hora Coleta','Modal','Transportadora','Setores'],columns='Desc_Status',fill_value=0).reset_index()
# st.write('Tubo')
# st.dataframe(Setores)
# st.dataframe(Base_Oficial)