import streamlit as st
import sessao_controle
from pathlib import Path

def render_home():
    st.title("Flamboyant")

    # Caminho seguro da imagem
    img_path = Path(__file__).parent.parent / "assets" / "imagens" / "salao.png"

    if img_path.exists():
        st.image(str(img_path), width='content')
    else:
        st.warning("Imagem salao.png não encontrada.")

    st.markdown("---")

    tab_quadro, tab_eventos = st.tabs(["Quadro", "Eventos"])
    with tab_quadro:
        col1, col2, col3 = st.columns(3)

        with col1:
            if st.button("📢 Avisos"):
                st.session_state["pagina"] = "avisos"
                st.rerun()

        with col2:
            if st.button("📊 Frequência"):
                st.session_state["pagina"] = "frequencia"
                st.rerun()

        with col3:
            if st.button("🚪 Sair"):
                sessao_controle.reset_sessao()
    with tab_eventos:
        st.title('Eventos')
