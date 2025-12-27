import streamlit as st
import pandas as pd
from acessos import quadros, usuarios

def render_designacoes_estudantes():
    # --- CSS para melhorar aparência ---
    st.markdown(
        """
    <style>
        div[data-baseweb="select"] > div {
            border-radius: 10px !important;
            border: 1px solid #999 !important;
            box-shadow: 2px 2px 6px rgba(0,0,0,0.15) !important;
        }
        .stDataFrame {border-radius: 10px; overflow: hidden;}
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("## 👨‍🏫 Minhas designações")

    # 🔙 Botão Voltar
    if st.button("⬅ Voltar para a página principal", key = 'minhas_designacoes_voltar'):
        st.session_state["pagina"] = "home"
        st.rerun()    

    st.markdown("---")

    # Carregar CSV
    try:
        df = pd.read_csv("assets/csv/estudantes.csv", sep=";", encoding="latin1")
    except Exception as e:
        st.error(f"Erro ao carregar o CSV: {e}")
        return

    # Renomear colunas
    df = df.rename(
        columns={
            "Date": "Data",
            "Type": "Tipo",
            "Student": "Estudante",
            "Assistant": "Ajudante",
        }
    )

    df["Date"] = pd.to_datetime(df["Data"], format="%d/%m/%y")
    df = df.sort_values(by="Date")
    df["Data"] = df["Date"].dt.strftime("%d/%m/%Y")

    estudantes = sorted(df["Estudante"].dropna().unique())

    # Usuário logado
    usuario_logado = st.session_state["usuario"]
    nome_completo = usuarios[usuario_logado]["nome"]

    # Filtro inicial pelo nome real do usuário
    filtro_inicial = [nome_completo] if nome_completo in estudantes else []

    estudantes_selecionados = st.multiselect(
        "👤 Filtrar por estudante:", options=estudantes, default=filtro_inicial
    )

    if estudantes_selecionados:
        df_filtrado = df[df["Estudante"].isin(estudantes_selecionados)]
    else:
        df_filtrado = df

    df_exibe = df_filtrado[["Data", "Tipo", "Estudante", "Ajudante"]]

    st.dataframe(df_exibe, width='stretch', hide_index=True)