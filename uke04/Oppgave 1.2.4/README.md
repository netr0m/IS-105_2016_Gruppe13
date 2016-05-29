# 1.2.4 Representasjon av kort i et dataprogram

Filen "deal.py" er vår besvarelse på denne oppgaven.
#### a)
Kort blir representert ved å tildeles en rank (valør) og suit (farge).

Dette kan vi se i koden, på linje 6:

**deck=[ranks+suits for ranks in ['2', '3', (...)] for suits in [' of Spades', ' of Hearts', (...)]])**

#### b)
Denne representasjonen kommer fra en liste som blir generert, *deck*.

#### c)
Deretter brukes random-modulen, som importeres gjennom **import random** og brukes ved **random.shuffle(deck)** på linje 8.

Her shuffles kortstokken (deck) og returneres med et gitt antall kort per hånd (numhands), som er satt til 5.

Til slutt printes lista *deal* til 5 spillere, som vi kan se på linje 12:

**print deal(5)**

#### d)
Unittest-funksjonene kan kjøres via filen "tests_poker.py".
