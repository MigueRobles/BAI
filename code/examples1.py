#! /usr/bin/env python
# -*- coding: utf-8 -*-

def maxi(a,b):
    if a>b:
        return a
    else:
        return b

def max_de_tres(a,b,c):
    max = a
    if b>max:
        max = b
    if c > max:
        max = c
    return max

def longitud(string):
    total = 0

    for c in string:
        total +=1
    return total

def sumar(lista):
    suma = 0
    for e in lista:
        suma +=e
    return suma

def mult(lista):
    producto = 1
    for e in lista:
        producto *= e
    return producto

def cadinversa(cadena):
    inversa = ""
    for i in range(longitud(cadena)):
        inversa += cadena[-i-1]
    return inversa

def comun(cadena1, cadena2):
    for i in cadena1:
        for j in cadena2:
            if i == j:
                return True
    return False

def generar_n_caracteres_ver1(n,c):
    cad = ""
    for i in range(n):
        cad+=c
    return cad
def generar_n_caracteres_ver2(n,c):
    return n*c

def procedimiento(lista):
    for i in lista:
        print i*"*"

print(maxi(8,15))
print(max_de_tres(3,25,3))
print(longitud("Amapola"))
print(sumar([1,2,3,4]))
print(mult([1,2,3,4]))
print(cadinversa("Amapola"))
print(comun("Amapola","Margarita"))
print(generar_n_caracteres_ver1(5,"x"))
print(generar_n_caracteres_ver2(5,"x"))
procedimiento([4,2,3])
