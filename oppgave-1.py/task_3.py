#Oppgave 1.3 – Analyser et tallintervall

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

