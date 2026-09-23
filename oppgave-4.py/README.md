












## Oppgave 4.4 - Feilretninger i sum_resolved_minutes

1. if request ["is_request"] = "yes": 
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
