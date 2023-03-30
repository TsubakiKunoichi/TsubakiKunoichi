import random
import numpy as np

spc = 3 # signed pro case
dpc = 18 # displays pro case
bpd = 12 # booster pro display

#xdpc = 5 # ziehe x displays aus einem case
def anz_displays(xdpc):
    numTests = 10000 # Anzahl an Tests

    signed = list()
    # Teste für x Cases
    for j in range(0, numTests):
        # Anzahl an Signed für aktuellen Pull auf 0 setzen
        signed.append(0)

        # Neues Case mit x Displays generieren
        Case = []
        # Displays ohne Signed hinzufügen
        # 0 = keine Signed
        for i in range(dpc - spc):
            Case.append(0)
        # Displays mit Signed hinzufügen
        # 1 = Signed
        for i in range(spc):
            Case.append(1)
        # Displays im Case mischen
        random.shuffle(Case)

        # Anzahl x aus einem Case ziehen
        for i in range(xdpc):
            signed[j] += Case.pop()

    # ~ gezogene Signed pro Case berechnen
    pspc = sum(signed) / numTests # pulled signed pro case
    keineSigned = list(filter(lambda x: x == 0, signed))
    eineSigned = list(filter(lambda x: x == 1, signed))
    zweiSigned = list(filter(lambda x: x == 2, signed))
    dreiSigned = list(filter(lambda x: x == 3, signed))
    mehrAlsEine  = list(filter(lambda x: x >= 1, signed))

    print("Durchschnittliche Signed Pro Case :", pspc)

    print("Keine Signed pro Case :", len(keineSigned) / numTests)
    print("Eine Signed pro Case :", len(eineSigned) / numTests)
    print("Zwei Signed pro Case :", len(zweiSigned) / numTests)
    print("Drei Signed pro Case :", len(dreiSigned) / numTests)
    alleSigned = []
    alleSigned.extend(keineSigned)
    alleSigned.extend(eineSigned)
    print("Test. Summe von 'Keine, Eine, Zwei, Drei' muss eins sein: ", len(alleSigned) / numTests);
    
    print("Mehr als eine Signed pro Case :", len(mehrAlsEine) / numTests)

#for i in range(10):
anz_displays(5);
