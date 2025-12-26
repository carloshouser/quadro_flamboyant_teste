import streamlit as st

def aplicar_estilo():
    st.markdown(
        """
        <style>
            /* Remove padding padrão */
            .block-container {
                padding-top: 1.5rem;
                padding-bottom: 2rem;
            }

            /* Títulos */
            h1, h2, h3 {
                color: #1f3c88;
            }

            /* Botões */
            div.stButton > button {
                background-color: #1f3c88;
                color: white;
                border-radius: 8px;
                height: 42px;
                font-weight: 600;
            }

            /* ===== BOTÃO ESPECIAL (PRIMARY) ===== */
            .stButton > button[kind="primary"] {
                background: linear-gradient(135deg, #ff9800, #f57c00) !important;
                color: white !important;
                border-radius: 14px;
                font-weight: 700;
                box-shadow: 0 0 14px rgba(255, 152, 0, 0.8) !important;
            }

            div.stButton > button:hover {
                background-color: #163172;
            }

            /* Hover botão especial */
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(135deg, #ffb74d, #fb8c00) !important;
        transform: translateY(-3px);
    }


        /* ====== BOTÕES NOS CARDS (colunas) ====== */
        div.stButton>button {
            width: 100%;
        }

        /* ====== TABS MELHORADAS ====== */
        .stTabs [data-baseweb="tab"] {
            padding: 12px 20px !important;
            font-size: 1rem;
            font-weight: 600;
            border-radius: 10px 10px 0 0;
        }





            /* Inputs */
            input {
                border-radius: 6px !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
