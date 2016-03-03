# -*- coding: utf-8 -*-
# Import setninger for modulene math og pprint
# Math for regneoppgaver
import math
# Pprint for å printe setninger på hver sin linje
import pprint

# Definer verdiene (antall studenter) for hvert fakultet
HoI = 1829.
# Definer navn på fakultet
HoITekst = "Helse- og idrettsfag"
HoP = 1525.
HoPTekst = "Humaniora og pedagogikk"
KF = 420.
KFTekst = "Kunstfag"
ToR = 2166.
ToRTekst = "Teknologi og realfag"
LU = 1506.
LUTekst = "Laererutdanningen"
OoS = 3093.
OoSTekst = "Oekonomi og samfunnsvitenskap"
total = HoI + HoP + KF + ToR + LU + OoS

# Utregning av sannsynlighet for at en student tilhører et gitt fakultet
# {:.2f} begrenser til to desimaler
HoIPoss = "{:.2f}".format(HoI/total * 100)
HoPPoss = "{:.2f}".format(HoP/total * 100)
KFPoss = "{:.2f}".format(KF/total * 100)
ToRPoss = "{:.2f}".format(ToR/total * 100)
LUPoss = "{:.2f}".format(LU/total * 100)
OoSPoss = "{:.2f}".format(OoS/total * 100)


# Liste over fakultet og verdier
UiAStudents = []
UiAStudents.append([HoITekst, HoI, HoIPoss])
UiAStudents.append([HoPTekst, HoP, HoPPoss])
UiAStudents.append([KFTekst, KF, KFPoss])
UiAStudents.append([ToRTekst, ToR, ToRPoss])
UiAStudents.append([LUTekst, LU, LUPoss])
UiAStudents.append([OoSTekst, OoS, OoSPoss])

print ("Navn paa fakultet, antall studenter, sannsynlighet")
# Pprint modul for å printe ut verdiene
pprint.pprint(UiAStudents)

print ("Som vi ser over, er det lavest sannsynlighet for at \nen gitt student tilhoerer fakultetet for " + KFTekst)