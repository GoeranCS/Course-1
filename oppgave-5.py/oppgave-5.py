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

