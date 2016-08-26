#!/usr/bin/python

import ctypes as ct

lib = ct.CDLL("libf2.so")

# pass int
a = ct.c_int(0)
while a.value < 1000:
  a.value = lib.incValue(a)

print a.value

# pass double
a = ct.c_double(0.0)
incDoubleValue = lib.incDoubleValue
incDoubleValue.restype = ct.c_double
while a.value < 999.8:
  a.value = lib.incDoubleValue(a)

print a.value

# pass pointer as argument
i = c_int(0)
p = 
