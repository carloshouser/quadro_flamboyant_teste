import streamlit as st
import sessao_controle
from pathlib import Path
from acessos import usuarios, nome_fantasia, usuario_tem_acesso

def render_home():
    st.title("Flamboyant")    

    # Caminho seguro da imagem
    img_path = Path(__file__).parent.parent / "assets" / "imagens" / "salao.png"

    if img_path.exists():
        st.image(str(img_path), width='content')
    else:
        st.warning("Imagem salao.png não encontrada.")

    st.markdown("---")
    
    usuario = st.session_state["usuario"]
    if usuarios[usuario]["sexo"] == "M":
        st.write(
            f"##### Saudações {nome_fantasia(usuarios[usuario], usuario)}, seja bem-vindo!!"
        )
    else:
        st.write(
            f"##### Saudações {nome_fantasia(usuarios[usuario], usuario)}, seja bem-vinda!!"
        )
    
    tab_quadro, tab_eventos = st.tabs(["Quadro", "Eventos"])
    with tab_quadro:
        col1, col2, col3 = st.columns(3)

        with col1:
            # Botão condicional
            if usuario_tem_acesso(usuario, "lembretes"):
                if st.button(label="📢 Anúncios e Lembretes", type='primary', key='lembretes'):
                    st.session_state["pagina"] = "lembretes"
                    st.rerun()
            if usuario_tem_acesso(usuario, "limpeza"):
                if st.button(label="📢 Limpeza do Salão do Reino ", type='secondary', key='limpeza'):
                    st.session_state["pagina"] = "limpeza"
                    st.rerun()

            if usuario_tem_acesso(usuario, "relatorio"):
                if st.button(label="📢 Relatório", type='secondary', key='relatorio'):
                    st.session_state["pagina"] = "relatorio"
                    st.rerun()

            if usuario_tem_acesso(usuario, "ociosidade"):
                if st.button(label="📢 Painel de Ociosidade", type='secondary', key='ociosidade'):
                    st.session_state["pagina"] = "ociosidade"
                    st.rerun()

            if usuario_tem_acesso(usuario, "vida_crista_escalas"):
                if st.button(label="📢 Vida Cristã - Escalas", type='secondary', key='vida_crista_escalas'):
                    st.session_state["pagina"] = "vida_crista_escalas"
                    st.rerun()

            if usuario_tem_acesso(usuario, "painel_frequencia"):
                if st.button(label="📢 Painel de Frequência", type='secondary', key='painel_frequencia'):
                    st.session_state["pagina"] = "painel_frequencia"
                    st.rerun()

            if usuario_tem_acesso(usuario, "designacoes_estudantes"):
                if st.button(label="📢 Minhas Designações", type='secondary', key='designacoes_estudantes'):
                    st.session_state["pagina"] = "designacoes_estudantes"
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