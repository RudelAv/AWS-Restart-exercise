import os

if os.path.exists("mission-data"):
    if os.path.exists("mission-data/rapports"):
        print("Le dossier rapports existe")
    else:
        os.makedirs("mission-data/rapports")

    if os.path.exists("mission-data/archives"):
        print("Le fichier rapport.txt existe")
    else:
        os.makedirs("mission-data/archives")
       
    for file in os.listdir("mission-data"):
        print(file)
        print("Taille du fichier : " + str(os.path.getsize("mission-data/" + file)/1000) + " ko")
    

else:
    print("Erreur: Le dossier n'existe pas")