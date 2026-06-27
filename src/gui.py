import tkinter as tk
from tkinter import filedialog, messagebox

from src.async_handler import run_async
from src.json_handler import read_json
from src.yaml_handler import read_yaml
from src.xml_handler import read_xml


window = tk.Tk()
window.title("Projekt - Narzędzia w branży IT")
window.geometry("800x600")

text = tk.Text(window, font=("Arial", 12))
text.pack(fill="both", expand=True)


def load_file(path):

    if path.endswith(".json"):
        data = read_json(path)

    elif path.endswith(".yaml"):
        data = read_yaml(path)

    elif path.endswith(".xml"):
        data = read_xml(path)

    else:
        messagebox.showerror("Błąd", "Nieznany format.")
        return

    text.delete("1.0", tk.END)
    text.insert(tk.END, str(data))


def open_file():

    path = filedialog.askopenfilename(
        filetypes=[
            ("JSON", "*.json"),
            ("YAML", "*.yaml"),
            ("XML", "*.xml")
        ]
    )

    if not path:
        return

    run_async(load_file, path)


button = tk.Button(
    window,
    text="Otwórz plik",
    command=open_file,
    width=20,
    height=2
)

button.pack(pady=10)

window.mainloop()