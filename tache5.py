import os
import datetime
import shutil

# copier et renommer le fichier journal_bord.txt

os.system("cp mission-data/journal_bord.txt mission-data/archives/journal_bord_" + datetime.datetime.now().strftime("%Y%m%d") + ".txt")

# creer le dossier rapports si il n'existe pas
os.makedirs("mission-data/rapports", exist_ok=True)

# creer le rapport
env_vars = {k: v for k, v in os.environ.items() if "PYTHON" in k or "PATH" in k}
usage = shutil.disk_usage("/")

with open("mission-data/rapports/rapport_systeme.txt", "w") as f:
    f.write(f"Repertoire courant: {os.getcwd()}\n\n")

