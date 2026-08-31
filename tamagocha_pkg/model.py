"""Основна модель персонажа тамагочі."""


class Tamagocha:
    """Представляє стан персонажа-тамагочі та його показники."""

    def __init__(self, name, eda, socialka, bdsm, trash, tired):
        self.name = name
        self.eda = eda
        self.socialka = socialka
        self.bdsm = bdsm
        self.trash = trash
        self.tired = tired

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
