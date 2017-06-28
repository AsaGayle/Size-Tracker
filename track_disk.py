import ctypes
import os
import platform
import sys

MAX_DISK_SIZE = 464000

def get_free_space_mb(dirname):
    """Return folder/drive free space (in megabytes)."""
    if platform.system() == 'Windows':
        free_bytes = ctypes.c_ulonglong(0)
        ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(dirname), None, None, ctypes.pointer(free_bytes))
        return free_bytes.value / 1024 / 1024
    else:
        st = os.statvfs(dirname)
        return st.f_bavail * st.f_frsize / 1024 / 1024

def get_disk_percentage(dirname):
    """Return percentage of disk space remaining"""
    space = int((get_free_space_mb(dirname)/MAX_DISK_SIZE)*100)
    return space

print(get_disk_percentage('/'))
