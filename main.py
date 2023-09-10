import logging
import datetime
import os
import speech_recognition as sr

from threading import Thread

from PIL import ImageGrab

from video import make_video


DURATION = 60
SS_DIR = "screenshoots"

condition = True


def recognize_speech():
    """
    Listens to microphone until it recognize some words
    and returns string of what it hears,
    uses google speech recognition(limit 50 calls per day)
    :return: string of what it hears
    """
    while condition:
        speech_recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            audio = speech_recognizer.listen(source)
        try:
            return speech_recognizer.recognize_google(audio)
        except sr.exceptions.UnknownValueError:
            return None
        except sr.RequestError as e:
            logging.error(
                "Could not request results from \
                    Google Speech Recognition service; {0}".format(
                    e
                )
            )


def get_file_creation_time(file):
    return datetime.datetime.fromtimestamp(os.path.getctime(file))


def is_file_older_than(file, duration):
    return (
        datetime.datetime.now() - get_file_creation_time(file) >
        datetime.timedelta(seconds=duration)
    )


def do_screenshots(ss_dir):
    while condition:
        img = ImageGrab.grab()
        img.save(f"{ss_dir}/{datetime.datetime.now()}.png", "PNG")


def delete_old_screenshots(duration, ss_dir):
    while condition:
        for file in os.listdir(ss_dir):
            if not is_file_older_than(f"{ss_dir}/{file}", duration):
                continue
            os.remove(f"{ss_dir}/{file}")


def main():
    """
    If 'clip it' said it creates video from captured screenshots
    """
    global condition
    t1 = Thread(target=do_screenshots, kwargs={"ss_dir": SS_DIR})
    t2 = Thread(
        target=delete_old_screenshots, kwargs={
            "duration": DURATION, "ss_dir": SS_DIR
        }
    )
    t1.start()
    t2.start()
    while True:
        text = recognize_speech() or "nothing"
        print(text)
        if "clip it" not in text:
            continue
        condition = False
        return make_video("screenshoots", "output.mp4")


if __name__ == "__main__":
    main()
