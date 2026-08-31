"""Основна модель персонажа тамагочі."""

MIN_STAT = 0
MAX_STAT = 100

STAT_LABELS = {
    "eda": ("Голод", "Спасибо было вкусно!"),
    "tired": ("Усталость", "Я выспалась!"),
    "trash": ("Уровень загрязненности комнаты", "Какая чистота!"),
    "socialka": ("Потебность в общении", "Я так хорошо погуляла!"),
    "bdsm": ("Потребность в страданиях", "Это было великолепно!"),
}

DEATH_MESSAGES = {
    "eda": "Ваш персонаж умер от голода",
    "trash": "Ваш персонаж умер в грязи от инфекций",
    "bdsm": "Ваш персонаж совершил суицид",
    "tired": "Ваш персонаж устал до смерти",
    "socialka": "Ваш персонаж умер от одиночества",
}


def clamp(value, low=MIN_STAT, high=MAX_STAT):
    """Обмежує значення показника діапазоном [low, high]."""
    return max(low, min(high, value))


class Tamagocha:
    """Представляє стан персонажа-тамагочі та його показники."""

    STAT_KEYS = ("eda", "socialka", "bdsm", "trash", "tired")

    def __init__(self, name, eda, socialka, bdsm, trash, tired):
        if not name:
            raise ValueError("name must not be empty")
        self.name = name
        self.eda = clamp(eda)
        self.socialka = clamp(socialka)
        self.bdsm = clamp(bdsm)
        self.trash = clamp(trash)
        self.tired = clamp(tired)

    def status_text(self):
        lines = ["Статус", str(self.name)]
        for key in self.STAT_KEYS:
            label, _ = STAT_LABELS[key]
            lines.append(label + " = " + str(getattr(self, key)))
        return "\n".join(lines)

    def restore(self, stat):
        """Відновлює вказаний показник до максимуму та повертає повідомлення."""
        if stat not in STAT_LABELS:
            raise ValueError(f"unknown stat: {stat}")
        setattr(self, stat, MAX_STAT)
        label, message = STAT_LABELS[stat]
        return f"{message}\n{label} = {getattr(self, stat)}"

    def feed(self):
        return self.restore("eda")

    def sleep(self):
        return self.restore("tired")

    def clean(self):
        return self.restore("trash")

    def socialize(self):
        return self.restore("socialka")

    def bdsm_club(self):
        return self.restore("bdsm")

    def death_message(self):
        for key in self.STAT_KEYS:
            if getattr(self, key) <= 0:
                return DEATH_MESSAGES[key]
        return None
