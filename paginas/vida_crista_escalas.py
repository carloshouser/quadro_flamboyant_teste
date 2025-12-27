import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def botao_voltar_principal():
    if st.button("⬅️ Voltar ao início", key='btn_vida_crista_voltar', width='stretch'):
        st.session_state["pagina"] = "home"
        st.rerun()


def render_escala():
    st.title("📌 Vida Cristã – Escalas")
    botao_voltar_principal()

    df = pd.read_csv(r"assets/csv/analise.csv", sep=";", encoding="latin1")
    df = df.fillna("")

    # =================================================
    #      CSS — Estilo Premium Soft-Glass Card
    # =================================================
    css = """
    <style>

    .table-card {
        width: 100%;
        max-height: 650px;
        overflow-y: auto;
        background: rgba(255, 255, 255, 0.75);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        border-radius: 18px;
        border: 1px solid rgba(200,200,200,0.45);
        box-shadow: 0 8px 30px rgba(0,0,0,0.06);
        margin-top: 25px;
    }

    table.custom-table {
        width: 100%;
        border-collapse: collapse;
        font-family: 'Segoe UI', sans-serif;
        font-size: 15px;
        color: #2c2c2c;
    }

    /* Cabeçalho elegante */
    table.custom-table thead th {
        position: sticky;
        top: 0;
        background: #ffffffee;
        backdrop-filter: blur(4px);
        padding: 14px 16px;
        font-weight: 600;
        font-size: 14px;
        border-bottom: 1px solid #ddd;
        color: #1a1a1a;
        letter-spacing: 0.25px;
        text-align: left;
        z-index: 10;
    }

    /* Linhas */
    table.custom-table tbody td {
        padding: 14px 16px;
        border-bottom: 1px solid #eee;
        font-size: 14px;
    }

    /* Zebra suave */
    table.custom-table tbody tr:nth-child(even) {
        background: #fafbff;
    }

    /* Hover muito elegante */
    table.custom-table tbody tr:hover {
        background: #eef2ff;
        box-shadow: inset 0 0 0 9999px rgba(79, 139, 249, 0.08);
        transition: 0.18s ease-in-out;
    }

    table.custom-table tbody tr:last-child td {
        border-bottom: none;
    }
    </style>
    """

    html_table = df.to_html(classes="custom-table", index=False, border=0)

    components.html(
        css + f"<div class='table-card'>{html_table}</div>",
        height=700,
        scrolling=False,
    )