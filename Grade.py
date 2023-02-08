import streamlit as st
import pandas as pd
import time

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
Modelagem_dados()
st.set_page_config(page_title='Tubo De PCP',  layout='wide', page_icon=':ambulance:')

#this is the header

t1, t2 = st.columns((0.1,1)) 
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
## Data