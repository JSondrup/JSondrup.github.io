from ast import If


print('Hej!')
print('Hvor mange DKK vil du veksle til Euro?')
DKK_string=input()
DKK = float(DKK_string)
print('Du vil veksle '+ str(int(DKK))+' DKK')
kurs=float(0.13)
print('Det bliver så '+ str(DKK*kurs) +' Euro')
gebyr=((DKK*kurs)*0.02)
if gebyr>0.5:
    print('Minus gebyr bliver det ' + str((DKK*kurs)*0.8) + ' Euro')
else:
    Gebyr_under=0.5
    print('Minus gebyr bliver det '+ str((DKK*kurs)-Gebyr_under) + ' Euro')