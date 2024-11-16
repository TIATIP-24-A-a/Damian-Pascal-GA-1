
# Detaillierte Erklärung der Testfälle in `Test_gcd.py`

## Überblick
Dieses Dokument bietet eine detaillierte Aufschlüsselung der Testfälle, die im Skript zur Validierung der Funktionalität des GCD-Rechners geschrieben wurden.

## Testfall-Aufschlüsselung

### 1. `test_calculate_gcd_single_number`
- **Zweck**: Sicherstellen, dass die GCD-Funktion eine einzelne Zahl korrekt verarbeiten kann.
- **Schritte**:
  1. Eingabe einer Liste mit einer einzigen Zahl `[7]`.
  2. Überprüfen, ob die Ausgabe `7` entspricht, da der GCD einer einzelnen Zahl die Zahl selbst ist.
- **Erwartetes Ergebnis**: `7`

### 2. `test_calculate_gcd_multiple_numbers`
- **Zweck**: Überprüfen, ob der GCD für mehrere Zahlen korrekt berechnet wird.
- **Schritte**:
  1. Eingabe einer Liste von Ganzzahlen `[48, 72, 108]`.
  2. Der GCD dieser Zahlen ist `12` (die größte Zahl, die alle drei ohne Rest teilt).
- **Erwartetes Ergebnis**: `12`

### 3. `test_calculate_gcd_prime_numbers`
- **Zweck**: Testen des Randfalls, bei dem die Eingabeliste nur Primzahlen enthält, die keinen gemeinsamen Teiler außer `1` haben.
- **Schritte**:
  1. Eingabe einer Liste von Primzahlen `[13, 17, 19]`.
  2. Da es keinen gemeinsamen Teiler außer `1` gibt, sollte der GCD `1` sein.
- **Erwartetes Ergebnis**: `1`

### 4. `test_calculate_gcd_empty_list`
- **Zweck**: Überprüfen, ob die Funktion eine leere Liste korrekt verarbeitet, indem sie eine `ValueError`-Ausnahme auslöst.
- **Schritte**:
  1. Eingabe einer leeren Liste `[]`.
  2. Erwartung, dass die Funktion eine `ValueError`-Ausnahme mit einer entsprechenden Fehlermeldung auslöst.
- **Erwartetes Ergebnis**: Eine `ValueError`-Ausnahme wird ausgelöst.

### 5. `test_validate_input_valid`
- **Zweck**: Sicherstellen, dass gültige Eingabestrings korrekt in Listen von Ganzzahlen umgewandelt werden.
- **Schritte**:
  1. Eingabe eines gültigen Strings `"48 72 108"`.
  2. Überprüfen, ob die Funktion die entsprechende Liste `[48, 72, 108]` zurückgibt.
- **Erwartetes Ergebnis**: `[48, 72, 108]`

### 6. `test_validate_input_invalid`
- **Zweck**: Sicherstellen, dass die Funktion einen Fehler auslöst, wenn der Eingabestring nicht-ganzzahlige Werte enthält.
- **Schritte**:
  1. Eingabe eines Strings `"48 abc 108"`, der ungültige Zeichen enthält.
  2. Erwartung, dass die Funktion eine `ValueError`-Ausnahme auslöst.
- **Erwartetes Ergebnis**: Eine `ValueError`-Ausnahme wird ausgelöst.

### 7. `test_validate_input_empty`
- **Zweck**: Überprüfen, ob die Funktion einen leeren Eingabestring korrekt verarbeitet.
- **Schritte**:
  1. Eingabe eines leeren Strings `""`.
  2. Erwartung, dass die Funktion eine `ValueError`-Ausnahme auslöst.
- **Erwartetes Ergebnis**: Eine `ValueError`-Ausnahme wird ausgelöst.

## Hinweise
- Diese Tests decken Randfälle, normale Fälle und Szenarien mit ungültigen Eingaben umfassend ab.
- Sie gewährleisten die Robustheit und Zuverlässigkeit der Funktionen `calculate_gcd` und `validate_input`.

---
