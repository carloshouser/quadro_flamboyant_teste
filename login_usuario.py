import streamlit as st
from acessos import usuarios
import sessao_controle


# ===============================
# Autenticação
# ===============================
def autenticar_usuario(usuario: str, senha: str) -> bool:
    """
    Verifica se usuário e senha são válidos.
    """
    return (
        usuario in usuarios
        and usuarios[usuario]["senha"] == senha
    )


# ===============================
# Render da tela de login
# ===============================
def render_login():
    """
    Renderiza a tela de login e atualiza sessão se sucesso.
    """
    st.title("Flamboyant - Quadro de Anúncios")

    usuario = st.text_input("Usuário")
    senha = st.text_input("Senha", type="password")

    if st.button("Entrar", use_container_width=True):
        if autenticar_usuario(usuario, senha):
            # Atualiza sessão
            st.session_state.update(
                {
                    "logado": True,
                    "usuario": usuario,
                    "pagina": "home",
                }
            )

            # Salva apenas o usuário no cookie
            sessao_controle.cookies["usuario"] = usuario

            st.rerun()
        else:
            st.error("Usuário ou senha incorretos.")
