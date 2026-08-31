"""Обчислення занепаду показників персонажа з часом."""
import re
from datetime import datetime


def parse_time(time_str):
    c = re.split(":| |-", time_str)
    y, m, d, h, mi, s = (int(x) for x in c)
    return datetime(y, m, d, h, mi, s)


def apply_decay(pet, saved_time_str, now=None):
    now = now or datetime.now()
    saved_time = parse_time(saved_time_str)
    delta = now - saved_time
    minutes = delta.seconds // 60
    pet.eda -= minutes // 15
    pet.socialka -= minutes // 20
    pet.bdsm -= minutes // 60
    pet.tired -= minutes // 15
    pet.trash -= minutes // 25
    return pet
