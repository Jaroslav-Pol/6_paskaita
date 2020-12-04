# class Kate:
#     def __init__(self, spalva, amzius): #galima nurodyti defaultines reiksmes
#         self.spalva = spalva
#         self.amzius = amzius
#         print("Objektas sukurtas")
#
# kate1 = Kate("Juoda", 7)
# kate2 = Kate("Balta", 3)
#
# print(kate1.spalva)
#
# kate2.amzius = 8  # jeigu norime pakeisti kazkokius objekto paramentrus
# print(kate2.amzius)

# class Kate:
#     def __init__(self, spalva, amzius): #galima nurodyti defaultines reiksmes
#         self.spalva = spalva
#         self.amzius = amzius
#
#     def miaukseti(self):
#         print(f"{self.spalva} kate sako MIAU!")
#
# kate1 = Kate("Juoda", 7)
# kate2 = Kate("Balta", 3)
#
# print(kate2.miaukseti())
#

# class Kate:
#     def __init__(self, spalva, amzius):
#         self.spalva = spalva
#         self.amzius = amzius
#
#     def miaukseti(self, miauksejimas = "Miau", kartai = 1):
#         print(miauksejimas * kartai)
#
# kate1 = Kate("Juoda", 7)
# kate2 = Kate("Balta", 3)
#
# kate2.miaukseti("MUR ", 5)
# kate1.miaukseti()

# class Kate:
#     def __init__(self, spalva, amzius):
#         self.spalva = spalva
#         self.amzius = amzius
#
#     def __str__(self):
#         return f"Kate {self.spalva}, amzius - {self.amzius}" #specialus metodas, kuris defaultu paleidziamas iskvietus objekta pvz print(kate1)
#     # def miaukseti(self, miauksejimas = "Miau", kartai = 1):
#     #     print(miauksejimas * kartai)
#
#     # def _judinti_kojas(self): # jeigu _ priekyje, reikia private metoda, kuri galima pasiekti tik kitam metode
#     #     pass
#     #
#     # def _ziureti_kur_begi(self):
#     #     pass
#
#     def begti(self):
#         # self._judinti_kojas()
#         # self._ziureti_kur_begi()
#         print("Bėgu")
#
# kate1 = Kate("Juoda", 7)
# kate2 = Kate("Balta", 3)
#
# print(kate1)
# print(kate2)
#

# pasisveikinimas = str("Sveikas pasauli") #stringai pythone ir kiti dalykai yra irgi objektai is tam tikros built in clases
# print(pasisveikinimas)