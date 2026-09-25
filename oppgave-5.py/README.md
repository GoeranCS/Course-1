
## Gøran Sagvollen
# Oppgave 5 - Miniprosjekt: aktivitetsplanlegger

Dette programmet er ikke ferdig. Jeg har foreløpig bare
laget de delene som bruker det jeg har lært så langt - lese og skrive filer, 
sjekke om noe er skrevet feil (validering), og bruke lister [] og funksjoner.

Det jeg har fått til:
- En funksjon som sjekker om en aktivitet er fylt ut riktig (ikke tomme felt
, at tiden er et postivt tall, og at status er enten "planned" eller "completed")
- å lese aktiviteter fra en fil, og håndtere at filen ikke finnes uten at programmet
krasjer.
- å skrive aktiviteter til en fil.
- å søke etter tittel eller kategori
- å filtrere på status
- å sortere etter dato og etter hvor lang tid noe tar
- å vise litt statistikk (antall, total tid, hvor mange som er fullført)

Oppgaven ber i tillegg om en klasse (Activity) og et menysystem der brukeren kan
skrive inn tall og styre programmet selv mens det kjører. 
Dette har jeg ikke laget ettersom jeg rett og slett ikke har kunnskapen til å gjøre det.


Det betyr at programmet per nå ikke kan kjøres og brukes som et vanlig program- det er bare noen ferdige, testede funksjoner som gjør hver sin jobb.

## Filstruktur

- Oppgave-5.py -  det jeg har skrevet så langt.
- aktiviteter.csv - eksempel på hvordan datafilen ser ut
- README.md - denne filen.


## Eksempel på datafil ( aktiviteter.csv)

```
title, category, date, estimated_minutes, status
trene styrke, trening, 14-02-2026,60,planned
Levere rapport,jobb,06-11-2026,120, completed
```


## Valg jeg har tatt
- lagret hver aktivitet som en dictionary med ( title, category,
date, estimated_minutes og status.)
- jeg bruker csv modulen til å lese og skrive filen, siden det passer godt når hver rad har 
faste felt.
- hvis filen ikke finnes når programmet leser den, 
fanger jeg opp feilen med try/except i stedet for at programmet
krasjer.
- hvis noen skriver bokstaver der det skal være et tall (for estimated_minutes), fanger
jeg det opp på samme måte.

## Testtilfeller (for det jeg har laget så langt)
1. alle felt er fylt ut riktig - godkjennes
2. tittel-feltet er tomt - avvises med beskjed om at felt mangler
3. skriver 'tjue' i stedet for tall - avvises med beskjed om at det ikke er et gyldig tall.
4. skriver -10 som antall minutter - avvises med beskjed om at tallet må være postivt
5. skriver "ferdig" som status i stedet for planned/completed - avvises med riktig beskjed.
6. prøver å lese fra en fil som ikke finnes - programmet gir beskjed i stedet for å krasje
7. sorterer en liste med flere aktiviteter etter varighet - den med lengst
tid havner øverst


## Mangler og ting som kan bli bedre

- programmet kan ikke brukes som et vanlig program ennå siden
menyen og innlesing fra tastatur mangler.
- klassen som oppgaven ber om er ikke laget
- jeg sjekker bare at datofelt ikke er tomt, ikke at det faktisk er en gyldig 
dato
- søket skiller mellom store og små bokstaver, så man må skrive riktig for å få treff
- jeg har skrevet norsk og engelsk om hverandre på noen steder, dette rpøver jeg å få fikset til å 
kun være engelsk.



## Git historikk
```
(.venv) PS C:\_GitHub\GA\Course-1> git log --oneline
438ef04 (HEAD -> master) #7 fikset bug i sorter_på_varighet
c701f6a #6 legg til statistikkvisning
6439f65 #5 lagt til sortering på varighet
e4d0649 #5 lagt til sortering på dato
07f95b3 #5 lagt til sortering på dato
595360e #4 lagt til søk og filtrering på status
ddd873e #4 lagt til søk og filtrering på status
b235cf1 #3 implementerer lagring og lesing av aktiviteter fra fil
0b36c23 #2 implementer lagring og lesing av aktiviteter fra fil
6451a68 #1 sette opp grunnstruktur og imports
```