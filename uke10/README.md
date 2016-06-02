# ICA 07/ UKE 10
####Hovedbesvarelsen vår er filene ICA07_Versjon1.py og ICA07_Versjon2.py.
**ICA07_Versjon1 er vår løsning på oppgaven, som er en samling av de ulike metodene vi har kodet for et filsystem.**
Disse metodene ligger også enkeltvis i sine egne filer i mappa "metoder"

**ICA07_Versjon2 er en kode vi har hentet fra nettet, og deretter lagt inn beskrivelser av hva koden gjør selv.**

##### Om filsystemet brukt i ICA07_Versjon2:
Typen av filsystem brukt her er *FAT*

Ettersom dette er et virtuelt filsystem, og ikke på en fysisk disk/enhet, er det i teorien ikke
begrenset med plass i systemet. I et vanlig filsystem på en fysisk enhet, ville sletting av en fil resultere
i at operativsystemet ikke lenger holder oversikt over hvor på "kartet" filen ligger lagret, og filen vil deretter
over tid bli overskrevet med nye data.

I vårt virtuelle filsystem, når man sletter en fil, kan vi se på koden for å forstå hva som skjer:

`def remove(self, name):
        self.list.remove(self.get(name))`
        
Her ser vi at metoden `remove` fjerner oppføringen av den gitte filen (name) fra listen, og denne filen dermed ikke lenger "eksisterer". Vi ser her at dette har en stor likhet med forklaringen ovenfor, om et "vanlig" filsystem, hvor oppføringen ikke lenger ligger i lista, og filen dermed anses som "slettet"/"fjernet".

**Gruppemedlemmer:**
Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen
