class Gamer:
    def __init__(self, username=""):
        # Имя игрока
        self.username = username

        # Базовые характеристики
        self.health = 150
        self.max_health = 150
        self.attack = 15
        self.defense = 0

        # Список артефактов
        self.artifacts = []

    def add_artifact(self, artifact):
        # Добавляем артефакт, если его ещё нет
        if artifact in self.artifacts:
            return

        self.artifacts.append(artifact)

        print(f"\n Ты нашёл артефакт: {artifact}")

        # Эффекты артефактов
        if artifact == "Меч гоплита":
            self.attack += 10
            print("️ Атака +10")

        elif artifact == "Щит Афины":
            self.defense += 15
            print(" Защита +15")

        elif artifact == "Шлем Ареса":
            self.attack += 9
            self.defense += 10
            print("️ Атака +9, ️ Защита +10")

        elif artifact == "Сандалии Гермеса":
            self.max_health += 15
            self.health += 15
            print("️ Максимальное здоровье +15")

        elif artifact == "Амулет Аполлона":
            self.health = min(self.max_health, self.health + 35)
            print(" Восстановлено 35 здоровья")

        elif artifact == "Пояс Геракла":
            self.attack += 20
            self.max_health += 30
            self.health += 30
            print(" Атака +20, ️ Макс. здоровье +30")

    def show_full_stats(self):
        # Выводим все характеристики игрока
        print("\n ТВОЯ СТАТИСТИКА")
        print(f"Здоровье: {self.health}/{self.max_health}")
        print(f"Атака: {self.attack}")
        print(f"Защита: {self.defense}")

        if not self.artifacts:
            print("Артефакты: нет")
        else:
            print("Артефакты:")
            for art in self.artifacts:
                print(f" - {art}")

    def to_dict(self):
        # Сохраняем данные игрока в словарь
        return {
            "username": self.username,
            "health": self.health,
            "max_health": self.max_health,
            "attack": self.attack,
            "defense": self.defense,
            "artifacts": self.artifacts,

        }

    def load_from_dict(self, data):
        # Загружаем данные игрока из словаря
        self.health = data["health"]
        self.max_health = data["max_health"]
        self.attack = data["attack"]
        self.defense = data["defense"]
        self.artifacts = data["artifacts"]