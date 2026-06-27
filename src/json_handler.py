import json


def read_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print("\nDane z pliku JSON:")
        print(data)

        return data

    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku.")

    except json.JSONDecodeError:
        print("Błąd: Niepoprawna składnia JSON.")

    except Exception as e:
        print("Wystąpił błąd:", e)


def save_json(path, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("Plik JSON został zapisany.")

    except Exception as e:
        print("Błąd podczas zapisu:", e)