import json
import os
from datetime import datetime


# Chargement du fichier JSON

with open("mission-data/telemetrie.json", "r", encoding="utf-8") as f:
    data = json.load(f)

releves = data["releves"]
print(f"Mission : {data['mission']}")
print(f"Nombre de releves : {len(releves)}\n")



# Tableau resume 
def formater_altitude(km):
    """Formate l'altitude """
    if km >= 1000:
        return f"{km:,} km".replace(",", " ")
    return f"{km} km"


def get_alertes(systemes):
    return [sys for sys, etat in systemes.items() if etat != "nominal"]


# En-tete du tableau
col_phase    = 20
col_altitude = 16
col_vitesse  = 10
col_carbu    = 10
col_alertes  = 30

sep = f"{'─' * col_phase}-+-{'─' * col_altitude}-+-{'─' * col_vitesse}-+-{'─' * col_carbu}-+-{'─' * col_alertes}"

header = (
    f"{'Phase':<{col_phase}} | {'Altitude':<{col_altitude}} | "
    f"{'Vitesse':<{col_vitesse}} | {'Carburant':<{col_carbu}} | Alertes"
)

print("=" * len(sep))
print(header)
print(sep)

for r in releves:
    phase    = r["phase"]
    altitude = formater_altitude(r["position"]["altitude_km"])
    vitesse  = f"{r['vitesse_km_s']} km/s"
    carbu    = f"{r['carburant_pct']}%"
    alertes  = get_alertes(r["systemes"])
    alerte_str = ", ".join(alertes) if alertes else "-"

    print(
        f"{phase:<{col_phase}} | {altitude:<{col_altitude}} | "
        f"{vitesse:<{col_vitesse}} | {carbu:<{col_carbu}} | {alerte_str}"
    )

print("=" * len(sep))


# Consommation moyenne de carburant par jour

fmt = "%Y-%m-%dT%H:%M:%S"
ts_premier = datetime.strptime(releves[0]["timestamp"], fmt)
ts_dernier = datetime.strptime(releves[-1]["timestamp"], fmt)

duree_jours = (ts_dernier - ts_premier).total_seconds() / 86400
conso_totale = releves[0]["carburant_pct"] - releves[-1]["carburant_pct"]
conso_par_jour = conso_totale / duree_jours

print(f"\n Periode        : {ts_premier.strftime('%d/%m/%Y')} → {ts_dernier.strftime('%d/%m/%Y')}")
print(f"  Duree          : {duree_jours:.1f} jours")
print(f" Conso totale   : {conso_totale:.1f}%")
print(f"📊 Conso/jour     : {conso_par_jour:.4f}% par jour")


# Relevés avec au moins une alerte

releves_alertes = []

for r in releves:
    alertes = get_alertes(r["systemes"])
    if alertes:
        releves_alertes.append({
            "phase": r["phase"],
            "timestamp": r["timestamp"],
            "altitude_km": r["position"]["altitude_km"],
            "vitesse_km_s": r["vitesse_km_s"],
            "carburant_pct": r["carburant_pct"],
            "systemes_en_anomalie": alertes
        })

print(f"\n🚨 Releves avec alertes ({len(releves_alertes)} sur {len(releves)}) :")
for ra in releves_alertes:
    ts = datetime.strptime(ra["timestamp"], fmt).strftime("%d/%m/%Y %H:%M")
    print(f"   • [{ts}] Phase '{ra['phase']}' → {', '.join(ra['systemes_en_anomalie'])}")


# Sauvegarde dans mission-data/rapports/

dossier = os.path.join("mission_data", "rapports")
os.makedirs(dossier, exist_ok=True)
chemin_sortie = os.path.join(dossier, "alertes_systemes.json")

rapport = {
    "mission": data["mission"],
    "genere_le": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
    "statistiques": {
        "total_releves": len(releves),
        "releves_avec_alertes": len(releves_alertes),
        "duree_mission_jours": round(duree_jours, 1),
        "consommation_carburant_totale_pct": round(conso_totale, 2),
        "consommation_moyenne_par_jour_pct": round(conso_par_jour, 4)
    },
    "alertes": releves_alertes
}

with open("mission_data/rapports/alertes_systemes.json", "w", encoding="utf-8") as f:
    json.dump(rapport, f, ensure_ascii=False, indent=2)

print(f"\n Rapport sauvegarde → mission_data/rapports/alertes_systemes.json")
