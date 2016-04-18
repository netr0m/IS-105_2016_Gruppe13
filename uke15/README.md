# ICA 09/ UKE 15
####Besvarelsen vår er filene "server.py" og "client.py"

For å bruke programmet, må du først kjøre server.py i WingIDE, og deretter kjøre client.py i CMD (Kan også gjøres motsatt, eller kjøre begge i CMD).

Begge filene må kjøres samtidig for at det skal fungere.
Deretter kan du skrive følge instruksjonene på skjermen i programmet "client.py", og se beskjedene komme opp på "server.py".
Man trenger kun en instans av "server.py", men flere brukere/PCer kan kjøre client.py samtidig.

I vår løsning har vi ikke implementert den grafiske utgaven av vårt spill fra ICA08/uke14, men heller valgt å kjøre alt i form av tekstbasert visning. Server holder hele tiden "staten" til verdenen, så hvis en spiller har flyttet kyllingen, vil dette vises om en annen bruker kobler seg til på et senere tidspunkt (så lenge server ikke har blitt restartet). Når det gjelder funksjonen med at kun én node skal kunne endre tilstanden av gangen, har vi ikke klart å implementere dette. Dette grunnet at vi prioriterte grunnleggende funksjonalitet, som f.eks. å gi beskjed om at brukeren har vunnet/tapt, og deretter restarte verden, osv. Da dette tok en del lengre tid enn forventet, rakk vi dessverre ikke å implementere en slik funksjonalitet (kun én node av gangen).

Med tanke på problemstillinger i forhold til synkronisering, kan vi se problemer med at hvis node1 flytter et objekt, og node2 prøver å flytte det samme objektet samtidig/kort tid etter, vil ikke node2's handling gi noen respons.
For å ta hensyn til dette problemet, har vi lagt inn en funksjon på klientens side hvor noden kan sjekke hvilken "state" verden er i.
I denne versjonen av programmet, hvis da node1 flytter et objekt, og node2 prøver å flytte det samme objektet, vil node2's (den siste som utførte handlingen) få sin forespørsel avvist.

**Gruppemedlemmer:**
Morten Amundsen, Nora Krogh, Erlend Sætre, Marius Fosseli, Joakim Kilen
