# -*- coding: utf-8 -*-
import math
import pprint

HoI = 1829
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

HoIPoss = format(round(math.log(HoI/1)))
HoPPoss = format(round(math.log(HoP/1)))
KFPoss = format(round(math.log(KF/1)))
ToRPoss = format(round(math.log(ToR/1)))
LUPoss = format(round(math.log(LU/1)))
OoSPoss = format(round(math.log(OoS/1)))


UiAStudents = []
UiAStudents.append([HoITekst, HoI, HoIPoss])
UiAStudents.append([HoPTekst, HoP, HoPPoss])
UiAStudents.append([KFTekst, KF, KFPoss])
UiAStudents.append([ToRTekst, ToR, ToRPoss])
UiAStudents.append([LUTekst, LU, LUPoss])
UiAStudents.append([OoSTekst, OoS, OoSPoss])

pprint.pprint(UiAStudents)