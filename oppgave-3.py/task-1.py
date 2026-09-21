# Oppgave 3 – Funksjoner og dokumentasjon

from datetime import datetime, timedelta
from typing import cast


def les_dato(tekst):
    """gjør denne teksten dd.mm.åååå om til en dato.

        parameter: tekst (str), f.eks)
    "10.10.2026"
    returner: dato om teksten er gyldig, ellers None
    """
    try:
        return datetime.strptime(tekst, "%d.%m.%Y").date()
    except ValueError:
        return None



def beregn_sluttid(starttid, minutter):
    """legger til minutter til startpunkt)

    parameter: starttid (str, tt:mm),
    ¨minutter (int)
    returner: sluttid som tekst (tt:mm),
    eller None om starttid er ugyldig."""

    try:
        start = datetime.strptime(starttid, "%H:%M")
    except ValueError:
        return None
    slutt = start + timedelta(minutes=minutter)
    return slutt.strftime("%H:%M")



def dager_mellom(dato1, dato2):
    """finn antall dager mellom to datoer)

    parameter: dato1 dato2 (datoer)
    returner: positivt heltall (rekkefølge kan være tilfeldig)"""
    return abs((dato2 - dato1).days)



def sorter_datoer(datoer):
    """sorter datoer med eldste først.

    parameter: datoer (liste med datoer)
    returner: ny liste i kronologisk rekkefølge"""
    return sorted(datoer)


# Hovedprogrammet nedenfor


print("planlegg studiøkter")

# les tre datoer



datoer = []
while len(datoer) < 2:
    tekst = input(f"dato{len(datoer)+1}(dd.mm.åååå): ")
    dato = les_dato(tekst)
    if dato is None:
        print("feil: dato er ugyldig. bruk formatet dd.mm.åååå f.eks.12.06.1997.")
    else:
        datoer.append(dato)


# les varigheten



while True:
    tekst = input("varighet regnet i minutter: ")
    if tekst.isdigit() and int(tekst) > 0:
        minutter = int(tekst)
        break
    print("feil: varighet må være et positivt heltall, f.eks. 50.")



# les starttidspunktet



while True:
    starttid = input("starttidspunkt (tt:mm): ")
    sluttid = beregn_sluttid(starttid, minutter)
    if sluttid is not None:
            break
    print("feil: starttiden er ugyldig. bruk formatet tt:mm, f.eks. 19:25.")



# resultater




print()
print("sluttid:", sluttid)
print("dager mellom dato1 og dato2:",dager_mellom(datoer[0], datoer[1]))
print ("datoene satt i kronologisk rekkefølge")
for dato in sorter_datoer(datoer):
    print("", dato.strftime("%d.%m.%Y"))




