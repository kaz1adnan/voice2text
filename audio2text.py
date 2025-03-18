import os
import speech_recognition as sr
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

test_filename = ""
FILENAME_FROM_MIC = "RECORDING.WAV"
VOICE_TEXT_FILENAME = "VOICE_AS_TEXT.txt"

r = sr.Recognizer()

def recognizeFromFile(filename):

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        return ""

    with sr.AudioFile(filename) as source:
        audioData = r.record(source)
        text = r.recognize_google(audioData)
        return text

def recognizeFromMicrophone(file2write):
    SAMPLE_RATE = 44100
    duration = 5 # in seconds
    audioRecording = sd.rec(duration * SAMPLE_RATE, samplerate = SAMPLE_RATE, channels = 1, dtype = 'int32')
    print("Recording Audio")
    sd.wait()
    sd.play(audioRecording, SAMPLE_RATE)
    print("Play Audio Complete")
    wav.write(file2write, SAMPLE_RATE, audioRecording)

def saveText2File(text, filename):
    with open(filename, 'w') as f:
        f.write(text)

if __name__ == "__main__":
    recognizeFromMicrophone(FILENAME_FROM_MIC)
    textFromVoice = recognizeFromFile(FILENAME_FROM_MIC)
    saveText2File(textFromVoice, VOICE_TEXT_FILENAME)