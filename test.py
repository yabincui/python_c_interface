#!/usr/bin/python

import ctypes as ct

lib = ct.CDLL("./libf2.so")

# pass and return int
a = ct.c_int(0)
while a.value < 1000:
  a.value = lib.incValue(a)

print a.value

# pass and return double
a = ct.c_double(0.0)
incDoubleValue = lib.incDoubleValue
incDoubleValue.restype = ct.c_double
while a.value < 999.8:
  a.value = lib.incDoubleValue(a)

print a.value

# pass pointer as argument
i = ct.c_int(0)
p = ct.pointer(i)
while i.value < 1000:
    lib.incInlineValue(p)

print i.value

# return pointer
retPointerFunc = lib.retPointer
retPointerFunc.restype = ct.POINTER(ct.c_int)
for i in range(1000):
    p = retPointerFunc()
    p[0]=p[0]+1

p = retPointerFunc()
print p[0]

# pass string as argument
s = ct.create_string_buffer('\000' * 32)
s.value = "hello, world"
lib.printString(s)

lib.printString("hello, world")
a = "hello"
a += "wworld"
lib.printString(a)

# return string
retStringFunc = lib.retString
retStringFunc.restype = ct.c_char_p
print retStringFunc()

# pass array as argument
a = (ct.c_int * 10)()
lib.incArray(a, 10)
for i in range(10):
    print a[i],
print

# return array pointer
retArrayFunc = lib.retArray
retArrayFunc.restype = ct.POINTER(ct.c_int)
p = retArrayFunc()
for i in range(10):
    print p[i],
print

# pass struct as argument
class MyStruct(ct.Structure):
    _fields_ = [('count', ct.c_int),
                 ('s', ct.POINTER(ct.c_int))]

myStru = MyStruct()
myStru.count = 10
a = (ct.c_int * 10)()
myStru.s = ct.cast(a, ct.POINTER(ct.c_int))
for i in range(10):
    myStru.s[i] = i + 1
for i in range(10):
    print myStru.s[i],
print

lib.printStruct(myStru)
lib.printStructP(ct.pointer(myStru))

# return struct
retStructFunc = lib.retStruct
retStructFunc.restype = MyStruct
myStru = retStructFunc()
for i in range(myStru.count):
    print myStru.s[i],
print

retStructPFunc = lib.retStructP
retStructPFunc.restype = ct.POINTER(MyStruct)
p = retStructPFunc()
for i in range(p[0].count):
    print p[0].s[i],
print

# check null pointer
retNullFunc = lib.retNull
retNullFunc.restype = ct.POINTER(MyStruct)
for i in range(2):
  p = retNullFunc()
  print p
  a = ct.cast(p, ct.c_void_p)
  if a.value is None:
    print 'retNullFunc() returns nullptr'
  else:
    print 'retNullFunc() doesn\'t return nullptr'
    p[0]

# python callback function called from c
CALLBACK_TYPE = ct.CFUNCTYPE(ct.c_int);

a = 0
def callback_func():
    global a
    a = a + 1
    return a

callback = CALLBACK_TYPE(callback_func)
lib.callCallback(callback)









