# Takes screenshots without pywin32 dependency (whole screen/single window)

```python
pip install ctypes-screenshot
```

```python
from ctypes_screenshots import screencapture_window, list_windows, screencapture

import cv2
import time

# get the hwnd if you want to capture a single window
list_windows()
# Out[5]: 
# [WindowInfo(pid=1544, title='Seagate Expansion Drive (F:)', hwnd=525322, length=29),
#  WindowInfo(pid=1840, title='', hwnd=72700, length=1),
#  WindowInfo(pid=1840, title='', hwnd=72702, length=1),
#  WindowInfo(pid=1840, title='jFDSk.png @ 100% (Layer 1, RGB/8)', hwnd=2362732, length=34),
#  WindowInfo(pid=3416, title='', hwnd=131744, length=1),

# captures a single window
for _ in screencapture_window(hwnd=5901160):
    last_time = time.time()
    cv2.imshow("OpenCV/Numpy normal", _)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
    print(f"fps: {1 / (time.time() - last_time)}", end="\r")

# uses mss 
for _ in screencapture(monitor={"top": 40, "left": 0, "width": 800, "height": 640}):
    last_time = time.time()
    cv2.imshow("OpenCV/Numpy normal", _)
    if cv2.waitKey(25) & 0xFF == ord("q"):
        cv2.destroyAllWindows()
        break
    print(f"fps: {1 / (time.time() - last_time)}", end="\r")



```
