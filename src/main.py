# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:10:06 2019

@author: caritutis
"""

import ctypes as C
math=C.CDLL('./libmymath2.so')
tres=C.c_float(3)
cuatro=C.c_float(4)
res=C.c_float()
math.add_float_ref(C.byref(tres),
                   C.byref(cuatro),
                   C.byref(res))
res.value
print("el primer numero a sumar es =",tres.value)
print("el segundo numero a sumar es=",cuatro.value)
print("la suma da como resultado=",res.value)
