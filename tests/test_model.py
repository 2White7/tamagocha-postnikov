"""Unit-тести для core-логіки тамагочі."""
from datetime import datetime

from tamagocha_pkg.model import Tamagocha, clamp
from tamagocha_pkg.timeutils import apply_decay
from tamagocha_pkg.interface import run_turn


def test_clamp_keeps_value_in_range():
    assert clamp(150) == 100
    assert clamp(-10) == 0
    assert clamp(42) == 42


def test_tamagocha_init_clamps_out_of_range_stats():
    pet = Tamagocha("Rex", 150, -5, 50, 50, 50)
    assert pet.eda == 100
    assert pet.socialka == 0


def test_feed_restores_eda_to_max():
    pet = Tamagocha("Rex", 10, 50, 50, 50, 50)
    pet.feed()
    assert pet.eda == 999  # навмисно зламаний тест (lab3, Частина 3)


def test_death_message_reports_lowest_priority_stat():
    pet = Tamagocha("Rex", 0, 50, 50, 50, 50)
    assert pet.death_message() == "Ваш персонаж умер от голода"


def test_death_message_none_when_alive():
    pet = Tamagocha("Rex", 50, 50, 50, 50, 50)
    assert pet.death_message() is None


def test_apply_decay_accounts_for_full_days_elapsed():
    pet = Tamagocha("Rex", 100, 100, 100, 100, 100)
    saved_time = "2024-01-01 00:00:00"
    now = datetime(2024, 1, 3, 0, 0, 0)  # +2 доби = 2880 хвилин
    apply_decay(pet, saved_time, now=now)
    # 2880 // 15 = 192, clamp до 0 (не в мінус)
    assert pet.eda == 0
    assert pet.tired == 0


def test_run_turn_status_choice_returns_text():
    pet = Tamagocha("Rex", 50, 50, 50, 50, 50)
    result = run_turn(pet, 1)
    assert "Статус" in result
