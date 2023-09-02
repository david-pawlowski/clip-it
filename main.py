from threading import Thread
from recognize_speech import recognize_speech

from screenshots import delete_old_screenshots, do_screenshots
from video import make_video


DURATION = 10
SS_DIR = "screenshoots"


def main():
    """
    If 'clip it' said it creates video from captured screenshots
    """
    t1 = Thread(target=do_screenshots, kwargs={"ss_dir": SS_DIR})
    t2 = Thread(
        target=delete_old_screenshots, kwargs={"duration": DURATION, "ss_dir": SS_DIR}
    )
    t1.start()
    t2.start()
    while True:
        if not recognize_speech() == "clip it":
            continue
        # TODO: MAKES NO SENSE AS T1 AND T2 ARE INFINITE LOOPS
        t2.join()
        t1.join()
        return make_video("screenshoots", "output.mp4")


if __name__ == "__main__":
    main()
