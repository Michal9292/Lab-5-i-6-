import argparse

from src.json_handler import read_json, save_json
from src.yaml_handler import read_yaml, save_yaml
from src.xml_handler import read_xml, save_xml

parser = argparse.ArgumentParser(
    description="Projekt - Narzędzia w branży IT"
)

parser.add_argument(
    "format",
    help="json, yaml lub xml"
)

parser.add_argument(
    "plik",
    help="Ścieżka do pliku"
)

args = parser.parse_args()

nowa_osoba = {
    "imie": "Anna",
    "wiek": 25,
    "miasto": "Kraków"
}

if args.format == "json":

    read_json(args.plik)
    save_json("data/nowy.json", nowa_osoba)

elif args.format == "yaml":

    read_yaml(args.plik)
    save_yaml("data/nowy.yaml", nowa_osoba)

elif args.format == "xml":

    read_xml(args.plik)

    xml_data = {
        "osoba": {
            "imie": "Anna",
            "wiek": "25",
            "miasto": "Kraków"
        }
    }

    save_xml("data/nowy.xml", xml_data)

else:
    print("Nieznany format.")