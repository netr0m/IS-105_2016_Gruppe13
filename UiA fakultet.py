import math
import pprint

HoI = 3249
HoITekst = "Helse- og idrettsfag"
HoP = 2707
HoPTekst = "Humaniora og pedagogikk"
KF = 713
KFTekst = "Kunstfag"
ToR = 3503
ToRTekst = "Teknologi og realfag"
LU = 2664
LUTekst = "Lererutdanningen"
OoS = 5491
OoSTekst = "Okonomi og samfunnsvitenskap"

HoIPoss = format(round(math.log2(HoI/1)))
HoPPoss = format(round(math.log2(HoP/1)))
KFPoss = format(round(math.log2(KF/1)))
ToRPoss = format(round(math.log2(ToR/1)))
LUPoss = format(round(math.log2(LU/1)))
OoSPoss = format(round(math.log2(OoS/1)))


UiAStudents = []
UiAStudents.append([HoITekst, HoI, HoIPoss])
UiAStudents.append([HoPTekst, HoP, HoPPoss])
UiAStudents.append([KFTekst, KF, KFPoss])
UiAStudents.append([ToRTekst, ToR, ToRPoss])
UiAStudents.append([LUTekst, LU, LUPoss])
UiAStudents.append([OoSTekst, OoS, OoSPoss])

pprint.pprint(UiAStudents)