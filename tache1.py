with open("mission-data/journal_bord.txt", "r") as file:
    nb_line = 0
    for line in file:
        if "Alerte" in line:
            print(line)
            with open("mission-data/alertes.txt", "a") as file2:
                file2.write(line)
            print("Fichier alertes.txt cree")
        elif "alerte" in line:
            print(line)
            with open("mission-data/alertes.txt", "a") as file2:
                file2.write(line)
            print("Fichier alertes.txt cree")
        nb_line += 1

    print("le nombre de ligne est: " + str(nb_line))
