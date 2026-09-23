# Oppgave 4 – Filer, feilhåndtering og feilsøking
# 4.1 Les og kontroller data
import csv
def les_supporthenvendelser (filnavn):
    gyldige_rader = []

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

            if int(id_tekst) < 0:
               print(f"rad {radnummer}: id må være positivt")
               continue

            if not minutter_tekst.isdigit():
               print(f"rad {radnummer}: minutes er ikke er gyldig heltall")
               continue

            if status != "yes" and status != "no":
               print(f"rad {radnummer}: is_resolved må være yes eller no")
               continue

            gyldige_rader.append({"id": int(id_tekst),
                 "category": kategori,
                 "minutes": int(minutter_tekst),
                 "is_resolved": status,
            })
    return gyldige_rader

rader = les_supporthenvendelser("supporthenvendelser.csv")
print(f"{len(rader)} gyldige rader")




# Oppgave 4.2
# Analyser data


