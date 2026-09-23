# Oppgave 1.1 – Beregn tidsbruk

while True:
    svar = input("Antall studieøkter: ")
    if svar.isdigit() and int(svar) > 0:
        antall = int(svar)
        break
    print("Ugyldig input. Skriv et positivt heltall.")

while True:
    svar = input("Minutter per økt: ")
    if svar.isdigit() and int(svar) > 0:
        minutter_per_økt = int(svar)
        break
    print("Ugyldig input. Skriv et positivt heltall.")

totalt = antall * minutter_per_økt
timer = totalt // 60
minutter = totalt % 60

print (f"Samlet tidsbruk: {timer} timer og {minutter} minutter")

# Oppgave 1.2


while True:
    tekst = input("Skriv inn tekst: ")
    if tekst.strip() != "":
        break
    print("Teksten kan ikke være tom eller bare ha mellomrom. Prøv igjen.")

print(f"Tegn med mellomrom: {len(tekst)}")
print(f"Uten mellomrom: {len(tekst.replace(' ', ''))}")
print(f"Små bokstaver: {tekst.lower()}")
print(f"Baklengs: {tekst [::-1]}")

if "python" in tekst.lower():
    print("Teksten inneholder ordet python")

else:
    print("Teksten inneholder ikke ordet python")


# Oppgave 1.3


while True:
    try:
        start = int(input("startverdi: "))
        slutt = int(input("sluttverdi: "))
    except ValueError:
        print("begge verdiene må være heltall. prøv igjen.")
        continue
    if start > slutt:
        print("startverdi kan ikke være større enn sluttverdi. prøv igjen.")
        continue
    break

partall = []
delelige_med_3 = []
summen = 0

for tall in range (start, slutt + 1):
    if tall % 2 == 0:
        partall.append(tall)
    if tall % 3 == 0:
        delelige_med_3.append(tall)
    summen += tall

print (f"partall: {partall}")
print (f"delelige_med_3: {delelige_med_3}")
print (f"summen: {summen}")


# Oppgave 1.4


while True:
    print("\n1. beregn tidsbruk")
    print ("2. analyser tekst")
    print ("3. analyser tallintervall")
    print ("4. avslutt")

    # fra linje 9-28 har jeg kopiert hele oppgave 1.1 rett inn
    valg = input("velg: ")
    if valg == "1":
        while True:
            svar = input("Antall studieøkter: ")
            if svar.isdigit() and int(svar) > 0:
                antall = int(svar)
                break
            print("Ugyldig input. Skriv et positivt heltall.")

        while True:
            svar = input("Minutter per økt: ")
            if svar.isdigit() and int(svar) > 0:
                minutter_per_økt = int(svar)
                break
            print("Ugyldig input. Skriv et positivt heltall.")

        totalt = antall * minutter_per_økt
        timer = totalt // 60
        minutter = totalt % 60
        print(f"Samlet tidsbruk: {timer} timer og {minutter} minutter")

    #etter linje 31 er hele oppgave 2 copy/pasted
    elif valg == "2":
        while True:
            tekst = input("Skriv inn tekst: ")
            if tekst.strip() != "":
                break
            print("Teksten kan ikke være tom eller bare ha mellomrom. Prøv igjen.")

        print(f"Tegn med mellomrom: {len(tekst)}")
        print(f"Uten mellomrom: {len(tekst.replace(' ', ''))}")
        print(f"Små bokstaver: {tekst.lower()}")
        print(f"Baklengs: {tekst[::-1]}")

        if "python" in tekst.lower():
            print("Teksten inneholder ordet python")

        else:
            print("Teksten inneholder ikke ordet python")

    # etter linje 51 er hele oppgave 3 copypasted
    elif valg == "3":
        while True:
            try:
                start = int(input("startverdi: "))
                slutt = int(input("sluttverdi: "))
            except ValueError:
                print("begge verdiene må være heltall. prøv igjen.")
                continue
            if start > slutt:
                print("startverdi kan ikke være større enn sluttverdi. prøv igjen.")
                continue
            break

        partall = []
        delelige_med_3 = []
        summen = 0

        for tall in range(start, slutt + 1):
            if tall % 2 == 0:
                partall.append(tall)
            if tall % 3 == 0:
                delelige_med_3.append(tall)
            summen += tall

        print(f"partall: {partall}")
        print(f"delelige_med_3: {delelige_med_3}")
        print(f"summen: {summen}")

    elif valg == "4":
        print("avslutter.")
        break
    else:
        print("ugyldig valg. skriv 1, 2, 3, eller 4.")


