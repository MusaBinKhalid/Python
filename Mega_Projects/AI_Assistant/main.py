#PLUTO 1.0

import speech_recognition as sr     # For recognizing speech input
import webbrowser                   # For opening websites
import pyttsx3                      # For text-to-speech functionality
import os                           # For interacting with the operating system
import random                       # For choosing random files (music)
import pyautogui                    # For simulating keyboard actions
import pyjokes                      # For fetching random programming jokes
from openai import OpenAI           # For AI response from OpenAI

music_folder = r"ADD_FOLDER_PATH"   # Path to your music folder (update this with the actual path)

recognizer = sr.Recognizer()        # Create a Recognizer instance
engine = pyttsx3.init()             # Initialize text-to-speech engine

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    client = OpenAI(
    api_key="YOUR_API_KEY"          # Replace with your OpenAI API key
    )
    completion = client.chat.completions.create(
        model = "gpt-3.5-turbo",    # Using GPT-3.5 Turbo model
        messages=[
            {"role": "system", "content": "You are a Virtual assistant like Jarvis from ironman but named Pluto. talk like humans and make sure to keep you answers short and simple like a human response!"},
            {"role": "user", "content" : command}
        ]
    )
    return(completion.choices[0].message)       # Extracting the AI response

def processCommand(c):
    print("Command:", c)
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://google.com")
        
    elif "open whatsapp" in c:
        webbrowser.open("https://web.whatsapp.com")
        
    elif "open telegram" in c:
        webbrowser.open("https://web.telegram.org/a/")
        
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")

    elif "play music" in c:
        try:
            songs = [file for file in os.listdir(music_folder) if file.endswith((".mp3", ".wav"))]
            if songs:
                song = random.choice(songs)                         # Pick a random song
                song_path = os.path.join(music_folder, song)        # Path to the song
                os.startfile(song_path)                             # Play the song
                speak(f"Playing {song}")
        except Exception as e:
            print("Music Error:", e)
            speak("Well sir, it seems silence wins this round.")

    elif "message" in c or "search" in c or "type" in c:
        try:
            text_to_type = c.replace("type", "").replace("message", "").replace("search", "").strip()
            if text_to_type:
                pyautogui.write(text_to_type, interval=0.05)        # Simulate Typing
                pyautogui.press('enter')                            # Press 'Enter' after Typing
            else:
                speak("You said type, but didn't say what to type.")
        except Exception as e:
            print("Typing Error:", e)
            speak("Well sorry sir. That didn’t work.")

    elif "joke" in c or "tell a joke" in c:
        try:
            joke = pyjokes.get_joke()
            speak(joke)
            print(joke)
        except Exception as e:
            print("Joke Error", e)
            speak("Well sorry sir. That didn’t work.")

    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Hello Sir. Pluto Online")

    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)           # Reduce noise
                print("Listening for 'Pluto' command...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=3)   # Listen for audio input

            speech = recognizer.recognize_google(audio)                             # Convert speech to text
            print("Heard:", speech)

            if "pluto" in speech.lower():                                           # Activate only if "pluto" is heard
                command = speech.lower().replace("pluto", "").strip()
                if command:
                    speak("Yes Sir")
                    processCommand(command)                                         # Execute the command
                else:
                    speak("Waiting for your command. Sir")
        except Exception as e:
            print("Error:", e)