# Oppgave 5 – Miniprosjekt: aktivitetsplanlegger

import csv

def valider_aktivitet(title, category, date, minutter_tekst, status):
    if title == '' or category == '' or date == '' or status == '':
        return False, "et felt mangler"

    try:
        minutter = int(minutter_tekst)
    except ValueError:
        return False, "estimated_minutes er ikke et heltall"

    if minutter < 0:
        return False, "estimated_minutes må være planned eller completed"

    return True, ""

def les_aktiviteter (filnavn):
    aktiviteter = []

    try:
        with open(filnavn, mode='r', encoding="utf-8-") as (csv_file):
            leser = csv.DictReader(csv_file)
            for rad in leser:
                aktiviteter.append({
                    "title": rad["title"],
                    "category": rad["category"],
                    "date": rad["date"],
                    "estimated_minutes": int(rad["estimated_minutes"]),
                    "status": rad["status"],
                    })
    except FileNotFoundError:
        print(f"fant ikke {filnavn} - starter med tom liste")
    return aktiviteter

