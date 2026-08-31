"""Читання та запис стану персонажа у JSON-файл."""
import json


def load_state(path="data.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_state(state, path="data.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(state, f)
