class Karakter:
    def __init__(self,nev:str,rend:str,lezerkard:str,midiklorian:int):
        self.Nev = nev
        self.Rend = rend
        self.Lezerkard = lezerkard
        self.Midiklorian = midiklorian
    def __str__(self):
        return f"{self.Nev:20}| {self.Rend:6}| {self.Lezerkard:6}| {self.Midiklorian}"
    

def atlagosMidiklorian():
    osszeg = 0
    for karakter in karakterek:
        osszeg+= karakter.Midiklorian
    return osszeg/len(karakterek)

def atlagfelettiMid():
    for karakter in karakterek:
        if karakter.Midiklorian>atlagosMidiklorian():
            print(karakter)

#adatok beolvasása fájlból és mentése objektumlistába
karakterek = []
with open("star-wars.csv","r",encoding = "utf-8") as fajl:
    fajl.readline()
    for sor in fajl:
        darabol = sor.split(',')
        peldany = Karakter(darabol[0],darabol[1],darabol[2],int(darabol[3]))
        karakterek.append(peldany)

#Listázd ki a Jediket. Hány Jedi van összesen?
jediDb = 0
for karakter in karakterek:
    if karakter.Rend == "Jedi":
        print(karakter)
        jediDb+=1
print(f"Jedik száma: {jediDb}")


maxmidiklorian = 0
legerosebbSith = ""
for karakter in karakterek:
    if karakter.Rend == "Sith" and karakter.Midiklorian>maxmidiklorian:
        maxmidiklorian = karakter.Midiklorian
        legerosebbSith = karakter.Nev
print(f"A legerőssebb Sith: {legerosebbSith} , midiklorian száma: {maxmidiklorian}")


for karakter in karakterek:
    if karakter.Rend == "Jedi" and karakter.Lezerkard == "Piros":
        print(karakter)



minmidiklorian = 20000
leggyengebbJedi = ""
for karakter in karakterek:
    if karakter.Rend == "Jedi" and karakter.Midiklorian < minmidiklorian:
        minmidiklorian = karakter.Midiklorian
        leggyengebbJedi = karakter.Nev

print(f"Legkisebb midikloriánszámú Jedi: {leggyengebbJedi}, Midiklorian száma: {minmidiklorian}")

for karakter in karakterek:
    if karakter.Nev == "Ahsoka Tano":
        print(f"Ahsoka Tano lézerkardja: {karakter.Lezerkard}")


print(atlagosMidiklorian())

atlagfelettiMid()