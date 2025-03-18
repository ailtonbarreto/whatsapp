# from urllib.parse import quote
# import webbrowser
from time import sleep
import pyautogui
import streamlit as st
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTIjlaFlFd2MaY9MQhswdNF2W1FzBWAxxHqlOszSfTLnxQ27ss9VyANMIEXjNsyMQ3cJBunTVDEbjUl/pub?gid=0&single=true&output=csv'


df = pd.read_csv(url)

# def enviar_mensagens(df, mensagem):
    
#     sleep(3)

#     for _, linha in df.iterrows():
#         nome = linha['nome']

#         telefone = linha['telefone'] 

#         try:
     
#             mensagem_personalizada = mensagem.replace("{nome}", nome)

  
#             link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(mensagem_personalizada)}'
            
#             webbrowser.open(link_mensagem_whatsapp)
            
#             sleep(10) 


#             pyautogui.hotkey('enter')
#             sleep(3)
#             pyautogui.hotkey('ctrl', 'w')
#             sleep(3)
            
#         except Exception as e:
#             st.error(f'Erro ao enviar mensagem para {nome}: {e}')
#             continue


# st.title('Envio de Mensagens Personalizadas via WhatsApp')


# st.write("Dados carregados da URL:")
# st.dataframe(df)


# if 'nome' in df.columns and 'telefone' in df.columns:
#     st.success("Dados carregados com sucesso.")


#     mensagem_input = st.text_area("Digite a mensagem! Utilize {nome} para incluir o nome do destinatário.")

#     if st.button('Enviar Mensagens'):
#         enviar_mensagens(df, mensagem_input)
# else:
#     st.error("O arquivo CSV deve conter as colunas 'nome' e 'telefone'!")
