import struct
import sys
import ctypes
import numpy as np

img = np.array([3, 2, 3, 2, 3, 2, 3]).astype('clongdouble')
print(img, img.dtype)
print(sys.getsizeof(img))
print(sys.getsizeof(np.uintc(3)))
print(sys.getsizeof(np.int8(1)))


def print_size_ctypes_var():
    print(sys.getsizeof(ctypes.c_bool))
    print(sys.getsizeof(ctypes.c_char))
    print(sys.getsizeof(ctypes.c_wchar))
    print(sys.getsizeof(ctypes.c_byte))
    print(sys.getsizeof(ctypes.c_ubyte))
    print(sys.getsizeof(ctypes.c_short))
    print(sys.getsizeof(ctypes.c_ushort))
    print(sys.getsizeof(ctypes.c_int))
    print(sys.getsizeof(ctypes.c_uint))
    print(sys.getsizeof(ctypes.c_long))
    print(sys.getsizeof(ctypes.c_ulong))
    print(sys.getsizeof(ctypes.c_longlong))
    print(sys.getsizeof(ctypes.c_ulonglong))
    print(sys.getsizeof(ctypes.c_size_t))
    print(sys.getsizeof(ctypes.c_ssize_t))
    print(sys.getsizeof(ctypes.c_float))
    print(sys.getsizeof(ctypes.c_double))
    print(sys.getsizeof(ctypes.c_longdouble))
    print(sys.getsizeof(ctypes.c_char_p))
    print(sys.getsizeof(ctypes.c_wchar_p))
    print(sys.getsizeof(ctypes.c_void_p))
