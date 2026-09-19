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

