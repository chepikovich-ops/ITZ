import random  # Импортируем модуль random для случайного выбора


class ArtifactBank:
    def __init__(self):
        # Базовый список артефактов античноcти
        self.base_artifacts = [
            "Меч гоплита",
            "Щит Афины",
            "Шлем Ареса",
            "Сандалии Гермеса",
            "Амулет Аполлона",
            "Пояс Геракла"
        ]

        # Доступные артефакты (копия базового списка)
        self.available_artifacts = self.base_artifacts.copy()

    def get_random_artifact(self):
        # Если артефакты закончились — пересоздаём банк
        if not self.available_artifacts:
            print("\n Древние силы возрождают утраченные артефакты...\n")
            self.available_artifacts = self.base_artifacts.copy()

        # Выбираем случайный артефакт
        artifact = random.choice(self.available_artifacts)

        # Удаляем его из доступных
        self.available_artifacts.remove(artifact)

        # Возвращаем название артефакта
        return artifact
