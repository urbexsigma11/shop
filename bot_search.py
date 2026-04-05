import json
import requests
import datetime

# Twoje źródła z pliku bookmarks.html i inne
SOURCES = [
    "http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/",
    "https://pixa.com.pl/"
]

def update_shop():
    new_inventory = []
    
    # Symulacja wyszukiwania - tutaj dodajesz logikę wyciągania cen
    # Dla Pixa.com.pl dodajemy Twoje +10%
    base_pixa_price = 100 
    
    new_inventory.append({
        "id": "lq_new_batch",
        "name": f"LQ SPEC-BATCH {datetime.datetime.now().strftime('%m/%Y')}",
        "price": 130,
        "category": "OP",
        "desc": "Nowy rzut z importu."
    })
    
    new_inventory.append({
        "id": "pixa_resell",
        "name": "PIXA RE-DROP",
        "price": round(base_pixa_price * 1.10, 2),
        "category": "IMPORT",
        "desc": "Automatyczny import z Pixa + 10% marży."
    })

    with open('data.json', 'w') as f:
        json.dump(new_inventory, f, indent=4)
    print("Baza towaru zaktualizowana.")

if __name__ == "__main__":
    update_shop()
