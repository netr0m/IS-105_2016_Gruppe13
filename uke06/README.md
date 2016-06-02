# ICA03 / UKE 6

### Oppgave 1.2.1

#### a)

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


#### b)

**Se filen oppg_1.2.1b.py for koden**


#### c)

Komprimeringsgraden er 45,45%

#### d)

**Se filen oppg_1.2.1d.py for koden**

B C C A C B C C C C C C C C C C C A C C C A

| Tegn | Antall | Sannsynlighet for forekomst: |
| --- | --- | --- |
| A | 3 | 13,64 % |
| B | 2 | 9,09 % |
| C | 17 | 77,27 % |

**Huffman:**

Hvis A = 10, B = 11, C = 0:
Blir det binære tallet: 110010011000000000001000010, som er 27 bits.
Den opprinnelige meldingen var på 176 bits, og ved bruk av Huffman coding har vi oppnådd en komprimeringsgrad på 84,66 %

For hvert tegn I LZW er det 8 bits. Mens i Huffman er det kun 1-2 bits per tegn. Komprimeringsgraden er derfor mer effektiv for den gitte teksten.

#### e)

Se filen 1.2.1e.py for koden, og filene output.txt og output1.txt for resultat.

Vi har kun fått til encoding, og ikke decoding.

output.txt er den komprimerte versjonen av hamlet.txt

output1.txt er den komprimerte versjonen av complete_shakespeare.txt

output2.txt er den komprimerte versjonen av shakespeare.txt

#### f)

| Input | Opprinnelig størrelse | Output | Komprimert størrelse | Komprimeringsgrad |
| --- | --- | --- | --- | --- |
| hamlet.txt | 180 kb | output.txt | 2 kb | 98.88888888888889 % |
| complete_shakespeare.txt | 2080 kb | output1.txt | 49 kb | 97.64423076923077 % |
| shakespeare.txt | 5459 kb | output2.txt | 131 kb | 97.60029309397326 % |

hamlet.txt ble komprimert til 2 kb, altså 98.88 % mindre enn originalfilen (180 kb).

complete_shakespeare.txt ble komprimert til 49 kb, altså 97,64 % mindre enn originalfilen (2080 kb).

shakespeare.txt ble komprimert til 131 kb, altså 97.6 % mindre enn originalfilen (5459 kb).

Ved første forsøk på denne komprimeringen, opplevde vi at komprimeringen tok veldig lang tid, og resultatet ble en "komprimert" fil som var større enn originalfilen. Dette skjedde på grunn av tabellstørrelsen vi hadde brukt (4095), og når denne ble redusert, opplevde vi at komprimeringen gikk raskere og størrelsen på output ble mye mindre enn orignalfilens størrelse.
