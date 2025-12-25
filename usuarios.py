usuarios = {
    "Carlos": {
        "senha": "ccc",
        "nome": "Carlos",
        "permissoes": ["a", "b", "c", "d", "e", "f", "g", "frequencia"],
        "sexo": "M",
    },
    "Jerome": {
        "senha": "@salmo8318",
        "permissoes": ["a", "b", "c", "d", "e", "f", "g", "frequencia"],
        "sexo": "M",
        "nome": "Jerome Sampaio",
    },
    "Elber": {
        "senha": "@juizes10",
        "permissoes": ["a", "b", "c", "d", "e", "f", "g"],
        "sexo": "M",
        "nome": "Elber Soares",
    }
}


def nome_fantasia(dic_usuario, nome):
    if dic_usuario["sexo"] == "M":
        return f"irmão {nome}"
    else:
        return f"irmã {nome}"