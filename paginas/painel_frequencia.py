import streamlit as st
import pandas as pd
import plotly.express as px

def render_painel_frequencia():
    st.markdown("## 📊 Frequência de Participações")
    # caminho_csv = r'C://docarlos//quadro_flamboyant_teste//teste_streamlit//analise.csv'
    caminho_csv = r"assets/csv/analise.csv"

    try:
        df = pd.read_csv(caminho_csv, sep=";", encoding="latin1")
        df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%y", errors="coerce")
    except Exception as e:
        st.error(f"Erro ao carregar o CSV: {e}")
        return

    # Filtro por data inicial
    data_minima = df["Data"].min().date()
    data_maxima = df["Data"].max().date()
    data_inicial = st.date_input(
        "Mostrar participações a partir de:",
        value=data_minima,
        min_value=data_minima,
        max_value=data_maxima,
        format="DD/MM/YYYY",
        key="freq_data_inicial",
    )

    data_final = st.date_input(
        "Mostrar participações até:",
        value=data_maxima,
        min_value=data_minima,
        max_value=data_maxima,
        format="DD/MM/YYYY",
        key="freq_data_final",
    )

    if data_inicial is not None:
        # Aplica o filtro apenas se a data for válida
        df = df[df["Data"] >= pd.to_datetime(data_inicial)]

    if data_final is not None:
        # Aplica o filtro apenas se a data for válida
        df = df[df["Data"] <= pd.to_datetime(data_final)]

        # Exibe a data no formato dd/mm/yyyy
        st.markdown(f"📆 **Data selecionada:** '{data_inicial.strftime('%d/%m/%Y')}'")
    else:
        st.warning("Por favor, selecione uma data válida.")

    # Formato longo
    df_long = df.melt(id_vars=["Data"], var_name="Modalidade", value_name="nome")
    df_long = df_long.dropna()
    df_long["nome"] = df_long["nome"].str.strip()

    # --- CONTAGEM + agregação das datas ---
    df_participacoes = (
        df_long.groupby(["nome", "Modalidade"])
        .agg(
            qtd=("Data", "count"),
            datas=(
                "Data",
                lambda x: ", ".join(sorted(x.dt.strftime("%d/%m/%Y").unique())),
            ),
        )
        .reset_index()
    )

    # --- FILTROS ---
    nomes = st.multiselect(
        "🔍 Filtrar por nome(s):", sorted(df_participacoes["nome"].unique())
    )
    modalidades = st.multiselect(
        "🎤 Filtrar por modalidade:", sorted(df_participacoes["Modalidade"].unique())
    )

    df_filtrado = df_participacoes.copy()
    if nomes:
        df_filtrado = df_filtrado[df_filtrado["nome"].isin(nomes)]
    if modalidades:
        df_filtrado = df_filtrado[df_filtrado["Modalidade"].isin(modalidades)]

    # --- GRÁFICO ---
    fig = px.bar(
        df_filtrado.sort_values(by="nome"),
        x="qtd",
        y="nome",
        color="Modalidade",
        orientation="h",
        title="Participações por Pessoa e Modalidade",
        labels={"qtd": "Qtd. Participações", "nome": "Participante"},
        height=600,
        hover_data={"datas": True, "qtd": True, "Modalidade": True, "nome": True},
    )

    fig.update_layout(
        xaxis=dict(tickmode="linear", tick0=0, dtick=1),
        yaxis=dict(categoryorder="category descending"),
    )

    st.plotly_chart(fig, use_container_width=True)

    if st.button("Início", key="btn_frequencia_inicio"):
        st.session_state["pagina"] = "home"
        st.rerun()