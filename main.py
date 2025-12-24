
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
# pip install -r requirements.txt


import streamlit as st

from login_usuario import render_login
from utilitarios import load_eventos
st.set_page_config(page_title="Quadro de Anúncios", layout="wide")

from ui import styles

def render_header():
    """
    Renderiza o cabeçalho do aplicativo com uma imagem.
    """
    st.image("imagens/salao.png", width='content')


styles.apply_css()

render_header()

# Inicializar a sessão
if "logado" not in st.session_state:
    st.session_state["logado"] = False
    st.session_state["pagina"] = "login"

if render_login():
    st.header('Sucesso')