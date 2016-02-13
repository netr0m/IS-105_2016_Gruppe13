# ICA03 UKE 6

**Oppgave 1.2.1**
```sh
a)
```

| **Input** | **Output Sequence** | **New dictionary entry** |
| --------- | --------------------| ------------------------ |
| **Code**  |                     | **Full** / **Conjecture**|
| 2 | B | NULL / 4: B? |
| 3 | C | 4: BC / 5: C? |
| 3 | C | 5: CC / 6: C? |
| 1 | A | 6: CA / 7: A? |
| 3 | C | 7: AC / 8: C? |
| 4 | BC | 8: CB / 9: B? |
| 5 | CC | 9: BCC / 10: CC? |
| 10 | CCC | 10: CCC / 11: CCC? |
| 11 | CCCC | 11: CCCC /
| 6 | CA |
| 10 | CCC |
| 1 | A |

Den ferdige koden blir da: B C C A C BC CC CCC CCCC CA CCC A

Hvis vi går ut fra at hvert symbol består av 8 bits, blir det da 8 * 22 bits som er 176 bits.

Format for tabell hentet fra: https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Welch

```sh
b)
```
Vi forstår ikke denne oppgaven, og har derfor ikke gjort den.

```sh
c)
```
Komprimeringsgraden er 45,45%

```sh
d)
```
**Se filen oppg_1.2.1d.py for koden**

B C C A C B C C C C C C C C C C C A C C C A

| Tegn | Antall | Sannsynlighet for forekomst: |
| --- | --- | --- |
| A | 3 | 13,64 % |
| B | 2 | 9,09 % |
| C | 17 | 77,27 % |

**Huffman:**

C: 1 bit * 17 = 17
B: 3 bits * 2 = 6
A: 2 bits * 3 = 6
Totalt: 29 bits

110010011000000000001000010

Kompringmeringsgraden er: 83,52 %

For hvert tegn I LZW er det 8 bits. Mens i Huffman er det kun 1-2 bits per tegn. Komprimeringsgraden er derfor mer effektiv for den gitte teksten.

```sh
e) og f)
```
Vi får ikke til disse oppgavene.
