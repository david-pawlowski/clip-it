from threading import Thread
from recognize_speech import recognize_speech

from screenshots import delete_old_screenshots, do_screenshots
from video import make_video


def main():
    """
    If 'clip it' said it creates video from captured screenshots
    """
    Thread(target=do_screenshots).start()
    Thread(target=delete_old_screenshots).start()
    while True:
        if not recognize_speech() == 'clip it':
            continue
        return # stop threads and make video

if __name__ == "__main__":
    main()
