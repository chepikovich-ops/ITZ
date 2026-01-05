class Boss:
    def __init__(self, name, hp, max_hp, attack):
        # Имя врага
        self.name = name

        # Текущее здоровье врага
        self.hp = hp

        # Максимальное здоровье врага
        self.max_hp = max_hp

        # Сила атаки врага
        self.attack = attack

    def take_damage(self, damage):
        # Уменьшаем здоровье врага на полученный урон
        self.hp -= damage