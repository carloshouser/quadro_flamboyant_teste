import streamlit as st
from sessao_controle import reset_sessao
from acessos import quadros, usuario_tem_acesso, usuarios

def render_eventos(events):
    """
    Renderiza a aba de eventos.
    """
    usuario = st.session_state["usuario"]
    
    st.title(quadros["lembretes"]["titulo"])

    st.subheader("Próximos Eventos")    
    for event in events:                
        if event["link"]:
            st.markdown(
                f"""
            ### 📅 {event['date']}
            #### [**{event['event']}**]({event['link']})
            """
            )

        else:
            st.markdown(
                f"""
              ### 📅 {event['date']}
                #### **{event['event']}**
                """
            )
        st.divider()