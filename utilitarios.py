import json
from pathlib import Path

def load_eventos():
    """
    Carrega dados de um arquivo JSON.
    """
    json_path = (
        Path(__file__).parent
        / "assets"
        / "jsons"
        / "eventos.json"
    )

    if not json_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {json_path}")

    with json_path.open("r", encoding="utf-8") as file:
        return json.load(file)
