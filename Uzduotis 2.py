"""Sukurti klasę Sukaktis, kuri turėtų savybę data
(galima atskirai įvesti metus, mėnesius ir kt.) ir metodus, kurie:"""

import datetime

now = datetime.datetime.now()

class Sukaktis:
    def __init__(self, data = "1990-08-31"): #defaultinis tekstas #3 uzduotis
        self.data = data

    #Perdaryti 2 užduotį taip, kad spausdinant datos objektą,
    # spausdintų ne objekto adresą, o įvestą datą
    def __str__(self):
        return self.data

    # Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
    def kiek_praejo(self):
        while True:
            try:
                gimimo_data = datetime.datetime.strptime(self.data, "%Y-%m-%d")

                print(f"Sukakties data: {gimimo_data}")

                skirtumas = now - gimimo_data
                skirtumas_days = int(skirtumas.days)
                skirtumas_month = int(skirtumas_days / 30.436875)  # vid dienu per menesi
                skirtumas_year = int(skirtumas_days / 365.2425)  # vid dienu per metus
                skirtumas_min = skirtumas_days * 1440
                skirtumas_sec = skirtumas_days * 86400

                print(f"Praejo {skirtumas_year} metu.")
                print(f"Praejo {skirtumas_month} menesiu.")
                print(f"Praejo {skirtumas_days} dienu.")
                print(f"Praejo {skirtumas_min} minuciu.")
                print(f"Praejo {skirtumas_sec} sekundziu.")
                break
            except:
                print("!!!Neteisingai ivedete gimimo data!!!")
                break

    # 2. Gražina, ar nurodytos sukakties metai buvo keliamieji
    def ar_keliamieji(self):
        import calendar
        metai = str(self.data).split("-") #splitina per sita simboli
        return calendar.isleap(int(metai[0]))

    #3. Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
    def atimti_dienas(self, dienu_sk):
        sukaktis = datetime.datetime.strptime(self.data, "%Y-%m-%d")
        return (sukaktis - datetime.timedelta(days=dienu_sk)).strftime("%Y-%m-%d")

    #4. Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą
    def prideti_dienas(self, dienu_sk):
        sukaktis = datetime.datetime.strptime(self.data, "%Y-%m-%d")
        return (sukaktis + datetime.timedelta(days=dienu_sk)).strftime("%Y-%m-%d")





sukakties_data = Sukaktis(input("Iveskite sukakties data: (YYYY-MM-DD)"))
sukakties_data.kiek_praejo() #1 Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
print("Ar keliamieji:", sukakties_data.ar_keliamieji()) #2. Gražina, ar nurodytos sukakties metai buvo keliamieji
print(sukakties_data.atimti_dienas(365))
print(sukakties_data.prideti_dienas(366))
























# def __init__(self, metai, menuo, diena, valanda=00, minutes=00, sekundes=00):
#     self.metai = metai
#     self.menuo = menuo
#     self.diena = diena
#     self.valanda = valanda
#     self.minutes = minutes
#     self.sekundes = sekundes