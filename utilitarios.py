import json

def load_eventos():
    """
    Carrega dados de um arquivo JSON.
    """
    with open('eventos.json', "r", encoding="utf-8") as file:
        return json.load(file)