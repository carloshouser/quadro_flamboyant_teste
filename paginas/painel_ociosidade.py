import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

# =========================
# LISTAS DE HABILITAÇÃO
# =========================

lst_presidencia = [
    "Carlos Alberto",
    "Carlos Montesino",
    "Ederson Carneiro",
    "Edson Padilha",
    "Jerome Sampaio",
    "Josnei Machado",
    "Luiz Nogueira",
    "Marcos Ribeiro",
    "Marcos Woicjki",
    "Miguel Mann Bernardo",
    "Paulo Carvalho",
    "Paulo Franco",
    "Raphael Madeira",
    "Sergio Santos",
]

lst_oracao = [
    "Anderson do Vale",
    "Armando Vieira",
    "Aron Stachecka",
    "Carlos Alberto",
    "Carlos Montesino",
    "David Affonso",
    "Ederson Carneiro",
    "Edson Padilha",
    "Felipe Carneiro",
    "Francinco Lezcano",
    "Gilmar de Lucas",
    "Giovani Vieira",
    "Jerome Sampaio",
    "João Batista",
    "José Francisco",
    "Josnei Machado",
    "Luís Cláudio de Júlio",
    "Luiz Nogueira",
    "Luiz Eleutério",
    "Marcos Ribeiro",
    "Marcos Woicjki",
    "Miguel Mann Bernardo",
    "Paulo Carvalho",
    "Paulo Franco",
    "Raphael Madeira",
    "Renato Horning",
    "Sergio Santos",
    "Valdir Tadra",
]

lst_tesouros = [
    "Armando Vieira",
    "Carlos Alberto",
    "Carlos Montesino",
    "Ederson Carneiro",
    "Edson Padilha",
    "Francinco Lezcano",
    "Jerome Sampaio",
    "Josnei Machado",
    "Luiz Nogueira",
    "Marcos Ribeiro",
    "Marcos Woicjki",
    "Miguel Mann Bernardo",
    "Paulo Carvalho",
    "Paulo Franco",
    "Raphael Madeira",
    "Sergio Santos",
]

lst_joias = [
    "Armando Vieira",
    "Aron Stachecka",
    "Carlos Montesino",
    "David Affonso",
    "Ederson Carneiro",
    "Felipe Carneiro",
    "Francinco Lezcano",
    "Gilmar de Lucas",
    "Giovani Vieira",
    "José Francisco",
    "Luís Cláudio de Júlio",
    "Marcos Ribeiro",
    "Paulo Carvalho",
    "Renato Horning",
]

lst_discurso = [
    "Armando Vieira",
    "Carlos Alberto",
    "Carlos Montesino",
    "David Affonso",
    "Ederson Carneiro",
    "Edson Padilha",
    "Felipe Carneiro",
    "Francinco Lezcano",
    "Gilmar de Lucas",
    "Giovani Vieira",
    "Jerome Sampaio",
    "Josnei Machado",
    "Luís Cláudio de Júlio",
    "Luiz Nogueira",
    "Marcos Ribeiro",
    "Marcos Woicjki",
    "Miguel Mann Bernardo",
    "Paulo Carvalho",
    "Paulo Franco",
    "Raphael Madeira",
    "Sergio Santos",
]

lst_estudo = [
    "Armando Vieira",
    "Carlos Alberto",
    "Carlos Montesino",
    "Ederson Carneiro",
    "Edson Padilha",
    "Jerome Sampaio",
    "Josnei Machado",
    "Luiz Nogueira",
    "Marcos Ribeiro",
    "Marcos Woicjki",
    "Miguel Mann Bernardo",
    "Paulo Carvalho",
    "Paulo Franco",
    "Raphael Madeira",
    "Sergio Santos",
]

lst_leitor = [
    "Anderson do Vale",
    "David Affonso",
    "Felipe Carneiro",
    "Gilmar de Lucas",
    "Giovani Vieira",
    "Heitor Wojcik",
    "Lucas Daniel",
    "Luís Cláudio de Júlio",
    "Luiz Eleutério",
    "Valdir Tadra",
]

# Mapeamento das colunas do CSV para as listas de elegíveis
categorias_map = {
    "Presidencia": lst_presidencia,
    "Oracao Inicial": lst_oracao,
    "Tesouros": lst_tesouros,
    "Joias": lst_joias,
    "Discurso1": lst_discurso,
    "Discurso2": lst_discurso,  # mesma lista
    "Estudo": lst_estudo,
    "Leitor": lst_leitor,
    "Oracao Final": lst_oracao,
}


def botao_voltar_inicio():
    if st.button("⬅️ Voltar ao início", key="ociosidade_btn_voltar"):
        st.session_state["pagina"] = "home"
        st.rerun()


# =========================
# Funções utilitárias
# =========================


def garantir_datas(df):
    if "Data" not in df.columns:
        raise ValueError("Arquivo CSV não contém a coluna 'Data'.")

    df = df.copy()
    df["Data"] = pd.to_datetime(df["Data"], format="%d/%m/%y", errors="coerce")

    if df["Data"].isna().any():
        df["Data"] = df["Data"].fillna(
            pd.to_datetime(df["Data"].astype(str), format="%d/%m/%y", errors="coerce")
        )

    if df["Data"].isna().any():
        raise ValueError("Algumas datas não puderam ser convertidas.")

    return df


def calcular_relatorio(df, coluna_csv, lista_habilitados):
    df = garantir_datas(df)
    max_data = df["Data"].max()

    registros = []

    for nome in lista_habilitados:
        if coluna_csv in df.columns:
            linhas = df[df[coluna_csv] == nome]
        else:
            linhas = df.iloc[0:0]

        if linhas.empty:
            ultima = pd.NaT
            ociosidade = None
        else:
            ultima = linhas["Data"].max()
            delta_days = (max_data - ultima).days
            ociosidade = delta_days // 7

        registros.append(
            {
                "Nome": nome,
                "Ultima Participacao": (ultima.date() if pd.notna(ultima) else None),
                "Ociosidade": ociosidade,
            }
        )

    df_cat = pd.DataFrame(registros)

    df_cat["Ociosidade"] = df_cat["Ociosidade"].astype("Int64")

    df_cat["never"] = df_cat["Ociosidade"].isna()
    df_cat = df_cat.sort_values(
        by=["never", "Ociosidade"], ascending=[False, False]
    ).reset_index(drop=True)

    df_cat["Posicao"] = df_cat.index + 1

    df_cat["Ultima Participacao Display"] = df_cat["Ultima Participacao"].apply(
        lambda x: "Nunca" if pd.isna(x) else x.strftime("%d/%m/%Y")
    )

    df_cat = df_cat[["Nome", "Ultima Participacao Display", "Ociosidade", "Posicao"]]

    df_cat = df_cat.rename(
        columns={"Ultima Participacao Display": "Ultima Participacao"}
    )

    return df_cat


def estilo_cor(df_cat):
    def color_row(row):
        o = row["Ociosidade"]

        if pd.isna(o):
            bg = "#ffcccc"  # vermelho
        elif o >= 12:
            bg = "#ffd8b2"  # laranja
        elif o >= 5:
            bg = "#fff4b1"  # amarelo
        else:
            bg = "#ccffd6"  # verde

        return [f"background-color: {bg}; color: #000000;" for _ in row]

    return df_cat.style.apply(color_row, axis=1)


# =========================
# STREAMLIT UI
# =========================


def render_painel_ociosidade():

    st.title("📊 Painel de Ociosidade — Designações")

    # ---- Botão de Ajuda ----
    if st.button("❓ Ajuda", key="ociosidade_btn_ajuda"):
        try:
            with open(r"assets/htmls/help_ociosidade.html", "r", encoding="utf-8") as f:
                html_code = f.read()
            st.markdown("## 📘 Ajuda")
            components.html(html_code, height=800, scrolling=True)
        except Exception as e:
            st.error(f"Erro ao carregar help_ociosidade.html: {e}")

    st.write("")  # espaço

    botao_voltar_inicio()

    try:
        df = pd.read_csv(r"assets/csv/analise.csv", sep=";", encoding="latin1")

        df_copia = df.copy()
        df_copia["Data"] = pd.to_datetime(
            df_copia["Data"], format="%d/%m/%y", errors="coerce"
        )

        primeira_data = df_copia["Data"].min()
        ultima_data = df_copia["Data"].max()

        if pd.notnull(primeira_data) and pd.notnull(ultima_data):
            periodo = (
                f"📅 **Período analisado:** "
                f"{primeira_data.strftime('%d/%m/%Y')} a {ultima_data.strftime('%d/%m/%Y')}"
            )
            st.markdown(periodo)
        else:
            st.markdown("📅 **Período analisado:** dados insuficientes.")

        df = garantir_datas(df)

    except Exception as e:
        st.error(f"Erro ao ler/parsear o CSV: {e}")
        st.stop()

    categorias = list(categorias_map.keys())
    abas = st.tabs(categorias)

    for tab, categoria in zip(abas, categorias):
        with tab:
            st.subheader(f"Categoria: {categoria}")

            lista = categorias_map[categoria]
            df_rel = calcular_relatorio(df, categoria, lista)

            sty = estilo_cor(df_rel)

            st.dataframe(sty, width='stretch', hide_index=True)

            st.write("")
            st.markdown(
                f"- Total de semanas no histórico: **{len(df['Data'].unique())}**  \n"
                f"- Pessoas na lista: **{len(lista)}**"
            )

            st.subheader("📌 Legenda de cores — Ociosidade (semanas)")
            st.markdown(
                """
            - 🟥 **Vermelho** — Nunca participou  
            - 🟧 **Laranja** — Ociosidade muito alta (≥ 12 semanas)  
            - 🟨 **Amarelo** — Ociosidade moderada (5 a 11 semanas)  
            - 🟩 **Verde** — Participou recentemente (< 5 semanas)  
            """
            )