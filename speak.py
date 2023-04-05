# make start and save , user input gates
# make a timestamp for the saved document to dynamically generate names
#refactor the filename so it doesn't add new transcripts for each chunk, but just adds to the same file per session

# --------------------
# import speech_recognition as sr
# from docx import Document

# r = sr.Recognizer()
# with sr.Microphone() as source:
#     print("Press 's' to start recording and 'x' to stop recording:")
#     while True:
#         audio = r.listen(source)
#         try:
#             text = r.recognize_google(audio)
#             print("You said: {}".format(text))
#             save_transcript = input("Do you want to save this transcript? (y/n): ")
#             if save_transcript.lower() == "y":
#                 # Save the transcript to a file
#                 with open("transcript.txt", "a") as f:
#                     f.write(text + "\n")
#             else:
#                 continue
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#         except sr.RequestError as e:
#             print("Could not request results from Google Speech Recognition service; {0}".format(e))
#         if input("Press 's' to start recording again or any other key to quit: ") != 's':
#             break

import speech_recognition as sr
from docx import Document
import pyperclip
import datetime

r = sr.Recognizer()
document = Document()

timestamp = datetime.datetime.now().strftime("%m-%d-%H-%M-%S")
filename = f"transcript_{timestamp}.docx"

while True:
    with sr.Microphone() as source:
        if input("Press 's' to start recording and 'x' to stop recording:") != 's':
            break
        print("Listening...")
        audio = r.listen(source)

        try:
            print("Processing audio ...")
            text = r.recognize_google(audio)
            print(f"Text playback: {text}")
            pyperclip.copy(text)
            save_transcript = input("Do you want to save this transcript? (y/n): ")

            if save_transcript.lower() == "y":
                # Save the transcript to a Word document with timestamp in the filename
                document.add_paragraph(text)
                document.save(filename)
                print(f"Transcript saved to {filename}")
            else:
                continue

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            break

