import numpy as np
import cv2
from mss import mss

MAC_WIDTH = 1440
MAC_HEIGHT = 900
FPS = 30
FRAME_SIZE = tuple((MAC_WIDTH * 2, MAC_HEIGHT * 2))

def main():
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter('output.mp4', fourcc, FPS, (FRAME_SIZE))
    monitor = {"top": 0, "left": 0, "width": MAC_WIDTH, "height": MAC_HEIGHT}
    with mss(with_cursor=True) as sct:
        for _ in range(FPS * 10):
            img = np.array(sct.grab(monitor))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            out.write(img)
    out.release()

if __name__ == "__main__":
    main()
