import streamlit as st
from pathlib import Path
from acessos import quadros

def render_lembretes():

    # 🔙 Botão Voltar    
    if st.button("⬅ Voltar para a página principal"):
        st.session_state["pagina"] = "home"
        st.rerun()

    st.title(quadros["lembretes"]["titulo"])

    html_path = (
        Path(__file__).parent.parent
        / "assets"
        / quadros["lembretes"]["arquivo"]
    )

    if html_path.exists():
        with open(html_path, "r", encoding="utf-8") as f:
            st.markdown("<div style='height:20px'></div>", unsafe_allow_html=True)
            st.components.v1.html(
                f.read(),
                height=700,
                scrolling=True
            )
    else:
        st.error("Arquivo de anúncios não encontrado.")
