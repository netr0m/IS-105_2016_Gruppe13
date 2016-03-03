# ICA 02 / UKE 5
Våre besvarelser for ICA 02
```sh
a)
```
Se filene UiA Fakultet.pdf og oppg_1.2.1.py for vår besvarelse.

```sh
b)
```
Man får minst informasjon fra fakultetet for Økonomi og Samfunnsfag.
Dette fordi det er 29,3% sannsynlighet for at en gitt student tilhører dette fakultetet.
Se også filen oppg_1.2.1.py for besvarelse.

```sh
c)
```
Se filen 1.2.1c.png for vårt Huffman Tre.

| **Fakultet** | **Kode** | **Kodelengde** |
| --- | --- | --- |
| Økonomi og samfunnsvitenskap | 00 | 2 bits |
| Teknologi og realfag | 01 | 2 bits |
| Helse- og idrettsfag | 100 | 3 bits |
| Humaniora og pedagogikk | 101 | 3 bits |
| Lærerutdanningen | 110 | 3 bits |
| Kunstfag | 111 | 3 bits |

```sh
d)
```
| | **Helse- og idrettsfag** | **Humaniora og pedagogikk** | **Kunstfag** | **Teknologi og realfag** | **Lærerutdanningen** | **Økonomi og samfunnsvitenskap** |
| --- | --- | --- | --- | --- | --- | --- |
| Antall studenter per fakultet | 1829 | 1525 | 420 | 2166 | 1506 | 3093 |
| Sannsynlighet | 0.17 | 0.15 | 0.04 | 0.21 | 0.14 | 0.29 |
| Bits | 3 | 3 | 3 | 2 | 3 | 2 |
| Bits * Sannsynlighet | | 0.51 | 0.45 | 0.12 | 0.42 | 0.42 | 0.58 |
| Bits pr. fakultet når 100 tilfeldige studenter er valgt | 51 | 45 | 12 | 42 | 42 | 58 |

Gjennomsnittlengden for en melding blir derfor 250 bits for 100 studenter, altså 2,5 bits pr. student.

##### Entropi:
0.29*log2(1/0.29) = 0.5179038064476742
0.21*log2(1/0.21) = 0.4728231410691526
0.17*log2(1/0.17) = 0.4345868692491456
0.15*log2(1/0.15) = 0.4105448391249309
0.14*log2(1/0.14) = 0.3971101774803969
0.04*log2(1/0.04) = 0.185754247590989

Svaret her blir 242 bits, som blir delt på 100, altså 2.42 bits per student.
Gjennom å regne ut ved bruk av entropi har vi oppnådd noen bits (18, for å være nøyaktig) mindre enn det vi gjorde ved bruk av Huffman-metoden.
Grunnen til dette er at sistnevnte metode ikke er optimal når det gjelder komprimering. 

```sh
e)
```
Se filen 1.2.1e.py
