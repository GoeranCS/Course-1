
## Gøran Sagvollen
## Tittel: datetime - Basic date and time types

URL: https://docs.python.org/3/library/datetime.html

## Oppgave 3- Funksjoner og dokumentasjon

Laget et program som planlegger studieøkter.
Programmet leser to datoer, en varighet i minutter, og et starttidspunkt fra tastaturet, samt viser sluttid, antall
dager mellom to datoer og datoene i kronologisk rekkefølge.

hele oppgaven ligger i oppgave-3.py

## Kjøre Programmet
1. Åpne oppgave-3.py i PyCharm.
2. Trykk keybind eller play-knapp for å kjøre programmet i terminalen
3. svar på følgende spørsmå.
- To datoer i formatet (dd.mm.åååå)
- Varighet i minutter (positivt heltall)
- Starttidspunkt på formatet (tt:mm)

Om noe er ugyldig, vises en feilmelding og programmet spør på nytt.


## Funksjoner

# Funksjon: 
1. les_dato(tekst) - Tekst på formatet (dd.mm.åååå)
2. beregn_sluttid(starttid, minutter)
3. dager_mellom(dato1, dato2)
4. sorter_datoer(datoer)

#Tar i mot
1. Tekst på formatet (dd.mm.åååå)
2. Starttid som tekst (tt:mm) og minutter (heltall)
3. To datoer
4. Liste med datoer 

#Returnerer
1. En dato eller None om teksten er ugyldig
2. Sluttid som tekst (tt:mm) eller none om starttid er ugyldig
3. Positivt antall dager mellom dem
4. Ny liste sortert kronologisk


## Standarbibliotek og dokumentasjon

Jeg bruker datetime fra Python- standardbiblioteket (datetime, timedelta, strptime og strftime)

### *Tittel: datetime - Basic date and time types

* Nettadresse: https://docs.python.org/3/library/datetime.html

* Om: strptime og strftime og formatkodene (%d, %m, %Y, %H, %M)
URL: https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

### KI bruk: 

* Jeg har brukt Claude til å rette koden min flere ganger, samt fått forklaringer på innryk, docstrings, rekkefølge og oppdeling av koden.
* Dette hjalp Claude med: laget et første utkast som inneholdt 4 funksjoner og datetime etter at jeg promptet en løsning på å lage et program
som inneholdt funksjoner.
* Feilsøking: forklarte hvorfor programmet ga "NameError" (feil inrykk på løkken som leser starttid), hvorfor sluttiden alltid ble med '00:00.' (.date () fjernet klokkeslettet.) og hvorfor 
dager_mellom returnerte en liste (en 'sorted' linje lå i feil funksjon)
* Hvordan sette opp en greit lesbar README.



## Test: gyldig og ugyldig svar:


```
# gyldig dato

planlegg studiøkter
dato1(dd.mm.åååå): 12.10.2009
dato2(dd.mm.åååå): 13.10.2009
varighet regnet i minutter: 50
starttidspunkt (tt:mm): 09:00

sluttid: 09:50
dager mellom dato1 og dato2: 1
datoene satt i kronologisk rekkefølge
 12.10.2009
 13.10.2009

# Ugyldig dato:
planlegg studiøkter
dato1(dd.mm.åååå): 12.12.2009
dato2(dd.mm.åååå): 12.13.2009
feil: dato er ugyldig. bruk formatet dd.mm.åååå f.eks.12.06.1997.
dato2(dd.mm.åååå): 

# Varighet: gyldig

planlegg studiøkter
dato1(dd.mm.åååå): 10.10.2009
dato2(dd.mm.åååå): 11.10.2009
varighet regnet i minutter: 45
starttidspunkt (tt:mm): 12:00
sluttid: 12:45
dager mellom dato1 og dato2: 1
datoene satt i kronologisk rekkefølge
 10.10.2009
 11.10.2009

# Ugyldig

planlegg studiøkter
dato1(dd.mm.åååå): 10.10.2009
dato2(dd.mm.åååå): 11.10.2009
varighet regnet i minutter: -2
feil: varighet må være et positivt heltall, f.eks. 50.
varighet regnet i minutter:


# Starttid: gyldig

planlegg studiøkter
dato1(dd.mm.åååå): 11.11.2009
dato2(dd.mm.åååå): 12.11.2009
varighet regnet i minutter: 40
starttidspunkt (tt:mm): 07:45

sluttid: 08:25
dager mellom dato1 og dato2: 1
datoene satt i kronologisk rekkefølge
 11.11.2009
 12.11.2009

# Resultat: 
Her tester jeg alle feil, og deretter viser riktig input.



planlegg studiøkter
dato1(dd.mm.åååå): 31.02.2026
feil: dato er ugyldig. bruk formatet dd.mm.åååå f.eks.12.06.1997.
dato1(dd.mm.åååå): 2026.12.24
feil: dato er ugyldig. bruk formatet dd.mm.åååå f.eks.12.06.1997.
dato1(dd.mm.åååå): 24.12.2026
dato2(dd.mm.åååå): 01.01.2026
varighet regnet i minutter: 0
feil: varighet må være et positivt heltall, f.eks. 50.
varighet regnet i minutter: -6
feil: varighet må være et positivt heltall, f.eks. 50.
varighet regnet i minutter: abc
feil: varighet må være et positivt heltall, f.eks. 50.
varighet regnet i minutter: 90
starttidspunkt (tt:mm): 25:00
feil: starttiden er ugyldig. bruk formatet tt:mm, f.eks. 19:25.
starttidspunkt (tt:mm): 14:30

sluttid: 16:00
dager mellom dato1 og dato2: 357
datoene satt i kronologisk rekkefølge
 01.01.2026
 24.12.2026
```
