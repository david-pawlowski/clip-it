import numpy as np
import cv2
from mss import mss

MY_WIDTH = 1440
MY_HEIGHT = 900
FPS = 30
FRAME_SIZE = tuple((MY_WIDTH * 2, MY_HEIGHT * 2))

def record(duration=10):
    """
    Records the screen for 10 seconds and saves it to output.mp4
    It is adjusted to work on a 1440x900 screen atm
    
    """
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, FPS, (FRAME_SIZE))
    monitor = {"top": 0, "left": 0, "width": MY_WIDTH, "height": MY_HEIGHT}
    with mss(with_cursor=True) as sct:
        for _ in range(FPS * duration):
            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            out.write(img)
    out.release()
