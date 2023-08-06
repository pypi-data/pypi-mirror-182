# https://github.com/Soldie/Stitch-Rat-pyton/blob/8e22e91c94237959c02d521aab58dc7e3d994cea/Configuration/mss/windows.py
import ctypes
from ctypes import wintypes
from collections import namedtuple

import mss
import numpy as np

user32 = ctypes.WinDLL("user32", use_last_error=True)
from ctypes import windll
from ctypes.wintypes import (
    BOOL,
    DOUBLE,
    DWORD,
    HBITMAP,
    HDC,
    HGDIOBJ,  # noqa
    HWND,
    INT,
    LPARAM,
    LONG,
    UINT,
    WORD,
)  # noqa


def check_zero(result, func, args):
    if not result:
        err = ctypes.get_last_error()
        if err:
            raise ctypes.WinError(err)
    return args


if not hasattr(wintypes, "LPDWORD"):  # PY2
    wintypes.LPDWORD = ctypes.POINTER(wintypes.DWORD)

WindowInfo = namedtuple("WindowInfo", "pid title hwnd length tid status")




def list_windows():
    """Return a sorted list of visible windows."""
    result = []

    @WNDENUMPROC
    def enum_proc(hWnd, lParam):
        status = 'invisible'
        if user32.IsWindowVisible(hWnd):
            status = 'visible'

        pid = wintypes.DWORD()
        tid = user32.GetWindowThreadProcessId(hWnd, ctypes.byref(pid))
        length = user32.GetWindowTextLengthW(hWnd) + 1
        title = ctypes.create_unicode_buffer(length)
        user32.GetWindowTextW(hWnd, title, length)
        result.append((WindowInfo(pid.value, title.value, hWnd, length, tid, status)))
        return True

    user32.EnumWindows(enum_proc, 0)
    return sorted(result)


SRCCOPY = 13369376
DIB_RGB_COLORS = BI_RGB = 0


class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]


class BITMAPINFOHEADER(ctypes.Structure):
    _fields_ = [
        ("biSize", DWORD),
        ("biWidth", LONG),
        ("biHeight", LONG),
        ("biPlanes", WORD),
        ("biBitCount", WORD),
        ("biCompression", DWORD),
        ("biSizeImage", DWORD),
        ("biXPelsPerMeter", LONG),
        ("biYPelsPerMeter", LONG),
        ("biClrUsed", DWORD),
        ("biClrImportant", DWORD),
    ]


class BITMAPINFO(ctypes.Structure):
    _fields_ = [("bmiHeader", BITMAPINFOHEADER), ("bmiColors", DWORD * 3)]


# Function shorthands


GetClientRect = windll.user32.GetClientRect
GetWindowRect = windll.user32.GetWindowRect
PrintWindow = windll.user32.PrintWindow
GetWindowThreadProcessId = windll.user32.GetWindowThreadProcessId
IsWindowVisible = windll.user32.IsWindowVisible
EnumWindows = windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(
    ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)
)

GetWindowDC = windll.user32.GetWindowDC
CreateCompatibleDC = windll.gdi32.CreateCompatibleDC
CreateCompatibleBitmap = windll.gdi32.CreateCompatibleBitmap
SelectObject = windll.gdi32.SelectObject
BitBlt = windll.gdi32.BitBlt
DeleteObject = windll.gdi32.DeleteObject
GetDIBits = windll.gdi32.GetDIBits

# Arg types
windll.user32.GetWindowDC.argtypes = [HWND]
windll.gdi32.CreateCompatibleDC.argtypes = [HDC]
windll.gdi32.CreateCompatibleBitmap.argtypes = [HDC, INT, INT]
windll.gdi32.SelectObject.argtypes = [HDC, HGDIOBJ]
windll.gdi32.BitBlt.argtypes = [HDC, INT, INT, INT, INT, HDC, INT, INT, DWORD]
windll.gdi32.DeleteObject.argtypes = [HGDIOBJ]
windll.gdi32.GetDIBits.argtypes = [
    HDC,
    HBITMAP,
    UINT,
    UINT,
    ctypes.c_void_p,
    ctypes.POINTER(BITMAPINFO),
    UINT,
]
# Return types
windll.user32.GetWindowDC.restypes = HDC
windll.gdi32.CreateCompatibleDC.restypes = HDC
windll.gdi32.CreateCompatibleBitmap.restypes = HBITMAP
windll.gdi32.SelectObject.restypes = HGDIOBJ
windll.gdi32.BitBlt.restypes = BOOL
windll.gdi32.GetDIBits.restypes = INT
windll.gdi32.DeleteObject.restypes = BOOL


WNDENUMPROC = ctypes.WINFUNCTYPE(
    wintypes.BOOL,
    wintypes.HWND,  # _In_ hWnd
    wintypes.LPARAM,
)  # _In_ lParam

user32.EnumWindows.errcheck = check_zero
user32.EnumWindows.argtypes = (
    WNDENUMPROC,  # _In_ lpEnumFunc
    wintypes.LPARAM,
)  # _In_ lParam

user32.IsWindowVisible.argtypes = (wintypes.HWND,)  # _In_ hWnd

user32.GetWindowThreadProcessId.restype = wintypes.DWORD
user32.GetWindowThreadProcessId.argtypes = (
    wintypes.HWND,  # _In_      hWnd
    wintypes.LPDWORD,
)  # _Out_opt_ lpdwProcessId

user32.GetWindowTextLengthW.errcheck = check_zero
user32.GetWindowTextLengthW.argtypes = (wintypes.HWND,)  # _In_ hWnd

user32.GetWindowTextW.errcheck = check_zero
user32.GetWindowTextW.argtypes = (
    wintypes.HWND,  # _In_  hWnd
    wintypes.LPWSTR,  # _Out_ lpString
    ctypes.c_int,
)  # _In_  nMaxCount
psapi = ctypes.WinDLL("psapi", use_last_error=True)

psapi.EnumProcesses.errcheck = check_zero
psapi.EnumProcesses.argtypes = (
    wintypes.LPDWORD,  # _Out_ pProcessIds
    wintypes.DWORD,  # _In_  cb
    wintypes.LPDWORD,
)  # _Out_ pBytesReturned


def screenshot(hwnd, client=True):
    """Grab a screenshot of the first visible window of the process
    with the given id. If client is True, no Window decoration is shown.
    This code is derived from https://github.com/BoboTiG/python-mss
    """
    rect = RECT()
    if client:
        GetClientRect(hwnd, ctypes.byref(rect))
    else:
        GetWindowRect(hwnd, ctypes.byref(rect))
    left, right, top, bottom = rect.left, rect.right, rect.top, rect.bottom
    w, h = right - left, bottom - top

    hwndDC = saveDC = bmp = None
    try:
        hwndDC = GetWindowDC(hwnd)
        saveDC = CreateCompatibleDC(hwndDC)
        bmp = CreateCompatibleBitmap(hwndDC, w, h)
        SelectObject(saveDC, bmp)
        if client:
            PrintWindow(hwnd, saveDC, 1)
        else:
            PrintWindow(hwnd, saveDC, 0)
        buffer_len = h * w * 4
        bmi = BITMAPINFO()
        bmi.bmiHeader.biSize = ctypes.sizeof(BITMAPINFOHEADER)
        bmi.bmiHeader.biWidth = w
        bmi.bmiHeader.biHeight = -h
        bmi.bmiHeader.biPlanes = 1
        bmi.bmiHeader.biBitCount = 32
        bmi.bmiHeader.biCompression = 0
        bmi.bmiHeader.biClrUsed = 0
        bmi.bmiHeader.biClrImportant = 0
        image = ctypes.create_string_buffer(buffer_len)
        bits = windll.gdi32.GetDIBits(saveDC, bmp, 0, h, image, bmi, DIB_RGB_COLORS)
        if bits != h:
            print("Error")
        image2 = bytearray(h * w * 3)
        image2[0::3], image2[1::3], image2[2::3] = image[2::4], image[1::4], image[0::4]

    finally:
        if hwndDC:
            DeleteObject(hwndDC)
        if saveDC:
            DeleteObject(saveDC)
        if bmp:
            DeleteObject(bmp)

    return (
        np.frombuffer(bytes(image2), dtype=np.uint8)
        .reshape((h, w, 3))[..., ::-1]
        .copy()
    )


def screencapture_window(hwnd, ignore_exceptions=True):
    while True:
        try:
            yield screenshot(hwnd, client=True)
        except Exception as fe:
            if not ignore_exceptions:
                raise fe
            continue


def screencapture(monitor, ignore_exceptions=True):
    with mss.mss() as sct:
        while True:
            try:
                bi = sct.grab(monitor)
                img = (
                    np.frombuffer(bytes(bi.raw), dtype=np.uint8)
                    .reshape((bi.height, bi.width, 4))[:, :, :3]
                    .copy()
                )
                yield img
            except Exception as fe:
                if not ignore_exceptions:
                    raise fe
                continue
