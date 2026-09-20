# Oppgave 2 – Datastrukturer og behandling av data

økter = [
    {"topic": "python variabler",
"duration_minutes": 45, "status":
"completed"},
    {"topic": "python løkker",
"duration_minutes": 60, "status":
"completed"},
    {"topic": "git og github",
"duration_minutes": 30, "status":
"planned"},
    {"topic": "dictionaries",
"duration_minutes": 50, "status":
"completed"},
    {"topic": "funksjoner",
"duration_minutes": 40, "status":
"planned"},
]

def vis (liste):
    if len(liste) ==0:
        print("ingen studieøkter funnet")
    for økt in liste:
        print(f"{økt['topic']} -  {økt['duration_minutes']} min - {økt['status']}")

def hent_varighet (økt):
    return økt["duration_minutes"]

while True:
    print("\n1. registrere en studieøkt")
    print("2. vise alle studieøkter")
    print("3. vis kun fullførte studieøkter")
    print("4. søk etter et ord i temaet")
    print("5. sorter etter varighet, lengst først")
    print("6. vis samlet og gjennomsnittelig varighet")
    print("7. avslutte programmet")

    valg = input ("velg: ")

    if valg == "1":
        tema = input ("tema: ").strip()
        if tema == "":
            print("tema kan ikke være tomt.")
            continue

        varighet = input ("varighet i minutter: ")
        if not (varighet.isdigit()and int(varighet) > 0):
            print("varighet må være et postivt heltall")
            continue

        status = input ("status(status/completed): ").strip().lower()
        if status != "planned" and status != "completed":
            print("status må være planned eller completed.")
            continue


        økter.append({"topic": "tema", "duration_minutes": int(varighet), "status": "status"})
        print("studieøkt registrert.")

    elif valg == "2":
         vis(økter)

    elif valg == "3":
         fullførte = []
         for økt in økter:
             if økt["status"] == "completed":
                 fullførte.append(økt)
         vis (fullførte)

    elif valg == "4":
         ord = input ("søk etter ord: ").strip().lower()
         if ord == "":
             print("søkeordet kan ikke være tomt.")
             continue

         treff =[]
         for treff in økter:
             if ord in økt["topic"].lower():
                 treff.append(økt)
         vis (treff)

    elif valg == "5":
         vis(sorted(økter, key=hent_varighet, reverse=True))

    elif valg == "6":
        total = 0
        antall = 0
        for økt in økter:
            if økt["status"] == "completed":
                total += økt["duration_minutes"]
                antall += 1

        if antall == 0:
            print("ingen fullførte studieøkter ennå")

        else:
            print(f"samlet varighet: {total} minutter")
            print (f"gjennomsnitt: {total / antall:.1f} minutter")

    elif valg == "7":
        print("avslutter.")
        break

    else:
        print ("ugyldig valg. skriv et tall fra 1 til 7.")






