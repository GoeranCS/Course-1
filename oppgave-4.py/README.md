# Oppgave 4 - Filer, feilhåndtering og feilsøking
## Formål

Programmet leser support-henvendelser fra 'supporthenvendelser.csv',
validerer dataen, analyserer de gyldige henvendelsene, og skriver rapport
til 'support-rapport.txt'

## Oppgave 4.1 -Les og kontroller data

Filen leses linje for linje med 'csv.DictReader', med UTF-8-koding og 'with open(...)' slik at filen lukkes automatisk etter bruk.

For hver fil kontrolleres det at:
- alle felt har en verdi
- 'id' er et positivt heltall
- 'minutes' er et heltall større enn eller lik 0
- 'is_resolved' er nøyaktig 'yes' eller 'no'

Rader som ikke oppfyller dette hoppes over.
En feilmelding med radnummer og årsak skrives
til terminalen, og programmet fortsetter med neste rad.

## Oppgave 4.2 Analyser data

 Basert på de gyldige radene beregnes:
- antall gyldige henvendelser totalt, og antall per kategori
- summert og gjennomsnittelig tidsbruk (gjennomsnitt avrundet til 1 desimal)
- antall løste og uløste henvendelser
- kategorien med flest henvendelser
- uløste henvendelser sortert med mest tidkrevende først


## Oppgave 4.3 Skriv rapport

analyseresultatet skrives til 'support-rapport.txt'. Filen opprettes
om den ikke finnes, og overskrives om den finnes fra før (mode="w").
Feilmeldinger om ugyldige rader vises kun i terminalen og er ikke
en del av rapportfilen.

## Feilhåndtering (try/except)
Filfeil håndteres med try/except (FileNotFoundError) rundt hele
fillesingen i les_supporthenvendelser.

Typekonvertering håndteres med egne try/except (ValueError) rundt hver konvertering:
- konvertering av id til heltall (int(id_Tekst))
- konvertering av minutes til heltall (int(minutter_tekst))

Hvis konverteringen feiler, skrives en feilmelding med radnummer til
terminalen, og raden hoppes over med continue.
Ingen tom except er brukt - kun de konkrete feiltypene som 
faktisk kan oppstå.


## Oppgave 4.4 - Feilretninger i sum_resolved_minutes

1. if request ["is_resolved"] = "yes": 
Brukte tilordning (=) i stedet for sammenligning (==). Rettet til "==".

2. total = request ["minutes"] 
Overskrev total i stedet for å legge til.
Rettet til:  total += request ["minutes"]
slik at minuttene summeres i stedet.

3. return total_minutes
Returnerte en variabel som ikke fantes noe sted i funksjonen.
Rettet til: return total 
som er den variabelen som faktisk ble bygget opp.

4. print(sum_resolved_minutes()) 
Kalte funksjonen uten argument, selv om funksjonen
krever en liste med henvendelser. Rettet til:
print(sum_resolved_minutes(rader))


## Bruk av KI (Claude)

Jeg har brukt claude som støtte under arbeidet med denne oppgaven. Konkret ble KI brukt til:
- Foreslå kodestruktur for deloppgavene basert på oppgavetekst.
- Feilsøke og forklare feilmeldinger jeg fikk underveis (innrykksfeil, variabelnavn 
og strukturfeil i try/except-blokker)
- Forklare forskjell på try/except mot annen feilhåndtering f.eks. isdigit()), og hjelpe med å bytte til 
try/except slik oppgaveteksten krevde.

Jeg har selv skrevet koden inn i PyCharm, kjørt og testet den, og rettet feil basert på tilbakemeldinger fra KI-verktøyet.
Jeg har vurdert løsningene som er brukt, men deler av kodeforslaget kom opprinnelig fra KI-samtalen og har blitt tilpasset gjennom flere runder testing, og retting.

