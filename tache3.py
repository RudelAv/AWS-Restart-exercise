import json

with open("mission-data/missions.json", "r") as file:
    data = json.load(file)
    numMission = 1
    totalBudget = 0
    for mission in data["missions"]:
        totalBudget += mission["budget_millions_usd"]
        
        # Afficher le resume de chaque mission
        print("[MSN-00" + str(numMission) + "]" + mission["nom"] + "-> " + mission["destination"] +  "| " + str(mission["duree_jours"]) + " jours " + " | Equipage: " + str(mission["equipage"]) + " | " + str(mission["budget_millions_usd"]) + " M$" + " | Date de lancement: " + mission["date_lancement"] + " | Statut: " + mission["statut"])

        # Afficher la mission la plus longue
        maxDuree = mission["duree_jours"]
        missionPlusLongue = mission
        
        if mission["duree_jours"] > maxDuree:
            maxDuree = mission["duree_jours"]
            missionPlusLongue = mission
        

        numMission += 1
    print("Le budget total est de: " + str(totalBudget) + " M$")
    print("la mission la plus longue est: " + missionPlusLongue["nom"] + " avec pour duree " + str(missionPlusLongue["duree_jours"]) + " jours")