import		math
		from functools import reduce


		def
ggt_von_datei(dateiname):
try:
#Datei öffnen und Zahlen einlesen
with open(dateiname, 'r') as file:
zahlen =[int (line.strip()) for line in file if line.strip().isdigit()]

#Prüfen, ob wir mindestens zwei Zahlen haben
	if len
(zahlen) < 2:
		print("Die Datei muss mindestens zwei Zahlen enthalten.")
			return None

#Berechne den GGT der Zahlen
			ggt = reduce(math.gcd, zahlen)

#Ausgabe des GGT
			print(f "Der größte gemeinsame Teiler der Zahlen in {dateiname} ist: {ggt}")
			return ggt

except FileNotFoundError:
		print(f "Die Datei {dateiname} wurde nicht gefunden.")
except ValueError:
		print("Die Datei enthält ungültige Daten.")
