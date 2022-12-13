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


#p3, p6, p9, p16:

r36916 = 255
g36916 = 0
b36916 = 0

#p2, p4, p5, p7, p10, p12, p13, p15:

r = 0
g = 255
b = 0

#p1, p8, p11, p14:

r = 0
g = 0
b = 255