#IMP Projekt: Bildkomprimierung 
#Gruppe: Laurenz Jonathan Vanessa

#Hier werden die RGB-Werte der Pixel definiert

print('Geben Sie bitte zuerst die RGB-Werte der 16 Pixel im Code an.')

r1 = 255
g1 = 0
b1 = 0

r2 = 0
g2 = 255
b2 = 0

r3 = 0
g3 = 0
b3 = 255

r4 = 0
g4 = 0
b4 = 255

r5 = 0
g5 = 0
b5 = 255

r6 = 0
g6 = 0
b6 = 255

r7 = 0
g7 = 0
b7 = 255

r8 = 0
g8 = 0
b8 = 255

r9 = 255
g9 = 0
b9 = 255

r10 = 0
g10 = 0
b10 = 255

r11 = 0
g11 = 0
b11 = 255

r12 = 255
g12 = 0
b12 = 255

r13 = 0
g13 = 0
b13 = 255

r14 = 0
g14 = 0
b14 = 255

r15 = 0
g15 = 0
b15 = 255

r16 = 0
g16 = 0
b16 = 255


#Die 16 Pixel werden in vier Gruppen unterteilt, sodass aus 4 pixeln mit unterschiedlichen Farben ein Zusammenschluss aus gleichen Farben wird, sodass man weniger Farben speichern muss, wodurch man weniger Speicherplatz braucht.

#Pixel1 
rp1 = [r1,r2,r3,r4]
gp1 = [g1,g2,g3,g4]
bp1 = [b1,b2,b3,b4]

#Pixel2 
rp2 = [r5,r6,r7,r8]
gp2 = [g5,g6,g7,g8]
bp2 = [b5,b6,b7,b8]

#Pixel3 
rp3 = [r9,r10,r11,r12]
gp3 = [g9,g10,g11,g12]
bp3 = [b9,b10,b11,b12]

#Pixel4 
rp4 = [r13,r14,r15,r16]
gp4 = [g13,g14,g15,g16]
bp4 = [b13,b14,b15,b16]



#Hier wird der Mittelwert der RGB-Werte werden ausgerechnet, um den neuen RGB-Wert der vier Pixel zu definieren

#Aufbau des Variablenname's:  r=red/g=green/b=blue , m = Mittelwert , p = Pixel , 1-4 = Nummer des Pixels

#1. Lösungsversuch: rmpx = sum(rpx) / len(rpx) --> hat nicht funktioniert

from statistics import mean 

#Pixel1
rmp1 = mean(rp1)
gmp1 = mean(gp1)
bmp1 = mean(bp1)

#Pixel2 
rmp2 = mean(rp2)
gmp2 = mean(gp2)
bmp2 = mean(bp2)

#Pixel3 
rmp3 = mean(rp3)
gmp3 = mean(gp3)
bmp3 = mean(bp3)

#Pixel4 
rmp4 = mean(rp4)
gmp4 = mean(gp4)
bmp4 = mean(bp4)


print('Nach der Zusammenfassung der 16 Pixel gibt es nun neue RGB-Werte für jeden der vier neuen Pixel.')
print('Die RGB-Werte für den 1. Pixel lauten:', rmp1, gmp1, bmp1)
print('Die RGB-Werte für den 2. Pixel lauten:', rmp2, gmp2, bmp2)
print('Die RGB-Werte für den 3. Pixel lauten:', rmp3, gmp3, bmp3)
print('Die RGB-Werte für den 4. Pixel lauten:', rmp4, gmp4, bmp4)

#Die RGB-Werte werden hier in YCbCr-Werte umgewandelt

#Pixel 1

Y1 = 0.299 * rmp1 + 0.587 * gmp1 + 0.114 * bmp1 
Cb1 = -0.169 * rmp1 - 0.331 * gmp1 + 0.500 * bmp1 
Cr1= 0.500 * rmp1 - 0.419 * gmp1 - 0.081 * bmp1 

#Pixel 2

Y2 = 0.299 * rmp2 + 0.587 * gmp2 + 0.114 * bmp2 
Cb2 = -0.169 * rmp2 - 0.331 * gmp2 + 0.500 * bmp2 
Cr2= 0.500 * rmp2 - 0.419 * gmp2 - 0.081 * bmp2 

#Pixel 3

Y3 = 0.299 * rmp3 + 0.587 * gmp3 + 0.114 * bmp3 
Cb3 = -0.169 * rmp3 - 0.331 * gmp3 + 0.500 * bmp3 
Cr3= 0.500 * rmp3 - 0.419 * gmp3 - 0.081 * bmp3 

#Pixel 4

Y4 = 0.299 * rmp4 + 0.587 * gmp4 + 0.114 * bmp4 
Cb4 = -0.169 * rmp4 - 0.331 * gmp4 + 0.500 * bmp4 
Cr4= 0.500 * rmp4 - 0.419 * gmp4 - 0.081 * bmp4 

print('Die RGB-Werte der vier neuen Pixel werden anschließend von RGB in YCBcr umgewandelt.')

print('Die YCBcr-Werte für den 1. Pixel lauten:', Y1, Cb1, Cr1)
print('Die YCBcr-Werte für den 2. Pixel lauten:', Y2, Cb2, Cr2)
print('Die YCBcr-Werte für den 3. Pixel lauten:', Y3, Cb3, Cr3)
print('Die YCBcr-Werte für den 4. Pixel lauten:', Y4, Cb4, Cr4)