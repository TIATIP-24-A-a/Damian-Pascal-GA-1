# Größter gemeinsamer Teiler (ggT)

Der größte gemeinsame Teiler (ggT) ist ein Begriff aus der Mathematik. Er bezeichnet die größte natürliche Zahl, durch die sich zwei ganze Zahlen ohne Rest teilen lassen. Das Pendant dazu ist das kleinste gemeinsame Vielfache (kgV).

## Definition

Der ggT zweier ganzer Zahlen \(a\) und \(b\) ist die größte Zahl \(d\), die sowohl \(a\) als auch \(b\) teilt. Mathematisch ausgedrückt:

- \(d | a\) und \(d | b\)
- Für jede Zahl \(c\), die \(a\) und \(b\) teilt, gilt \(c | d\).

## Berechnungsmethoden

### 1. **Primfaktorzerlegung**
Zur Bestimmung des ggT über die Primfaktorzerlegung:
- Zerlege beide Zahlen in ihre Primfaktoren.
- Wähle die überlappenden Primfaktoren mit dem jeweils kleineren Exponenten.

### 2. **Euklidischer Algorithmus**
Eine effizientere Methode zur Berechnung des ggT ist der euklidische Algorithmus:
- Subtrahiere iterativ die kleinere Zahl von der größeren, bis der Rest null ist.
- Der ggT ist dann die letzte nicht-null Restzahl.

**Beispiel:**
- Zahlen: \(143\) und \(65\)
- Schritte:
  - \(143 - 65 = 78\)
  - \(78 - 65 = 13\)
  - Der ggT ist \(13\).

### 3. **Moderne Variante des Euklidischen Algorithmus**
Statt der Subtraktion verwendet man Division mit Rest:
- Dividende wird durch Divisor geteilt.
- Neuer Divisor ist der vorherige Rest.
- Wiederholen, bis der Rest null ist.

### 4. **Steinscher Algorithmus**
Eine Alternative zum euklidischen Algorithmus, die abhängig von der verwendeten Maschinerie vorteilhaft sein kann:
- Gemeinsame Faktoren von 2 werden zunächst entfernt.
- Rekursives Abziehen der verbleibenden ungeraden Teile.

## Eigenschaften und Rechenregeln

- **Kommutativgesetz:** \(ggT(a, b) = ggT(b, a)\)
- **Assoziativgesetz:** \(ggT(a, ggT(b, c)) = ggT(ggT(a, b), c)\)
- **Distributivgesetz:** \(ggT(a, b + c) = ggT(a, b)\), falls \(a | c\).

### Zusammenhang mit dem kgV
Es gilt die Beziehung:
\[
kgV(a, b) \cdot ggT(a, b) = |a \cdot b|
\]

## Anwendungen

1. **Bruchrechnung:**
   - Zum Kürzen eines Bruchs wird der ggT von Zähler und Nenner verwendet.

2. **Algebraische Strukturen:**
   - Der Begriff ggT lässt sich auf andere Strukturen wie Polynome oder Integritätsringe erweitern.

## Beispiele in der Informatik

### Implementierung in C
Iterativ:
```c
int GreatestCommonDivisor(int a, int b) {
    int h;
    while (b != 0) {
        h = a % b;
        a = b;
        b = h;
    }
    return abs(a);
}
```
Rekursiv:
```c
int GreatestCommonDivisor(int a, int b) {
    if (b == 0) return abs(a);
    return GreatestCommonDivisor(b, a % b);
}
```

## Erweiterte Konzepte

- **Lemma von Bézout:**
  - Der ggT zweier Zahlen \(a\) und \(b\) kann als Linearkombination dargestellt werden:
    \[
    ggT(a, b) = x \cdot a + y \cdot b
    \]
  - Die Koeffizienten \(x\) und \(y\) können mit dem erweiterten euklidischen Algorithmus berechnet werden.

## Sonderfälle

1. \(ggT(a, 0) = |a|\)
2. \(ggT(0, 0)\) ist undefiniert.

## Literatur und Weblinks
- [Wikipedia: Größter gemeinsamer Teiler](https://de.wikipedia.org/wiki/Gr%C3%B6%C3%9Fter_gemeinsamer_Teiler)
- [Euklidischer Algorithmus](https://de.wikipedia.org/wiki/Euklidischer_Algorithmus)

