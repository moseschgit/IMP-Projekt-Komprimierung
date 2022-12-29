#IMP Projekt: Bildkomprimierung 
#Gruppe: Laurenz Jonathan Vanessa


#Protokoll noch schreiben
# schauen, was wir sonst noch machen müssen vanessa
#codierung verstehen, erklären ycbcr laurenz
#ideen holen, nachdenken wie man es programmieren könnte jonathan
#protokoll schreiben : Jonathan
#erklärung/ präsentation zum Projekt: Vanessa (schaut was wir bei der präsentation machen könnten, z.B. erklärung komprimierung generell, ycbcr generell usw.)
#--> alles visualisieren und fortschritte, sowie notizen in gemeinsamme gruppe schicken


#Überlegung 1 
#Bild in Replit einfügen --> Überlegung 2 wird durchgeführt --> Bild wird komprimiert Ausgegeben
# --> PROBLEM: KANN KEIN BILD EINFÜGEN/ AUSGEBEN



#Überlegung 2
#bild in der theorie komprimieren
#pixel werden mit Listen angegeben, die zusammengefasst werden 
#wenn pixel, die nebeneinander liegen ähnlich sind, werden sie zusammengefasst.
#am Ende schauen, wie viel gespeichert wurde



#Procreate design 


#möglichkeit fürs Schaubild
#import matplotlib.pyplot as plt
#import numpy as np

#x = np.linspace(0, 2 * np.pi, 200)
#y = np.sin(x)

#fig, ax = plt.subplots()
#ax.plot(x, y)
#plt.show()





#Beispiel für einen kleinen Abschnitt des Bildes, der zusammengefasst wird

#Jedes Bild wird in 16 Raster aufgeteilt (4x4) bei jedem Raster bestimmte Anzahl an Werten (hier im bsp. 8 Werte) --> NOCH SCHAUEN WIE MAN DIE EINZELNEN FARBEN IN ZAHLEN DEFINIERT

#a1= 100
#b2= 200
#c3= 155
#d4= 160
#e5= 170
#f6= 180
#g7= 190
#h8= 200

#Listen werden mit Variablen aufgebaut 







#l1 = [a1, b2, c3, d4, e5, f6,g7, h8]




#Mittelwert wird ausgerechnet 

#pythonic_machine_ages = [a1, b2, c3, d4, e5, f6,g7, h8]

#def mean(dataset):
#    return sum(dataset) / len(dataset)




#print(mean(pythonic_machine_ages))

#def pixelabfrage(rgb_im, x, y):
# rgb_im = rgb_im
#  x = x
#  y = y
#  r, g, b = rgb_im.getpixel ((x,y))

#print ('Pixelkoordinaten:%3s%3s  rot:%3s grün:3%s  blau:%3s'% (x, y, r, g, b))

#rgb in ycbcr umwandeln dann graustufe in liste eintragen und mittelwert




#Pixel definieren
#p=Pixel x=Zahl des Pixels

#px
#pixel bestehen aus r , g , b

#Neue Pixel definieren: (aus 16 x 16 wird 4x4) --> hier werden die neuen Pixel als Spalten definiert


#Wir wollten etwas programmieren, dass die Farben eines Bildes erkennt, was wir leider nicht geschafft haben, weshlab man die Farben manuell eintragen muss.

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

r9 = 0
g9 = 0
b9 = 255

r10 = 0
g10 = 0
b10 = 255

r11 = 0
g11 = 0
b11 = 255

r12 = 0
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



#Mittelwert der RGB-Werte werden ausgerechnet, um die neuen RGB-Werte zu definieren

#Name = r=red/g=green/b=blue + m=Mittelwert + p=Pixel + 1-4=Nummer des Pixels

#Pixel2 
rmp1 = sum(rp1) / len(rp1)
gmp1 = sum(gp1) / len(gp1)
bmp1 = sum(bp1) / len(bp1)

#Pixel2 
rmp2 = sum(rp2) / len(rp2)
gmp2 = sum(gp2) / len(gp2)
bmp2 = sum(bp2 / len(bp2)

#Pixel3 
rmp3 = sum(rp3) / len(rp3)
gmp3 = sum(gp3) / len(gp3)
bmp3 = sum(bp3) / len(bp3)

#Pixel4 
rp4 = sum(rp4) / len(rp4)
gp4 = sum(gp4) / len(gp4)
bp4 = sum(bp4) / len(bp4)
