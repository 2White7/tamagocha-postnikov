"""Точка входу симулятора тамагочі."""
import logging
from datetime import datetime

from tamagocha_pkg.model import Tamagocha
from tamagocha_pkg.storage import load_state, save_state
from tamagocha_pkg.timeutils import apply_decay
from tamagocha_pkg.interface import game_loop

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger("tamagocha")


def main():
    state = load_state()
    logger.info("Loaded state for pet: %s", state["name"])
    pet = Tamagocha(
        state["name"], state["eda"], state["socialka"],
        state["bdsm"], state["trash"], state["tired"],
    )
    apply_decay(pet, state["time"])
    logger.info("Decay applied, entering game loop")
    game_loop(pet)

    state["eda"] = pet.eda
    state["socialka"] = pet.socialka
    state["bdsm"] = pet.bdsm
    state["trash"] = pet.trash
    state["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    save_state(state)
    logger.info("Session saved, exiting")


if __name__ == "__main__":
    main()
