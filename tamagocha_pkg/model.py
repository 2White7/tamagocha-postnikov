"""Основна модель персонажа тамагочі."""

MIN_STAT = 0
MAX_STAT = 100


def clamp(value, low=MIN_STAT, high=MAX_STAT):
    """Обмежує значення показника діапазоном [low, high]."""
    return max(low, min(high, value))


class Tamagocha:
    """Представляє стан персонажа-тамагочі та його показники."""

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
        return (
            "Статус\n" + str(self.name)
            + "\nГолод = " + str(self.eda)
            + "\nУсталость = " + str(self.tired)
            + "\nУровень загрязненности комнаты = " + str(self.trash)
            + "\nПотебность в общении = " + str(self.socialka)
            + "\nПотребность в страданиях = " + str(self.bdsm)
        )

    def feed(self):
        self.eda = 100
        return "Спасибо было вкусно!\nГолод = " + str(self.eda)

    def sleep(self):
        self.tired = 100
        return "Я выспалась!\nУсталость = " + str(self.tired)

    def clean(self):
        self.trash = 100
        return "Какая чистота!\nУровень загрязнения = " + str(self.trash)

    def socialize(self):
        self.socialka = 100
        return "Я так хорошо погуляла!\nПотребность в общении = " + str(self.socialka)

    def bdsm_club(self):
        self.bdsm = 100
        return "Это было великолепно!\nПотребность в страданиях = " + str(self.bdsm)

    def death_message(self):
        if self.eda <= 0:
            return "Ваш персонаж умер от голода"
        if self.trash <= 0:
            return "Ваш персонаж умер в грязи от инфекций"
        if self.bdsm <= 0:
            return "Ваш персонаж совершил суицид"
        if self.tired <= 0:
            return "Ваш персонаж устал до смерти"
        if self.socialka <= 0:
            return "Ваш персонаж умер от одиночества"
        return None
