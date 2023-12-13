#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 13:16:00 2023

@author: emirhankabakci
"""

#kullanıcıdan bilgi almak için input kullanırız. input bunları string olarak getirir, o yüzden direkt böyle toplama yaparsak ikisini string olarak birleştirir.
birinci_sayi = input()
ikinci_sayi = input()
#aşağıdaki yolla string değerimizi int e çevirebiliriz. ya da floata. çıktıyı da int olarak alabiliriz ya da float. ne istersek yani. int olursa, noktalı kısmı yok eder program
topla = int(birinci_sayi) + float(ikinci_sayi)
print(topla)