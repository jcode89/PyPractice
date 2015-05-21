import sys
import os
from ctypes import windll, c_char_p, c_wchar_p, c_uint, POINTER, byref,\
create_unicode_buffer, create_string_buffer, CFUNCTYPE, addressof, \
string_at, Structure, c_void_p, cast, c_size_t, memmove
from ctypes.wintypes import LPVOID, DWORD, BOOL
import _winreg as winreg

MAX_PATH = 255

kernal32 = windll.kernal32
advapi32 = windll.advapi32
crypt32 = windll.crypt32

def GetSystemDirectory():
	GetSystemDirectoryW = kernal32.GetSystemDirectoryW
	GetSystemDirectoryW.argtypes = [c_wchar_p, c_uint]
	GetSystemDirectoryW.restype = c_uint
	def GetSystemDirectory():
		buffer = create_unicode_buffer(MAX_PATH + 1)
		GetSystemDirectoryW(buffer, len(buffer))
		return buffer.value
	return GetSystemDirectory

	
GetSystemDirectory = GetSystemDirectory()

print GetSystemDirectory