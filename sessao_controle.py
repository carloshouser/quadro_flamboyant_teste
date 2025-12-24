import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import os

password = os.environ["COOKIE_SECRET"]

# Configuração dos Cookies
cookies = EncryptedCookieManager(
    prefix="flamboyant_",
    password=password,
)

if not cookies.ready():
    st.stop()

def reset_sessao():
    """
    Reseta a sessão do Streamlit e remove cookies.
    Faz logout: limpa cookies e volta para tela de login.
    """
    cookies["usuario"] = ""
    cookies["senha"] = ""
    st.session_state["logado"] = False
    st.session_state["pagina"] = "login"
    st.rerun()