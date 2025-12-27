
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
from paginas.lembretes import render_lembretes
from paginas.limpeza import render_limpeza
from paginas.relatorios import render_relatorio
from paginas.painel_ociosidade import render_painel_ociosidade
from paginas.vida_crista_escalas import render_escala
from paginas.painel_frequencia import render_painel_frequencia
from paginas.designacoes_estudantes import render_designacoes_estudantes
from paginas.designacoes_mecanicas import render_designacoes_mecanicas
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

    elif pagina == 'lembretes':
        render_lembretes()
        
    elif pagina == 'limpeza':
        render_limpeza() 

    elif pagina == 'relatorio':
        render_relatorio() 

    elif pagina == "ociosidade":
            render_painel_ociosidade()

    elif pagina == "vida_crista_escalas":
            render_escala()

    elif pagina == "painel_frequencia":
            render_painel_frequencia()
    
    elif pagina == "designacoes_estudantes":
            render_designacoes_estudantes()

    elif pagina == "designacoes_mecanicas":
            render_designacoes_mecanicas()

    else:
        st.error("Página não encontrada.")
