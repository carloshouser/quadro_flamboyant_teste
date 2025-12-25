import streamlit as st
from pathlib import Path
from acessos import quadros

def render_lembretes():

    # ===============================
    # 🔙 TOPO FIXO DO STREAMLIT
    # ===============================
    with st.container():
        col1, col2 = st.columns([1, 9])
        with col1:
            if st.button("⬅ Voltar"):
                st.session_state["pagina"] = "home"
                st.rerun()

    # separação real no layout do Streamlit
    st.markdown("---")

    st.title(quadros["lembretes"]["titulo"])

    # ===============================
    # 📄 IFRAME ISOLADO
    # ===============================
    html_path = (
        Path(__file__).parent.parent
        / "assets"
        / quadros["lembretes"]["arquivo"]
    )

    if html_path.exists():
        # ⚠️ container exclusivo para o iframe
        with st.container():
            st.components.v1.html(
                html_path.read_text(encoding="utf-8"),
                height=700,
                scrolling=True
            )
    else:
        st.error("Arquivo de anúncios não encontrado.")
