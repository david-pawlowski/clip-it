from screen_recorder import record
from recognize_speech import recognize_speech


def main():
    """
    If 'clip it' said records screen for 10 seconds and saves it to output.mp4
    """
    while True:
        if not recognize_speech() == 'clip it':
            continue
        return record()

if __name__ == "__main__":
    main()
