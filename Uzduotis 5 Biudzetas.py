class Irasas:
    tipas = input("Iveskite tipa: ")
    suma = int(input("Iveskite suma: "))



class Biudzetas:
    def __init__(self, ivesti_duomenys):
        self.zurnalas = [ivesti_duomenys]


    #Metodas prideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą,
    # sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
    def prideti_pajamu_irasa(self, suma):
        self.zurnalas.append(suma)
        print(suma)

    #Metodas prideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą,
    # sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
    def prideti_islaidu_irasa(self, suma):



    #Metodas gauti_balansą(self), kuris gražintų žurnale
    # laikomų pajamų ir išlaidų balansą.
    def gauti_balansa(self):
        return sum(self.zurnalas)


    #Metodas parodyti_ataskaita(self), kuris atspausdintų visus pajamų
    # ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).
    def parodyti_ataskaita(self):
        print()
