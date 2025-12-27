import streamlit as st
from pathlib import Path
from acessos import quadros

def render_lembretes():

    # 🔧 ESPAÇO DE SEGURANÇA NO TOPO (antes de tudo)
    st.markdown("<div style='height:60px'></div>", unsafe_allow_html=True)

    # 🔙 Botão Voltar
    if st.button("⬅ Voltar para a página principal", key = 'lembrete_voltar', width='stretch'):
        st.session_state["pagina"] = "home"
        st.rerun()

    st.markdown("---")
    st.title(quadros["lembretes"]["titulo"])

    html_path = (
        Path(__file__).parent.parent
        / "assets"
        / quadros["lembretes"]["arquivo"]
    )

    if html_path.exists():
        placeholder = st.empty()
        with placeholder:
            st.components.v1.html(
                html_path.read_text(encoding="utf-8"),
                height=700,
                scrolling=True
            )
    else:
        st.error("Arquivo de anúncios não encontrado.")
