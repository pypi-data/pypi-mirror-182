from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'hi my package do many thing and made by liveofcode '
LONG_DESCRIPTION = 'hi this package do this  chatbot, input to file Translatortext it have Speak engine ,Listen engine,write like print password maker and do math and search on google and search website'

# Setting up
setup(
    name="pyliveofcode",
    version=VERSION,
    author="liveofcode",
    author_email="liveallgamegamer@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['pyliveofcode'],
    install_requires=['openai','python-dotenv','pyttsx3','SpeechRecognition','googletrans'])
