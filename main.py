import numpy as np
import cv2
from mss import mss

MAC_WIDTH = 1440
MAC_HEIGHT = 900
FRAME_SIZE = tuple((MAC_WIDTH * 2, MAC_HEIGHT * 2))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 60, (FRAME_SIZE))

with mss() as sct:
    monitor = {"top": 0, "left": 0, "width": 1440, "height": 900}
    while True:
        img = np.array(sct.grab(monitor))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        out.write(img)

        if cv2.waitKey(2) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
