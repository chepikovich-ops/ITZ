import random  # Импортируем модуль random для случайных чисел

from gamer import Gamer  # Импортируем класс игрока
from boss import Boss  # Импортируем класс врага
from artefacts import ArtifactBank  # Импортируем банк артефактов

# Функция для безопасного выбора пользователя
def get_choice(options):
    while True:  # Цикл продолжается, пока игрок не введет правильное число
        try:
            choice = int(input("Твой выбор: "))  # Преобразуем ввод в число
            if choice in options:  # Если число допустимо
                return choice  # Возвращаем его
            else:
                print("Неверный вариант.")  # Сообщаем о неверном выборе
        except ValueError:  # Если введено не число
            print("Введите число.")  # Просим ввести число

# Функция для отображения статистики боя
def show_battle_stats(player, enemy):
    print("\n" + "="*30)  # Разделитель
    print(f" {player.health}/{player.max_health} HP |  {player.attack} ATK |  {player.defense} DEF")  # Статы игрока
    print(f" {enemy.name}: {enemy.hp}/{enemy.max_hp} HP | ️ {enemy.strength} ATK")  # Статы врага
    print("="*30)  # Разделитель

class Game :  # Класс самой игры
    def __init__(self):
        self.player = Gamer()  # Создаём объект игрока
        self.artifact_bank = ArtifactBank()  # Создаём банк артефактов
        # Список всех артефактов
        self.artifact_bank.available_artifacts = [
            "Ржавое копьё гладиатора",
            "Бронзовый нагрудник",
            "Благословение Гипноса",
            "Амулет Афины",
            "Каменный молот",
            "Кожаные поножи",
            "Зелье стойкости",
            "Золото полиса"
        ]
        self.noise = 0  # Уровень шума (увеличивается при активных действиях)
        self.blessing = False  # Флаг благословения от богов
        self.preparation = 0  # Очки подготовки (влияют на шансы против Минотавра)
        self.decisions = []  # Список сделанных выборов для анализа финала

    # Метод боя
    def battle(self, enemy):
        print(f"\n Начинается бой с {enemy.name}!")  # Сообщение о начале боя
        while enemy.hp > 0 and self.player.health > 0:  # Пока оба живы
            show_battle_stats(self.player, enemy)  # Показываем текущие статы
            print("1. Атаковать\n2. Защищаться\n3. Посмотреть статистику")  # Опции
            choice = get_choice([1, 2, 3])  # Получаем выбор игрока
            if choice == 3:  # Если игрок хочет посмотреть статистику
                self.player.show_full_stats()  # Показываем статистику игрока
                continue  # Возвращаемся к выбору
            if choice == 1:  # Если атакуем
                enemy.hp -= self.player.attack  # Уменьшаем здоровье врага
                print(f"Ты наносишь {self.player.attack} урона!")  # Сообщаем о нанесённом уроне
                self.noise += 1  # Шум увеличивается
            elif choice == 2:  # Если защищаемся
                reduced = max(0, enemy.strength - self.player.defense - 2)  # Считаем урон после защиты
                self.player.health -= reduced  # Уменьшаем здоровье игрока
                print(f"Ты защищаешься и получаешь {reduced} урона.")  # Сообщаем о полученном уроне
            if enemy.hp > 0:  # Если враг жив
                enemy.attack(self.player)  # Он атакует

        return self.player.health > 0  # Возвращаем True, если игрок жив

    # Метод получения артефакта
    def get_artifact(self):
        prize = self.artifact_bank.get_random_artifact()  # Берём случайный артефакт из банка
        if prize:  # Если артефакт найден
            self.player.add_artifact(prize)  # Добавляем артефакт игроку
            print(f" {self.artifact_bank.get_description(prize)}")  # Показываем описание артефакта

    # Метод запуска сюжета
    def start(self):
        print(" ЛАБИРИНТ МИНОТАВРА ")  # Заголовок игры
        print("Ты — гладиатор, брошенный в древний лабиринт в котором погибло множество героев.\n")  # Вводная история
        self.player.show_full_stats()  # Показываем начальные статы игрока

        # Вход в лабиринт
        print("\nПеред тобой зев лабиринта.")
        print("1. Смело войти\n2. Осторожно продвигаться")
        choice = get_choice([1, 2])
        self.decisions.append(choice)  # Сохраняем решение
        if choice == 1:  # Смелый вход
            self.noise += 2  # Увеличиваем шум
            if not self.battle(Boss("Страж лабиринта", 17, 90, 9)):  # Бой с охранником
                print(" Ты пал в самом начале пути.")  # Игрок умер
                return
        else:  # Осторожное продвижение
            self.get_artifact()  # Получаем артефакт
            self.preparation += 1  # Подготовка увеличивается

        # 2 выбор — первый зал
        print("\nТы доходишь до первого зала.")
        print("1. Осмотреть алтарь\n2. Пойти по левому коридору\n3. Пойти по правому коридору")
        choice = get_choice([1, 2, 3])
        self.decisions.append(choice)
        if choice == 1:
            if random.randint(1, 6) >= 4:  # Шанс получить благословение
                print("Боги благосклонны! Ты получаешь благословение.")
                self.blessing = True
            else:
                print("Боги молчат...")
        elif choice == 2:
            if not self.battle(Boss("Тень лабиринта", 37, 80, 12)):
                print(" Ты погиб в тени.")
                return
        else:
            self.get_artifact()
            self.preparation += 1

        # 3 выбор — ловушки
        print("\nТы видишь два пути.")
        print("1. Лабиринтная ловушка\n2. Тайный проход\n3. Зал с обломками")
        choice = get_choice([1, 2, 3])
        self.decisions.append(choice)
        if choice == 1:
            if self.noise >= 3:
                if not self.battle(Boss("Ловушка + монстр", 68, 100, 14)):
                    print(" Ты погиб в ловушке.")
                    return
            else:
                print("Ты тихо обошел ловушку.")
        elif choice == 2:
            self.get_artifact()
            self.preparation += 1
        else:
            if not self.battle(Boss("Скелет-страж", 40, 60, 10)):
                print(" Погиб от скелета.")
                return

        # 4 выбор — загадка
        print("\nТы находишь древний рунный камень с загадкой.")
        print("1. Решить загадку\n2. Игнорировать")
        choice = get_choice([1, 2])
        self.decisions.append(choice)
        if choice == 1:
            if random.randint(1, 2) == 1:
                print("Ты решаешь загадку и находишь артефакт!")
                self.get_artifact()
                self.preparation += 1
            else:
                print("Неудача, ничего не происходит.")
        else:
            print("Ты идёшь дальше.")

        # 5 выбор — мост
        print("\nТы подходишь к разрушенному мосту.")
        print("1. Перепрыгнуть\n2. Пройти по старому мосту")
        choice = get_choice([1, 2])
        self.decisions.append(choice)
        if choice == 1:
            if not self.battle(Boss("Летучий охранник", 30, 70, 13)):
                print(" Падение в пропасть.")
                return
            self.preparation += 1
        else:
            print("Старый мост держит, но шум увеличен.")
            self.noise += 2

        # 6 выбор — затаиться или идти напролом
        print("\nТы видишь свет в конце коридора.")
        print("1. Затаиться и обойти\n2. Идти напролом")
        choice = get_choice([1, 2])
        self.decisions.append(choice)
        if choice == 1:
            print("Ты тихо обходишь опасность.")
            self.preparation += 1
        else:
            if not self.battle(Boss("Хранитель коридора", 45, 90, 15)):
                print(" Погиб в бою.")
                return

        # 7 выбор — сокровищница
        print("\nСокровищница перед тобой.")
        print("1. Взять артефакт\n2. Игнорировать")
        choice = get_choice([1, 2])
        self.decisions.append(choice)
        if choice == 1:
            self.get_artifact()
            self.preparation += 1

        # 8 выбор — ещё один коридор
        print("\nДва пути: левый и правый.")
        print("1. Левый\n2. Правый")
        choice = get_choice([1, 2])
        self.decisions.append(choice)
        if choice == 1:
            if not self.battle(Boss("Тёмный страж", 40, 80, 12)):
                print(" Погиб в темноте.")
                return
            self.preparation += 1
        else:
            self.get_artifact()
            self.preparation += 1

        # 9 выбор — мост перед Минотавром
        print("\nТы подходишь к залу Минотавра.")
        print("1. Войти смело\n2. Осторожно продвигаться")
        choice = get_choice([1, 2])
        self.decisions.append(choice)
        if choice == 1:
            self.noise += 2
        else:
            self.preparation += 1

        # Финальный бой с Минотавром
        print("\nТы слышишь дыхание Минотавра впереди.")
        if self.blessing or self.preparation >= 5:
            print("Ты готов к бою.")
            boss = Boss("Минотавр", 150, 150, 16)
        else:
            print("Ты застигнут врасплох!")
            boss = Boss("Минотавр", 180, 180, 18)
        if not self.battle(boss):
            print(" Ты пал перед Минотавром.")
            return

        # Определяем концовку
        print("\n Ты побеждаешь Минотавра!")
        if self.player.health >= 100 and self.preparation >= 7 and self.blessing:
            print("️ Легендарная концовка: весь лабиринт покорен и ты стал легендой!")
        elif self.player.health >= 70 and self.preparation >= 5:
            print(" Хорошая концовка: ты победил, но испытания оставили след.")
        else:
            print(" Плохая концовка: победа далась с трудом, многие враги остались позади.")

if __name__ == "__main__":
    game = Game()  # Создаём объект игры
    game.start()  # Запускаем игру