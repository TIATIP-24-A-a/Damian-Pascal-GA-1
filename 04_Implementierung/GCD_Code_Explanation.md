
# Erklärung des GCD-Berechnungsprogramms

Das folgende Python-Skript berechnet den **größten gemeinsamen Teiler (GGT)** einer Liste von Zahlen.

---

## **1. Importierte Module**
```python
from math import gcd
from functools import reduce
```
- **`gcd`**: Funktion aus dem Modul `math`, berechnet den GGT von zwei Zahlen.
- **`reduce`**: Aus dem Modul `functools`, um eine Funktion sukzessive auf eine Liste anzuwenden.

---

## **2. Funktion `calculate_gcd(numbers)`**
Diese Funktion berechnet den GGT einer Liste von Zahlen.

### **Signatur**
```python
def calculate_gcd(numbers):
```
### **Beschreibung**
- **Parameter:** `numbers` ist eine Liste von Ganzzahlen.
- **Rückgabe:** Der GGT der Liste.

### **Details**
#### Fehlerbehandlung:
```python
if len(numbers) == 0:
    raise ValueError('Numbers cannot be empty.')
```
- Leere Listen werden mit einem `ValueError` abgefangen.

#### Konvertierung und Validierung:
```python
try:
    numbers = map(int, numbers)
except ValueError:
    raise ValueError("Alle Eingaben muessen Ganzzahlen sein!.")
```
- Jedes Element wird in eine Ganzzahl konvertiert. Ungültige Werte lösen einen Fehler aus.

#### Berechnung des GGTs:
```python
return reduce(gcd, numbers)
```
- `reduce` wendet die `gcd`-Funktion sukzessive auf Paare in der Liste an.

---

## **3. Funktion `parse_input(input_string)`**
### **Signatur**
```python
def parse_input(input_string):
```
### **Beschreibung**
- Konvertiert die Eingabe (String) in eine Liste von Ganzzahlen.
- **Validierung:**
  - Prüft, ob die Eingabe leer ist.
  - Wandelt den String in Ganzzahlen um.
```python
if not input_string:
    raise ValueError("Eingabe darf nicht leer sein.")
```
- Fehlerhafte Eingaben lösen einen `ValueError` aus.

---

## **4. Hauptprogramm (`if __name__ == "__main__":`)**
```python
if __name__ == "__main__":
    try:
        input_string = input("Fügen Sie Ganzzahlen getrennt durch Leerzeichen ein: ").strip()
        numbers = parse_input(input_string)
        result = calculate_gcd(numbers)
        print(f"Der groesste gemeinsame Teiler von {numbers} ist {result}")
    except ValueError as e:
        print(f"Fehler: {e}")
```

### **Details**
1. **Benutzereingabe:**
   - Der Benutzer wird gebeten, Ganzzahlen (durch Leerzeichen getrennt) einzugeben.
   - Die Eingabe wird bereinigt, um führende oder nachfolgende Leerzeichen zu entfernen.

2. **Verarbeitung:**
   - Die Eingabe wird mit `parse_input` validiert.
   - Der GGT wird mit `calculate_gcd` berechnet.

3. **Ausgabe:**
   - Gibt den GGT der Zahlen aus.

4. **Fehlerbehandlung:**
   - Abfangen von Fehlern mit sinnvollen Fehlermeldungen.

---

## **Zusammenfassung**
- Das Skript berechnet den GGT einer Zahlenliste.
- Es validiert die Eingabe und behandelt Fehler wie leere Eingaben oder ungültige Zeichen.

---

