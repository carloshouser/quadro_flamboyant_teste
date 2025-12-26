import streamlit as st

# Dicionário com os quadros de anúncios
quadros = {
    "lembretes": {
        "titulo": "Anúncios e Lembretes",
        "arquivo": r"htmls/lembrete.html"
    },

    "limpeza": {
        "titulo": "Limpeza do Salão do Reino",
        "arquivo": r"pdfs/limpeza.pdf"        
    },

    "relatorio": {
        "titulo": "Relatório (Basta preencher, printar e enviar)",
        "arquivo": r"htmls/relatorio.html"
    }
    
}

usuarios = {
    "Carlos": {
        "senha": "ccc",
        "nome": "Carlos",        
        "sexo": "M",
        'acesso' : ["lembretes", "limpeza", "relatorio"]
    },
    "Jerome": {
        "senha": "jjj",
        'acesso' : [],
        "sexo": "M",
        "nome": "Jerome Sampaio",
    },
    "Elber": {
        "senha": "@juizes10",
        'acesso' : [],
        "sexo": "M",
        "nome": "Elber Soares",
    }
}

def nome_fantasia(dic_usuario, nome):
    if dic_usuario["sexo"] == "M":
        return f"irmão {nome}"
    else:
        return f"irmã {nome}"
    
def usuario_tem_acesso(usuario, acesso):
    return acesso in usuarios.get(usuario, {}).get("acesso", [])
    
