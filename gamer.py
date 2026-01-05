import json  # Для сохранения и загрузки данных в формате JSON

class Gamer:  # Класс игрока
    def __init__(self, username="", health=120, max_health=120, attack=15, defense=5):
        self.username = username  # Имя игрока
        self.health = health  # Текущее здоровье
        self.max_health = max_health  # Максимальное здоровье
        self.attack = attack  # Сила атаки
        self.defense = defense  # Сила защиты
        self.artifacts = []  # Список артефактов игрока

    # Функция отображения всех статов и артефактов
    def show_full_stats(self):
        print("\n" + "="*30)  # Разделитель для удобства
        print(f"️ {self.username}'s Stats:")
        print(f"HP: {self.health}/{self.max_health} | ATK: {self.attack} | DEF: {self.defense}")
        if self.artifacts:  # Если есть артефакты
            print("Артефакты:")
            for art in self.artifacts:
                print(f"- {art}")
        else:
            print("Артефактов пока нет.")
        print("="*30)

    # Функция получения урона игроком
    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)  # Уменьшаем урон на защиту
        self.health -= actual_damage  # Вычитаем урон из здоровья
        return actual_damage  # Возвращаем фактический урон

    # Функция добавления артефакта и применения бонусов
    def add_artifact(self, artifact_name):
        if artifact_name in self.artifacts:  # Если такой артефакт уже есть
            print(f"У тебя уже есть {artifact_name}!")
            return

        self.artifacts.append(artifact_name)  # Добавляем артефакт
        print(f" Ты получил артефакт: {artifact_name}")

        # Применяем бонусы в зависимости от артефакта
        if artifact_name == "Ржавое копьё гладиатора":
            self.attack += 8
            print(" Атака +8")
        elif artifact_name == "Бронзовый нагрудник":
            self.defense += 10
            print(" Защита +10")
        elif artifact_name == "Благословение Гипноса":
            self.max_health += 30
            self.health += 30
            print("️ Здоровье +30")
        elif artifact_name == "Амулет Афины":
            self.attack += 5
            self.defense += 5
            print("️ Атака +5 |  Защита +5")
        elif artifact_name == "Каменный молот":
            self.attack += 12
            print("️ Атака +12")
        elif artifact_name == "Кожаные поножи":
            self.max_health += 15
            self.health += 15
            print("️ Здоровье +15")
        elif artifact_name == "Зелье стойкости":
            self.defense += 8
            print(" Защита +8")
        elif artifact_name == "Священная кошка":
            print(" Кошка приносит мораль, но не увеличивает статы")

        elif artifact_name == "Золото полиса":
            self.health += 20
            self.defense += 5
            print("️ Здоровье +20 |  Защита +5")