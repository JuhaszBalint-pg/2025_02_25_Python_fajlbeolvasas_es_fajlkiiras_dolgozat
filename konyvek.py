"""
Olvasd be a konyvek.txt adatait, majd oldd meg az alábbi feladatokat!

1. Hány könyv szerepel a fájlban?
2. Melyik könyvnek van a legtöbb oldala?
3. Melyik könyvnek van a legkevesebb oldala?
4. Melyik szerző írt a legtöbb könyvet?
5. Átlagosan hány oldalasak a könyvek?

***EXTRA - nehezebb feladat*** (nem kötelező, de érdemes megpróbálni):
6. Melyik kiadó adott ki a legtöbb könyvet?

A megoldott feladatokat a kiirt_adatok nevű mappában hozd létre statisztika.txt néven!
"""

konyvek = []
with open('beolvasando_adatok\konyvek.txt', 'r', encoding='utf-8') as forrasfajl:
    next (forrasfajl)

    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        cim = adatok[0]
        szerzo = adatok[1]
        oldalszam = int(adatok[2])
        kiado = adatok[3]

        konyv = {'cím': cim, 'szerző': szerzo, 'oldalszám': int(oldalszam), 'kiadó' : kiado}
        konyvek.append(konyv)

print(f'{konyvek=}')

#1. feladat: Hány könyv szerepel a fájlban?
konyvekszama = len(konyvek)

print(f"1. A beolvasott fájlban összesen {konyvekszama} könyv szerepel.")

#2. feladat: Melyik könyvnek van a legtöbb oldala?
legtobb_oldalszam = 0
legtobb_oldalu_konyv = str()
for konyv in konyvek:
    if konyv['oldalszám'] > legtobb_oldalszam:
        legtobb_oldalszam = konyv['oldalszám']
        legtobb_oldalu_konyv = konyv['cím']

print(f"2. A legtöbb oldalas könyv: {legtobb_oldalu_konyv}")

#3. feladat: Melyik könyvnek van a legkevesebb oldala?

legkevesebb_oldalszam = 1000000
legkevesebb_oldalu_konyv = str()
for konyv in konyvek:
    if konyv['oldalszám'] < legkevesebb_oldalszam:
        legkevesebb_oldalszam = konyv['oldalszám']
        legkevesebb_oldalu_konyv = konyv['cím']

print(f"3. A legkevesesbb oldalas könyv: {legkevesebb_oldalu_konyv}")

#4. feladat: Melyik szerző írt a legtöbb könyvet?
irok = {

}
for konyv in konyvek:
    if konyv['szerző'] in irok:
        irok[konyv['szerző']] += 1
    else:
        irok[konyv['szerző']] = 1

legtobbetirtak = []
legtobbetirt = 0
for k, v in irok.items():
    if legtobbetirt < v or legtobbetirt == v:
        legtobbetirt = v
        legtobbetiro = k
        legtobbetirtak.append(k)

print(f"4. A legtöbb könyvet író szerző/szerzők: {legtobbetirtak}")

#5. feladat: Átlagosan hány oldalasak a könyvek?
osszoldalszam = 0
for konyv in konyvek:
    osszoldalszam += konyv['oldalszám']
    atlagoldalszam = osszoldalszam/len(konyvek)
print(f'5. Az átlagos oldalszám: {atlagoldalszam:.2f}')

with open('kiirt_adatok\statisztika.txt', 'w', encoding='utf-8') as celfajl:
    celfajl.write(f'A beolvasott fájlban összesen {konyvekszama} könyv szerepel.\n')
    celfajl.write(f'A legtöbb oldalas könyv: {legtobb_oldalu_konyv}\n')
    celfajl.write(f'A legkevesesbb oldalas könyv: {legkevesebb_oldalu_konyv}\n')
    celfajl.write(f'A legtöbb könyvet író szerző/szerzők: {legtobbetirtak}\n')
    celfajl.write(f'Az átlagos oldalszám: {atlagoldalszam:.2f}')