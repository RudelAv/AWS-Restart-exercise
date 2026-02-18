import json

# fonction pour ajouter une mission
def ajouter_mission(chemin_json, nouvelle_mission):
    with open(chemin_json, "r") as f:
        data = json.load(f)
        dernier_id = int(data["missions"][-1]["id"].split("-")[1])
        nouvelle_mission["id"] = f"MSN-{dernier_id + 1:03d}"
        data["missions"].append(nouvelle_mission)

    # ecrire le fichier
    with open(chemin_json, "w") as f:
        json.dump(data, f, indent=4)
    print("Mission ajoute avec succes")


# supprimer une mission avec confirmation

def supprimer_mission(chemin_json, mission_id):
    with open(chemin_json, "r") as f:
        data = json.load(f)
        for mission in data["missions"]:
            if mission["id"] == mission_id:
                data["missions"].remove(mission)
                with open(chemin_json, "w") as f:
                    json.dump(data, f, indent=4)
                print("Mission supprime avec succes")
                return
        print("Mission non trouvee")

nouvelle = {
    "id": "MSN-006",
    "nom": "Proxima Relay",
    "destination": "Alpha Centauri (sonde)",
    "date_lancement": "2035-06-01",
    "statut": "théorique",
    "equipage": [],
    "duree_jours": 29200,
    "budget_millions_usd": 125000
}
ajouter_mission("mission-data/missions.json", nouvelle)
        

supprimer_mission("mission-data/missions.json", "MSN-006")
