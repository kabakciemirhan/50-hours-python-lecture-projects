#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 16:54:40 2023

@author: emirhankabakci
"""

#veri yapıları - dictionary (sözlük)
#sözlükler kapsayıcıdır, değiştirilebilir ama sırasızdır
#sözlük içinde diziler de olabilir
sozluk = {
    "reg" : "regresyon modeli",
    "loj" : ["lojistik regresyon", 28, 17.5],
    "cart" :"classification and reg"
}
print(len(sozluk))
print(sozluk)

#sözlükten seçim yapma
print(sozluk["reg"])