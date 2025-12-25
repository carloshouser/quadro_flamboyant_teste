import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import os

# ===============================
# Configuração segura dos cookies
# ===============================
COOKIE_SECRET = os.environ.get("COOKIE_SECRET")

if not COOKIE_SECRET:
    st.error("Variável de ambiente COOKIE_SECRET não configurada.")
    st.stop()

cookies = EncryptedCookieManager(
    prefix="flamboyant_",
    password=COOKIE_SECRET,
)

if not cookies.ready():
    st.stop()


# ===============================
# Inicialização do session_state
# ===============================
def init_sessao():
    """
    Garante que todas as chaves necessárias existam no session_state.
    """
    defaults = {
        "logado": False,
        "usuario": None,
        "pagina": "login",
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


# ===============================
# Login automático via cookie
# ===============================
def tentar_login_por_cookie():
    """
    Se existir usuário salvo no cookie, autentica automaticamente.
    """
    usuario_cookie = cookies.get("usuario")
    if usuario_cookie and not st.session_state["logado"]:
        st.session_state.update(
            {
                "logado": True,
                "usuario": usuario_cookie,
                "pagina": "home",
            }
        )
        st.rerun()


# ===============================
# Logout
# ===============================
def reset_sessao():
    """
    Faz logout: limpa cookies e sessão.
    """
    cookies["usuario"] = ""
    st.session_state.update(
        {
            "logado": False,
            "usuario": None,
            "pagina": "login",
        }
    )
    st.rerun()
