## Municipality Module
# Features:
- Steuern erheben, Einnahmen und Ausgaben verwalten von verschiedenen Gebäuden.
- Abwanderung basierend auf der Zufriedenheit der Bürger imulieren.
- Einführen von Ereignissen mit unterschiedlichen Auswirkungen auf Zufriedenheit und Kontostand.

# Klassen:
- Municipality: Repräsentiert eine Gemeinde mit Bürgern, Gebäuden und Veranstaltungen.
- Citizens: Verwaltet die Bevölkerung und deren Zufriedenheit.
- Building (z. B. Schule, Polizeistation, Krankenhaus): Repräsentiert verschiedene Arten von Gebäuden in der Gemeinde.
- Event: Stellt Ereignisse dar, die in der Gemeinde auftreten können.
- SatisfactionFactors: Speichert Faktoren, die die Zufriedenheit der Bürger beeinflussen.
  
# Methoden
- simulate_one_round(): Simuliert eine Runde der Gemeinde, aktualisiert das Kontostand, die Bürger und löst Ereignisse aus.
- get_satisfaction(): Berechnet und liefert die Gesamtzufriedenheit der Bürger.
- get_satisfaction_factors(): Liefert die Zufriedenheitsfaktoren, die die Bürger betreffen.
- debug_print_stats(): Druckt die aktuelle Bürgerzahl und den Kontostand.
- add_building(name: str): Fügt ein neues Gebäude des angegebenen Typs hinzu.
- demolish_building(name: str): Reißt ein Gebäude des angegebenen Typs ab.
- sim_migration(satisfaction: float): Simuliert die Migration auf der Grundlage der Zufriedenheit der Bürger.
- create_event(): Erzeugt nach dem Zufallsprinzip ein Ereignis mit den angegebenen Auswirkungen.
- predict_migration(): Sagt die Migration auf der Grundlage der aktuellen Zufriedenheit voraus.

## Citizens Module
# Features:
- Verwaltung der Bevölkerung einer simulierten Gemeinde. 
- Erhebung von Steuern auf der Grundlage eines festgelegten Steuersatzes.
- Berechnung der Gesamtzufriedenheit der Bürger unter Berücksichtigung verschiedener Faktoren.
- Ermittlung der Migrationsraten auf der Grundlage der Zufriedenheit der Bürger.

# Klassen:
- Citizens: Repräsentiert die Bevölkerung einer Gemeinde mit Methoden zur Steuererhebung, Zufriedenheitsberechnung und Wanderungsbestimmung.

# Methoden:
- collect_taxes(tax_rate: float) -> int: Erhebt Steuern von den Bürgern auf der Grundlage des angegebenen Steuersatzes.
- get_total_satisfaction(tax_rate: float, buildings: list[object], event: object) -> float: Berechnet die Gesamtzufriedenheit der Bürger unter Berücksichtigung von Steuersätzen, Gebäuden und Ereignissen.
- get_satisfaction_factors(buildings: list[object], event: object) -> object: Berechnet die Zufriedenheitsfaktoren auf der Grundlage von Gebäuden und Ereignissen.
- tax_rate_satisfaction_penalty(tax_rate: float) -> float: Berechnet die Zufriedenheitsstrafe auf der Grundlage des Steuersatzes.
- base_satisfaction_factors() -> object: Ermittelt die Basiszufriedenheitsfaktoren auf der Grundlage der Bevölkerungsgröße der Stadt.
- determine_migration(satisfaction) -> int: Ermittelt die Migrationsraten auf der Grundlage der Zufriedenheit der Bürger.

## Building Module
# Features:
- Abstrakte Gebäudeklasse für die Gebäudeverwaltung.
- BasicBuilding-Klasse mit allgemeinen Funktionalitäten für Gebäude.
- Verschiedene Gebäudetypen (z. B. Schule, ElectircityGrid, BusStation) mit spezifischen Eigenschaften und Methoden.

# Klassen:
- Building: Abstrakte Basisklasse für alle Gebäudetypen.
- BasicBuilding: Klasse zur Darstellung von zum Leben wichtigen Gebäuden in der Gemeinde.
- ElectiveBuilding: Klasse zur Darstellung von Wahlgebäuden in der Gemeinde.
  
# Methoden:
Gemeinsame Methoden für alle Gebäudetypen, wie:
- build(), destroy(), get_build_cost() und get_satisfaction_factor_influence().

## Satisfaction Factors Module
# Features:
- SatisfactionFactors Klasse: zur Darstellung und Manipulation von Faktoren, die die Zufriedenheit der Bürger beeinflussen.
- Methoden zum Skalieren, Multiplizieren, Potenzieren und Berechnen des Durchschnitts der Zufriedenheitsfaktoren.

# Klasse: 
- SatisfactionFactors: stellt die Zufriedenheitsfaktoren: Infrastruktur, Sicherheit, Gesundheit und Unterhaltung dar.

## Event Module
# Features: 
- Ereignisklasse zur Darstellung von Ereignissen in der Gemeinde.
- Jedes Ereignis hat einen Namen, eine Beschreibung, Auswirkungen auf den Zufriedenheitsfaktor und eine Auswirkung auf das finanzielle Gleichgewicht.


## Wie eine Runde aussieht.
1. Rundeanzahl 
2. Einwohnerzahl
3. Immigration + Zulassungung auswählen
4. Kontostand
5. Steuersatz + Wunschsatz eingeben
6. Event

# Basic Setup:
- 10k Einwohner
- 1 Stromnetz
- 2 Schulen
- 2 Polizeistationen
- 10 Bushaltenestellen
  
# Mögliche Events
- Naturkatastrophe
- Konzert


# Authoren:
- 6963879, Tverdohleb
- 8291925, Hoffmann
