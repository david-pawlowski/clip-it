from setuptools import find_packages, setup

setup(
    name='clip-it',
    version='1.0',
    description='Screen reocrder, that creates video from captured screenshots',
    author='karamba',
#    author_email='foomail@foo.example',
    packages=find_packages(),
    install_requires=['opencv-python', 'pyaudio', 'SpeechRecognition', 'Pillow'], #external packages as dependencies
)
