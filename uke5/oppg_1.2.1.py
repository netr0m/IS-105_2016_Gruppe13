# -*- coding: utf-8 -*-
# Import setninger for modulene math og pprint
# Math for regneoppgaver
import math
# Pprint for å printe setninger på hver sin linje
import pprint

# Definer verdiene (antall studenter) for hvert fakultet
HoI = 1829
# Definer navn på fakultet
HoITekst = "Helse- og idrettsfag"
HoP = 1525
HoPTekst = "Humaniora og pedagogikk"
KF = 420
KFTekst = "Kunstfag"
ToR = 2166
ToRTekst = "Teknologi og realfag"
LU = 1506
LUTekst = "Laererutdanningen"
OoS = 3093
OoSTekst = "Oekonomi og samfunnsvitenskap"

# Utregning
HoIPoss = format(round(math.log(HoI/1)))
HoPPoss = format(round(math.log(HoP/1)))
KFPoss = format(round(math.log(KF/1)))
ToRPoss = format(round(math.log(ToR/1)))
LUPoss = format(round(math.log(LU/1)))
OoSPoss = format(round(math.log(OoS/1)))

# Liste over fakultet og verdier
UiAStudents = []
UiAStudents.append([HoITekst, HoI, HoIPoss])
UiAStudents.append([HoPTekst, HoP, HoPPoss])
UiAStudents.append([KFTekst, KF, KFPoss])
UiAStudents.append([ToRTekst, ToR, ToRPoss])
UiAStudents.append([LUTekst, LU, LUPoss])
UiAStudents.append([OoSTekst, OoS, OoSPoss])

# Pprint modul for å printe ut verdiene
pprint.pprint(UiAStudents)