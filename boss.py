class Boss:  # Класс для врагов (боссов или обычных монстров)
    def __init__(self, name="Страж лабиринта", hp=150, max_hp=150, strength=10):  # Инициализация босса
        self.name = name  # Имя врага
        self.hp = hp  # Текущее здоровье
        self.max_hp = max_hp  # Максимальное здоровье
        self.strength = strength  # Сила атаки

    def take_damage(self, damage):  # Метод для получения урона
        self.hp -= damage  # Уменьшаем здоровье на полученный урон

    def attack(self, target):  # Обычная атака
        damage = self.strength  # Урон равен силе атаки
        print(f" {self.name} атакует и наносит {damage} урона!")  # Сообщение о атаке
        target.take_damage(damage)  # Применяем урон к цели (игроку)

    def strong_attack(self, target):  # Сильная атака
        damage = self.strength + 15  # Урон увеличен на 15
        print(f" {self.name} сильно атакует и наносит {damage} урона!")  # Сообщение о сильной атаке
        target.take_damage(damage)  # Применяем урон к цели