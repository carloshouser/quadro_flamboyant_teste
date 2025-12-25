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

            div.stButton > button:hover {
                background-color: #163172;
            }

            /* Inputs */
            input {
                border-radius: 6px !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
