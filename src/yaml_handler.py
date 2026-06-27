import yaml


def read_yaml(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = yaml.safe_load(file)

        print("\nDane z pliku YAML:")
        print(data)

        return data

    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku.")

    except yaml.YAMLError:
        print("Błąd: Niepoprawna składnia YAML.")

    except Exception as e:
        print("Wystąpił błąd:", e)


def save_yaml(path, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            yaml.dump(
                data,
                file,
                allow_unicode=True,
                sort_keys=False
            )

        print("Plik YAML został zapisany.")

    except Exception as e:
        print("Błąd podczas zapisu:", e)