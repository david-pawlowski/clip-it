import time
from PIL import ImageGrab
import datetime
import os
from threading import Thread

SS_DIR = "screenshoots"
DURATION = 10


def get_file_creation_time(file):
    return datetime.datetime.fromtimestamp(os.path.getctime(file))


def is_file_older_than(file, duration=DURATION):
    return datetime.datetime.now() - get_file_creation_time(file) > datetime.timedelta(
        seconds=duration
    )


def do_screenshots():
    while True:
        img = ImageGrab.grab()
        img.save(f"{SS_DIR}/{datetime.datetime.now()}.png", "PNG")


def delete_old_screenshots():
    while True:
        for file in os.listdir(SS_DIR):
            if not is_file_older_than(f"{SS_DIR}/{file}", DURATION):
                continue
            os.remove(f"{SS_DIR}/{file}")


if __name__ == "__main__":
    Thread(target=do_screenshots).start()
    time.sleep(DURATION)
    Thread(target=delete_old_screenshots).start()
