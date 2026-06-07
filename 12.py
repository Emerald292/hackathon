from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

class Anomaly:
    def __init__(self, description, threat_level):
        self.description = description
        self.threat_level = threat_level
        self.time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    def save_to_file(self):
        with open("anomalies.txt", "a", encoding="utf-8") as file:
            file.write(
                f"[{self.time}] Загроза: {self.threat_level} | {self.description}\n"
            )


def add_anomaly():
    print("\n=== Реєстрація аномалії ===")

    description = input("Що ви помітили в Академії? ")

    while True:
        try:
            threat_level = int(input("Оцініть рівень загрози (1-5): "))

            if 1 <= threat_level <= 5:
                break

            print("Введіть число від 1 до 5.")

        except ValueError:
            print("Потрібно ввести число.")

    anomaly = Anomaly(description, threat_level)
    anomaly.save_to_file()

    if threat_level == 5:
        print(Fore.RED + "☢ КРИТИЧНА АНОМАЛІЯ!" + Style.RESET_ALL)

    elif threat_level == 4:
        print(Fore.YELLOW + "⚠ УВАГА! Виявлено небезпечну аномалію!" + Style.RESET_ALL)

    else:
        print(Fore.GREEN + "✓ Аномалію успішно зареєстровано." + Style.RESET_ALL)

    print("\nДані зашифровано і збережено в архів. Дякуємо за службу!")
def show_archive():
    print("\n=== Архів аномалій ===")

    try:
        with open("anomalies.txt", "r", encoding="utf-8") as file:
            content = file.read()

            if content:
                print(content)
            else:
                print("Архів порожній.")

    except FileNotFoundError:
        print("Архів ще не створено.")


while True:
    print("\n=== СЕКРЕТНИЙ ТЕРМІНАЛ БЕЗПЕКИ ===")
    print("1. Зареєструвати аномалію")
    print("2. Переглянути архів")
    print("3. Вийти")

    choice = input("Ваш вибір: ")

    if choice == "1":
        add_anomaly()

    elif choice == "2":
        show_archive()

    elif choice == "3":
        print("Завершення роботи терміналу...")
        break

    else:
        print("Невірний вибір.")

