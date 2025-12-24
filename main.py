
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

import os
import streamlit as st
from utilitarios import load_eventos
from constantes import usuarios
st.set_page_config(page_title="Quadro de Anúncios", layout="wide")
from streamlit_cookies_manager import EncryptedCookieManager

from ui import styles

password = os.environ["COOKIE_SECRET"]

# Configuração dos Cookies
cookies = EncryptedCookieManager(
    prefix="flamboyant_",
    password=password,
)

if not cookies.ready():
    st.stop()

styles.apply_css()

def autenticar_usuario(usuario, senha):
    """
    Verifica se o usuário e a senha são válidos.
    """
    return usuario in usuarios and usuarios[usuario]["senha"] == senha

# Inicializar a sessão
if "logado" not in st.session_state:
    st.session_state["logado"] = False
    st.session_state["pagina"] = "login"

# Renderizações
def render_login():
    """
    Renderiza a tela de login.
    """
    st.title("Flamboyant - Quadro de Anúncios")
    usuario = st.text_input("Usuário").strip()
    senha = st.text_input("Senha", type="password").strip()

    if st.button("Entrar", key="btn_login_entrar"):
        if autenticar_usuario(usuario, senha):
            # Atualiza sessão
            st.session_state.update(
                {"logado": True, "usuario": usuario, "pagina": "home"}
            )
            # Salva login nos cookies
            cookies["usuario"] = usuario
            cookies["senha"] = senha
            st.write('Autenticado!')
            #st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")    

render_login()