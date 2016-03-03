#Kilde: http://matplotlib.org/examples/api/barchart_demo.html
# -*- coding: utf-8 -*-
# Import setninger for modulene math og pprint
# Math for regneoppgaver
import math
# Pprint for å printe setninger på hver sin linje
import pprint
# Numpy og matplotlib for å lage fremvise graf
import numpy as np
import matplotlib.pyplot as plt

# Definer verdiene (antall studenter) for hvert fakultet
# Definer navn på fakultet
HoI = 1829.
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
UiAStudents.append([HoITekst, HoI, HoIPoss+"%"])
UiAStudents.append([HoPTekst, HoP, HoPPoss+"%"])
UiAStudents.append([KFTekst, KF, KFPoss+"%"])
UiAStudents.append([ToRTekst, ToR, ToRPoss+"%"])
UiAStudents.append([LUTekst, LU, LUPoss+"%"])
UiAStudents.append([OoSTekst, OoS, OoSPoss+"%"])

print ("Navn paa fakultet, antall studenter, sannsynlighet")
# Pprint modul for å printe ut verdiene
pprint.pprint(UiAStudents)

print ("\nVi faar minst informasjon fra fakultetet for " + OoSTekst + ". Dette fordi det er " + OoSPoss + "% sannsynlighet \nfor at en student tilhoerer dette fakultetet.")


# Lager lister med tall vi har fått tidligere for å opprette en graf
students = (HoI, HoP, KF, ToR, LU, OoS)
probability = (HoIPoss, HoPPoss, KFPoss, ToRPoss, LUPoss, OoSPoss)
faculties = ('HoI', 'HoP', 'KF', 'ToR', 'LU', 'OoS')

ind = np.arange(len(faculties))  # Plasseringen for grafene
width = 0.75       # Bredden på grafene

fig, ax = plt.subplots() # Forteller at vi ønsker å bruke en graf

# Henter plassering fra ind, bredde fra width, verdi på barene fra listene og farge
axStudents = ax.bar(ind, students, width, color='r')
axProbability = ax.bar(ind, probability, width, color='r')

ax.set_title('Faculty, number of students and probability') # Tittel på grafen
ax.set_ylabel('Students') # Navn for y aksen
ax.set_xticks(ind + 0.4) # Plassering på bar-navnene
ax.set_xticklabels(faculties) # Navnet på barene

# Designer hvor og hvordan verdiene skal vises over grafene
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height*100, 
                '%d' % int(height),
                ha='center', va='bottom')

# Verdiene ovenfor grafene vises i prosent, og forteller sannsynligheten for at en gitt student tilhører fakultetet
autolabel(axProbability)

plt.show()
