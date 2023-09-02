import speech_recognition as sr


def recognize_speech():
    """
    Listens to microphone until it recognize some words
    and returns string of what it hears,
    uses google speech recognition(limit 50 calls per day)
    :return: string of what it hears
    """
    speech_recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        audio = speech_recognizer.listen(source)
    try:
        return speech_recognizer.recognize_google(audio)
    except sr.exceptions.UnknownValueError:
        return None
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(
                e
            )
        )
