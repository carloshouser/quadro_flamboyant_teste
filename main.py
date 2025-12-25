
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

# Controle de sessão e cookies
import sessao_controle

# Estilo global
from estilo import aplicar_estilo

# Telas
from login_usuario import render_login
from paginas.home import render_home
# (no futuro: dashboard, cadastro, frequência, etc.)

# ===============================
# Configuração da página
# ===============================
st.set_page_config(
    page_title="Flamboyant - Quadro de Anúncios",
    layout="wide",
)

# ===============================
# Estilo global (UMA vez)
# ===============================
aplicar_estilo()

# ===============================
# Inicialização da sessão
# ===============================
sessao_controle.init_sessao()

# ===============================
# Login automático por cookie
# ===============================
sessao_controle.tentar_login_por_cookie()

# ===============================
# Roteamento central
# ===============================
if not st.session_state["logado"]:
    # Tela de login
    render_login()

else:
    pagina = st.session_state["pagina"]

    if pagina == "home":
        render_home()

    elif pagina == "dashboard":
        st.header("Dashboard")

    elif pagina == "cadastro":
        st.header("Cadastro")

    elif pagina == "frequencia":
        st.header("Frequência")

    else:
        st.error("Página não encontrada.")
