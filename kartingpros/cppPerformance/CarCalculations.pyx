from libc.math cimport pow
PI = 3.14159265359
cdef calcRad(int direction):
    return PI * direction / 180