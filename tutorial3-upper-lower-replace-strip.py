#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 12:59:22 2023

@author: emirhankabakci
"""

#upper method
gel_yaz = "geleceği yazanlar"
print(gel_yaz.upper())

#lower method
print(gel_yaz.lower())

#yazının küçük mü büyük harf mi olduğunu kontrol etmek için (ilk verilen değişkenin)
print(gel_yaz.islower())
print(gel_yaz.isupper())

#replace - verilen değişkendeki istediğimiz bir değeri istediğimiz bir değere dönüştürmek için kullanılır
print(gel_yaz.replace("e","a"))

#strip - istemediğimiz değeri silelim
stripDeger = "merhaba dünya**"
print(stripDeger.strip("*"))

