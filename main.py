# ⌨️ Atalhos de teclado
# Windows + Ctrl + D → Cria imediatamente uma nova área de trabalho.
# Windows + Ctrl + ← / → → Alterna entre as áreas de trabalho criadas.
# Windows + Tab → Abre a Visão de Tarefas, onde você pode gerenciar 
# e adicionar áreas de trabalho manualmente.

# Variável de ambiente para criptografia: 
# COOKIE_SECRET: xxx
# import secrets
# print(secrets.token_hex(32))

# python.exe -m pip install --upgrade pip
# pip install streamlit
# pip install streamlit-cookies-manager
# pip freeze > requirements.txt

import os
import streamlit as st
st.set_page_config(page_title="Quadro de Anúncios", layout="wide")
from streamlit_cookies_manager import EncryptedCookieManager

password = os.environ["COOKIE_SECRET"]

# Configuração dos Cookies
cookies = EncryptedCookieManager(
    prefix="flamboyant_",
    password=password,
)

if not cookies.ready():
    st.stop()

st.title('Teste')