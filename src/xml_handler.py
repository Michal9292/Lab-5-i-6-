import xmltodict


def read_xml(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = xmltodict.parse(file.read())

        print("\nDane z pliku XML:")
        print(data)

        return data

    except FileNotFoundError:
        print("Błąd: Nie znaleziono pliku.")

    except Exception as e:
        print("Błąd XML:", e)


def save_xml(path, data):
    try:
        xml = xmltodict.unparse(data, pretty=True)

        with open(path, "w", encoding="utf-8") as file:
            file.write(xml)

        print("Plik XML został zapisany.")

    except Exception as e:
        print("Błąd podczas zapisu XML:", e)