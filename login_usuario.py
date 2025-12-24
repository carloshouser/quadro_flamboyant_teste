import streamlit as st
from constantes import usuarios
import sessao_controle


def autenticar_usuario(usuario, senha):
    """
    Verifica se o usuário e a senha são válidos.
    """
    return usuario in usuarios and usuarios[usuario]["senha"] == senha

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
            sessao_controle.cookies["usuario"] = usuario
            sessao_controle.cookies["senha"] = senha
            return True
        else:
            st.error("Usuário ou senha incorretos.") 
            return False