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


def skriv_aktiviteter (aktiviteter, filnavn):
    with open(filnavn, mode='w', encoding="utf-8-", newline="") as (csv_file):
        felt = ["title", "category", "date", "estimated_minutes", "status"]
        skriver = csv.DictWriter(csv_file, fieldnames=felt)
        skriver.writeheader()
        for aktivitet in aktiviteter:
            skriver.writerow(aktivitet)

def sok_aktiviteter (aktiviteter, søkeord):
    treff = ()
    for aktivitet in aktiviteter:
        if søkeord in aktivitet["title"] or søkeord in aktivitet["category"]:
           treff.append(aktivitet)
    return treff

def filtrer_på_status (aktiviteter, status):
    treff = []
    for aktivitet in aktiviteter:
        if aktivitet["status"] == status:
            treff.append(aktivitet)
    return treff

def sorter_på_dato (aktiviteter):
    return sorted(aktiviteter, key=lambda a: a["date"])

def sorter_på_varighet (aktiviteter):
    return sorted(aktiviteter, key=lambda a: a["estimated_minutes"], reverse=True)


def vis_statistikk(aktiviteter):
    antall_totalt = len(aktiviteter)
    sum_minutter = 0
    antall_fullført = 0

    for aktivitet in aktiviteter:
        sum_minutter += aktivitet["estimated_minutes"]
        if aktivitet["status"] == "completed":
            antall_fullført += 1

    print (f"antall aktiviteter: {antall_totalt}")
    print(f"samlet estimert tid: {sum_minutter} min")
    print(f"antall fullført: {antall_fullført}")








