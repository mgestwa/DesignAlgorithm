# Wczytaj biblioteki Python Standard i DesignScript
import sys
import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# Wartości wejściowe do tego węzła będą przechowywane w postaci listy w zmiennych IN.
DUAll = IN[0]
PipeAll = IN[1]

#Połączenie rur i przepływów
x = zip(DUAll, PipeAll)

#Posortowanie elementów od najmniejszego
x.sort()

#Filtrowanie elemetów: odpływy jednostkowe i sumy odpływów.
DU_05 = list(filter(lambda x: x[0] == 0.5, x))
DU_08 = list(filter(lambda x: x[0] == 0.8, x))
DU_25 = list(filter(lambda x: x[0] == 2.5, x))

TylkoDU = DU_05 + DU_08 + DU_25                 #Tylko odpływy jednostkowe
SumyDU = list(set(x).difference(TylkoDU))       #Pozostałe, sumy odpływów

#Określenie średnic rur przy przepływach TylkoDU (odpływy jednostkowe od urządzeń)
for i in TylkoDU:
    
# Przypisz dane wyjściowe do zmiennej OUT.
OUT = SumyDU