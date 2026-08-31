"""Обчислення занепаду показників персонажа з часом."""
import re
from datetime import datetime

from tamagocha_pkg.model import clamp


def parse_time(time_str):
    c = re.split(":| |-", time_str)
    y, m, d, h, mi, s = (int(x) for x in c)
    return datetime(y, m, d, h, mi, s)


def apply_decay(pet, saved_time_str, now=None):
    now = now or datetime.now()
    saved_time = parse_time(saved_time_str)
    delta = now - saved_time
    # BUG FIX: раніше `delta.seconds` рахував лише секунди в межах поточної
    # доби (0-86399) і ігнорував `delta.days`, тому після перерви довшої
    # за добу занепад показників рахувався некоректно (занадто малим).
    total_minutes = delta.days * 24 * 60 + delta.seconds // 60
    pet.eda = clamp(pet.eda - total_minutes // 15)
    pet.socialka = clamp(pet.socialka - total_minutes // 20)
    pet.bdsm = clamp(pet.bdsm - total_minutes // 60)
    pet.tired = clamp(pet.tired - total_minutes // 15)
    pet.trash = clamp(pet.trash - total_minutes // 25)
    return pet
