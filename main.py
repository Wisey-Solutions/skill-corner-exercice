# This code has been formatted using Black with a maximum line width of 78 characters.

import sys
import json

def process_line(line_number: int, line: str) -> str:
    """
    Traite une ligne du fichier en fonction de certaines conditions.

    Args:
        line_number (int): Le numéro de la ligne.
        line (str): Le contenu de la ligne.

    Returns:
        str: Le résultat traité de la ligne.
    """
    if line_number % 5 == 0:
        new_data = "Multiple de 5"
    elif "$" in line:
        new_data = line.replace(" ", "_")
    elif line.endswith("."):
        new_data = line
    elif line.startswith("{"):
        try:
            new_data = json.dumps(
                {**json.loads(line), **{"pair": line_number % 2 == 0}}
            )
        except json.JSONDecodeError:
            new_data = "Rien à afficher"
    else:
        new_data = "Rien à afficher"

    return new_data


def process_file(filename: str) -> None:
    """
    Traite un fichier en parcourant ses lignes et en appliquant process_line à chacune.

    Args:
        filename (str): Le chemin vers le fichier à traiter.
    """
    with open(filename, "r") as file:
        for line_number, line in enumerate(file): # Using the file obj as Iterator for large files support
            new_data = process_line(line_number, line.strip())
            print(f"{line_number} : {new_data}")


def main():
    """
    Fonction principale du programme. Prend en charge les arguments de ligne de commande.
    """
    if len(sys.argv) != 2:
        print("Utilisation : python main.py <CHEMIN_VERS_FICHIER_LOGS>")
        return

    filename = sys.argv[1]
    try:
        process_file(filename=filename)
    except FileNotFoundError:
        print(f"Erreur : Le fichier {filename} n'existe pas")

if __name__ == "__main__":
    main()
