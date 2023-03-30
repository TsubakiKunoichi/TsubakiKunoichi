import random
import numpy as np

spc = 3 # signed pro case
dpc = 18 # displays pro case
bpd = 12 # booster pro display
list_signed_info = list() # Liste für pulled signed pro case inkl. x displays aus einem case und mindestens eine Signed pro Case
                        # [pspc, xdpc, mspc]

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
    list_signed_info.append(list([pspc,xdpc]))
    keineSigned = list(filter(lambda x: x == 0, signed))
    eineSigned = list(filter(lambda x: x == 1, signed))
    zweiSigned = list(filter(lambda x: x == 2, signed))
    dreiSigned = list(filter(lambda x: x == 3, signed))
    mehrAlsEine  = list(filter(lambda x: x >= 1, signed))
    mehrAlsZwei  = list(filter(lambda x: x >= 2, signed))
    mehrAlsDrei  = list(filter(lambda x: x >= 3, signed))

    print("Durchschnittliche Signed Pro Case :", pspc)

    print("Keine Signed pro Case :", len(keineSigned) / numTests)
    print("Eine Signed pro Case :", len(eineSigned) / numTests)
    print("Zwei Signed pro Case :", len(zweiSigned) / numTests)
    print("Drei Signed pro Case :", len(dreiSigned) / numTests)
    alleSigned = keineSigned;
    alleSigned.extend(eineSigned)
    alleSigned.extend(zweiSigned)
    alleSigned.extend(dreiSigned)
    print("Test. Summe von 'Keine, Eine, Zwei, Drei' muss eins sein: ", len(alleSigned) / numTests);
    
    mspc = len(mehrAlsEine) / numTests
    print("Mehr als eine Signed pro Case :", mspc)
    elt = list_signed_info.pop()
    elt.append(mspc)
    elt.append(len(mehrAlsZwei) / numTests)
    elt.append(len(mehrAlsDrei) / numTests)
    list_signed_info.append(elt)

for i in range(19):
    print(f"-----Chancen für {i} Displays--------------------------------------------")
    anz_displays(i);

for [ps, xd, m1s, m2s, m3s] in list_signed_info:
    if xd == 0:
        print("No output when no displays are bought.")
    else:
        #print(xd, "displays pro Case get you ", ps, "signed on average. These are ", ps/xd, "signed per display.")
        print(xd, " displays pro Case get you at least ", m1s, "signed. Hence a quota of ", m1s/xd, " at least one signed per display.")
print("The quota could be interpreted as score and the highest score yields the most efficient signed per case, factoring in displays.")

print("Comprehensive Score-Output:")
for [ps, xd, m1s, m2s, m3s] in list_signed_info:
    if xd > 0:
        print(xd, " displays, min. 1: ", m1s/xd,", min. 2: ", m2s/xd, ", min. 3: ", m3s/xd)
