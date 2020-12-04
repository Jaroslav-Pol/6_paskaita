"""Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:"""
"""Perdaryti 1 užduotį taip, kad jei kuriant objektą, nepaduodamas joks tekstas, 
veiksmai turi būti atliekami su „Zen of Python“ tekstu"""

class Sakinys:
    def __init__(self, tekstas = "Zen of Python"):
        self.tekstas = tekstas

    # """1. Gražina tekstą atbulai"""
    def atbulai(self):
        return self.tekstas[::-1]

    # 2. Grazina teksta mazosiomis
    def mazosiomis(self):
        return self.tekstas.casefold()

    #3. Gražina tekstą didžiosiomis raidėmis
    def didziosiomis(self):
        return self.tekstas.upper()

    #4. Gražina žodį pagal nurodytą eilės numerį
    def pagal_numeri(self, numeris):
        zodziai = self.tekstas.split()
        return zodziai[numeris-1]

    #  arba
    # def pagal_numeri(self, numeris):
    #     return self.tekstas.split()[numeris -1]

    #5. Gražina, kiek tekste yra nurodytų simbolių arba žodžių
    def kiek_simboliu(self, simbolis):
        return self.tekstas.count(simbolis)

    #6. Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
    def pakeisk_zodi(self, senas_zodis, naujas_zodis):
        return self.tekstas.replace(senas_zodis, naujas_zodis)

    #7. Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
    def kiek_elementu(self):
        skaiciai = 0
        didziosios = 0
        mazosios = 0

        for simbolis in self.tekstas:
            if simbolis.isdigit():
                skaiciai += 1
            if simbolis.isupper():
                didziosios += 1
            if simbolis.islower():
                mazosios += 1

        print(f"Sakinyje yre {len(self.tekstas.split())} zodziai, {didziosios} diziosios raides, {mazosios} mazosios raides, {skaiciai} skaiciu.")


mano_sakinys = Sakinys("As esu katinas")


print(mano_sakinys.atbulai()) #1. Grazina teksta atbulai
print(mano_sakinys.mazosiomis())  # 2. Grazina teksta mazosiomis
print(mano_sakinys.didziosiomis()) #3. Gražina tekstą didžiosiomis raidėmis
print(mano_sakinys.pagal_numeri(3))  #4. Gražina žodį pagal nurodytą eilės numerį
print(mano_sakinys.kiek_simboliu("a")) #5. Gražina, kiek tekste yra nurodytų simbolių arba žodžių
print(mano_sakinys.pakeisk_zodi("katinas", "labai didelis barsukas!")) #6. Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
print(mano_sakinys.kiek_elementu())     #7. Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

mano_sakinys2 = Sakinys()

print(mano_sakinys2.atbulai()) #1. Grazina teksta atbulai
print(mano_sakinys2.mazosiomis())  # 2. Grazina teksta mazosiomis
print(mano_sakinys2.didziosiomis()) #3. Gražina tekstą didžiosiomis raidėmis
print(mano_sakinys2.pagal_numeri(3))  #4. Gražina žodį pagal nurodytą eilės numerį
print(mano_sakinys2.kiek_simboliu("a")) #5. Gražina, kiek tekste yra nurodytų simbolių arba žodžių
print(mano_sakinys2.pakeisk_zodi("Python", "labai didelis barsukas!")) #6. Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
print(mano_sakinys2.kiek_elementu())     #7. Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
