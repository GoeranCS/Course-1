# Oppgave 4 – Filer, feilhåndtering og feilsøking
# 4.1 Les og kontroller data
import csv
def les_supporthenvendelser (filnavn):
    gyldige_rader = []
    try:
        with open (filnavn, mode='r', encoding='utf-8') as csv_file:
            leser = csv.DictReader(csv_file)
            radnummer =  1

            for rad in leser:
                radnummer += 1


                id_tekst = rad["id"]
                kategori = rad["category"]
                minutter_tekst = rad["minutes"]
                status = rad["is_resolved"]

                if id_tekst == "" or kategori == "" or minutter_tekst == "" or status == "":
                   print(f"rad {radnummer}: mangler et felt")
                   continue

                if not id_tekst.lstrip("-").isdigit():
                   print(f"rad {radnummer}: id er ikke et heltall")
                   continue

                try:
                    id_verdi = int(id_tekst)
                except ValueError:
                    print(f"rad {radnummer}: id er ikke et heltall")
                    continue
                if id_verdi <0:
                    print(f"rad {radnummer}: id må være postivt")
                    continue

                try:
                    minutter_verdi =int(minutter_tekst)
                except ValueError:
                    print(f"rad {radnummer}: minutes er ikke et gyldig heltall")
                    continue

                if status != "yes" and status != "no":
                   print(f"rad {radnummer}: is_resolved må være yes eller no")
                   continue

                gyldige_rader.append({"id": id_verdi,
                     "category": kategori,
                     "minutes": minutter_verdi,
                     "is_resolved": status,
                })
    except FileNotFoundError:
        print(f"fant ikke filen: {filnavn}")
    return gyldige_rader

rader = les_supporthenvendelser("supporthenvendelser.csv")
print(f"{len(rader)} gyldige rader")




# Oppgave 4.2 Analyser data

def analyser_data(gyldige_rader):
    antall_totalt = len(gyldige_rader)

    antall_per_kategori ={}
    for rad in gyldige_rader:
        kategori = rad["category"]
        if kategori not in antall_per_kategori:
            antall_per_kategori [kategori] = 0
        antall_per_kategori[kategori] += 1

    sum_minutter = 0
    for rad in gyldige_rader:
        sum_minutter += rad["minutes"]

    if antall_totalt > 0:
       snitt_minutter = round(sum_minutter / antall_totalt, 1)
    else:
        snitt_minutter = 0

    antall_lost = 0
    antall_ulost = 0
    for rad in gyldige_rader:
        if rad["is_resolved"] == "yes":
            antall_lost += 1
        else:
             antall_ulost += 1

    mest_kategori = None
    mest_antall = 0
    for kategori in antall_per_kategori:
        if antall_per_kategori[kategori] > mest_antall:
           mest_antall = antall_per_kategori[kategori]
           mest_kategori = kategori

    ulost_liste =[]
    for rad in gyldige_rader:
        if rad ["is_resolved"] == "no":
           ulost_liste.append(rad)

    ulost_sortert = sorted(ulost_liste, key=lambda x: x["minutes"], reverse=True)

    return {
         "antall_totalt": antall_totalt,
         "antall_per_kategori": antall_per_kategori,
         "sum_minutter": sum_minutter,
         "snitt_minutter": snitt_minutter,
         "antall_lost": antall_lost,
         "antall_ulost": antall_ulost,
         "mest_kategori": mest_kategori,
         "ulost_sortert": ulost_sortert,
    }
analyse = analyser_data(rader)
print(analyse)

# Oppgave 4.3 Skriv rapport

def skriv_rapport(analyse, filnavn):
    kategori_tekst = ""
    for kategori in  analyse["antall_per_kategori"]:
        antall = analyse["antall_per_kategori"][kategori]
        linje =f" {kategori}: {antall}\n"
        kategori_tekst +=linje

    ulost_tekst = ""
    for rad in analyse["ulost_sortert"]:
        id_verdi = rad["id"]
        kategori_verdi = rad["category"]
        minutter_verdi = rad["minutes"]
        linje = f" id {id_verdi} - {kategori_verdi} -- {minutter_verdi} min\n"
        ulost_tekst +=linje

    totalt = analyse["antall_totalt"]
    sum_min = analyse["sum_minutter"]
    snitt_min = analyse["snitt_minutter"]
    antall_lost = analyse["antall_lost"]
    antall_ulost = analyse["antall_ulost"]
    mest_kategori = analyse["mest_kategori"]

    rapport = "SUPPORT-RAPPORT\n"
    rapport += "=================\n\n"
    rapport += f"antall gyldige henvendelser: {totalt}\n\n"
    rapport += "antall per kategori:\n"
    rapport +=  kategori_tekst
    rapport += "\n"
    rapport += f"sum minutter brukt: {sum_min}\n"
    rapport += f"snitt minutter per henvendelser: {snitt_min}\n\n"
    rapport += f"loste henvendelser: {antall_lost}\n"
    rapport += f"ulost henvendelser: {antall_ulost}\n"
    rapport += f"kategori med flest henvendelser: {mest_kategori}\n"
    rapport += f"uloste henvendelser sortert (mest tidkrevende først):\n"
    rapport += ulost_tekst

    with open(filnavn, mode='w', encoding="utf-8") as file: file.write(rapport)

skriv_rapport(analyse, "support-rapport.txt")


# Oppgave 4.4 Finn og rett feil

def sum_resolved_minutes(requests):
    total = 0
    for request in requests:
        if request["is_resolved"] == "yes":
            total += request["minutes"]
    return total

print(sum_resolved_minutes(rader))

