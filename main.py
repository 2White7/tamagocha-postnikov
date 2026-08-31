"""Точка входу симулятора тамагочі."""
from datetime import datetime

from tamagocha_pkg.model import Tamagocha
from tamagocha_pkg.storage import load_state, save_state
from tamagocha_pkg.timeutils import apply_decay
from tamagocha_pkg.interface import game_loop


def main():
    state = load_state()
    pet = Tamagocha(
        state["name"], state["eda"], state["socialka"],
        state["bdsm"], state["trash"], state["tired"],
    )
    apply_decay(pet, state["time"])
    game_loop(pet)

    state["eda"] = pet.eda
    state["socialka"] = pet.socialka
    state["bdsm"] = pet.bdsm
    state["trash"] = pet.trash
    state["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_state(state)


if __name__ == "__main__":
    main()
