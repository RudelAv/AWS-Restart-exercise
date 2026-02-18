import json

# Charger le fichier JSON
def charger_json_securise(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            print(file_path + " charge avec succes " + str(len(data["missions"])) + " missions")
            return data
    except FileNotFoundError:
        print("Fichier introuvable : " + file_path)
    except json.JSONDecodeError:
        print("Json Invalide dans : " + file_path)
    except Exception as e:
        return None

# Cas 1 : fichier normal
data = charger_json_securise("mission-data/missions.json")

# Cas 2 : fichier inexistant
data = charger_json_securise("mission-data/fantome.json")

# Cas 3 : créez un fichier corrompu pour tester
with open("mission-data/corrompu.json", "w") as f:
    f.write("{nom: valeur_sans_guillemets}")
data = charger_json_securise("mission-data/corrompu.json")
