# ICA06 UKE 9
## Gruppe 13:
Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen

**Oppgave 1.2.1**
```sh
a)
```
###### 1 = True, 0 = False
#### NOT Gate
0 er ikke 1
1 er ikke 0

|   |   |
| --- | --- |
| 0 | 1 |
| 1 | 0 |

#### AND Gate
Hvis A og B er True, blir output True

| **Input 1** | **Input 2** | **Output** |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 1 |

#### OR Gate
Hvis A eller B input er True, blir output True

| **Input 1** | **Input 2** | **Output** |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 1 |

#### XOR Gate
Kun én input kan være True for at output blir True

| **Input 1** | **Input 2** | **Output** |
| --- | --- | --- |
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

#### NOR Gate
Hvis A og B er False, blir output True

| **Input 1** | **Input 2** | **Output** |
| --- | --- | --- |
| 0 | 0 | 1 |
| 0 | 1 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |

```sh
b)
```
#### Turing machine
| **Tilstand** | **Symbol** | **Skriver** | **Operasjon** | **Resultat** |
| --- | --- | --- | --- | --- |
| Tilstand 0 | Blank | Blank | Flytt tape til høyre | 111B |
| Tilstand 1 | 1 | 0 | Flytt tape til høyre | 110B |
| Tilstand 1 | 1 | 0 | Flytt tape til høyre | 100B |
| Tilstand 1 | 1 | 0 | Flytt tape til høyre | 000B |
| Tilstand 1 | Blank | 1 | Flytt tape til venstre | 1000B |
| Tilstand 2 | 0 | 0 | Flytt tape til venstre | 1000B |
| Tilstand 2 | 0 | 0 | Flytt tape til venstre | 1000B |
| Tilstand 2 | 0 | 0 | Flytt tape til venstre | 1000B |
| Tilstand 2 | Blank | Blank | Stop Tilstand | 1000B |

Når prosessen når "Stop Tilstand", står det 1000B på "tape".

For å komme til "Stop Tilstand" kreves det totalt 9 operasjoner.

```sh
c)
```
#### "Elve-krysningsproblemet"
En kort oppsummering av steg som kreves for å komme over elven:
```
1. Frakt kyllingen over til den høyre siden av elven.
2. Sett av kyllingen, og dra tilbake til venstresiden.
3. Ta med kornet, eller reven, over til høyresiden.
4. Sett av kornet/reven, og ta med kyllingen tilbake til venstresiden.
5. Sett av kyllingen, og ta med reven, eller kornet, over til høyresiden.
6. Sett av reven/kornet, og dra tilbake til venstresiden.
7. Ta med kyllingen over til høyresiden.
```

Forskjellen mellom prosessen beskrevet i avsnitt 4.1.3 og i videoen, er at løsningen som ble brukt i videoen har angitt "states" på forhånd, og beskriver hvordan omgivelsene fungerer. I 4.1.3 eksemplet blir handlingene beskrevet som en kombinasjon av kontroll på systemet og området den kontrollerer.
