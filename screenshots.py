from PIL import ImageGrab
import datetime
import os


def get_file_creation_time(file):
    return datetime.datetime.fromtimestamp(os.path.getctime(file))


def is_file_older_than(file, duration):
    return datetime.datetime.now() - get_file_creation_time(file) > datetime.timedelta(
        seconds=duration
    )


def do_screenshots(ss_dir):
    while True:
        img = ImageGrab.grab()
        img.save(f"{ss_dir}/{datetime.datetime.now()}.png", "PNG")


def delete_old_screenshots(duration, ss_dir):
    while True:
        for file in os.listdir(ss_dir):
            if not is_file_older_than(f"{ss_dir}/{file}", duration):
                continue
            os.remove(f"{ss_dir}/{file}")
