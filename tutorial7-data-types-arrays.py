#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:14:26 2023

@author: emirhankabakci
"""

#veri yapıları

#listeler

#[]
#list()

notlar = [90, 80, 70, 60]
print(type(notlar))

yeniListe = ["a", 19.3, 59, notlar]
print(yeniListe)
print(yeniListe[2])
print(yeniListe[3])

#liste içi type sorgulama
print(type(yeniListe[0]))

#listeye eleman ekleme çıkarma
liste2 = ["ali", "veli"]
liste2 = liste2 + ["kemal"]
print(liste2)
del liste2[2]
print(liste2)

##ekleme çıkarmayı aynı zamanda metod ile yapabiliriz
liste3 = [1, 3, 56]
liste3.append(5)
print(liste3)
liste3.remove(liste3[2])
print(liste3)

#metotlarla eleman ekleme çıkarma
liste3.insert(0, "insert")
print(liste3)
liste3.pop(3)
print(liste3)