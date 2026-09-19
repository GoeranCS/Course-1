# Oppgave 1.2 – Analyser tekst

while True:
    tekst = input("Skriv inn tekst: ")
    if tekst.strip() != "":
        break
    print("Teksten kan ikke være tom eller bare ha mellomrom. Prøv igjen.")

print(f"Tegn med mellomrom: {len(tekst)}")
print(f"Uten mellomrom: {len(tekst.replace(' ', ''))}")
print(f"Små bokstaver: {tekst.lower()}")
print(f"Baklengs: {tekst [ :: -1]}")

if "python" in tekst.lower():
    print("Teksten inneholder ordet python")

else:
    print("Teksten inneholder ikke ordet python")
