import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk  # Ensure Pillow library is installed

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# GUI Setup
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("600x600")
window.configure(bg="#1c1c1c")

# Load and display profile picture
profile_image = None
profile_photo = None  # Initialize PhotoImage variable
profile_image_path = r"C:\Users\3TEE\Pictures\Screenshots\fz.jpg"

# Attempt to load the profile image
try:
    profile_image = Image.open(profile_image_path)
    profile_image = profile_image.resize((100, 80), Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
    profile_photo = ImageTk.PhotoImage(profile_image)
    image_label = tk.Label(window, image=profile_photo, bg="#1c1c1c")
    image_label.pack(pady=10)
except FileNotFoundError:
    print("Error: The image file was not found.")
    # Create a placeholder image if file is not found
    placeholder_image = Image.new("RGB", (100, 100), "gray")
    profile_photo = ImageTk.PhotoImage(placeholder_image)
    image_label = tk.Label(window, image=profile_photo, bg="#1c1c1c")
    image_label.pack(pady=10)
except Exception as e:
    print(f"Image loading error: {e}")
 


# Display User Name
user_name = tk.Label(window, text="Faizan Ahmed", font=("Arial", 16, "bold"), bg="#1c1c1c", fg="white")
tk.Label(window, text="Create by", font=("Arial", 8, "bold"), bg="#1c1c1c", fg="white")
user_name.pack(pady=5)

# Output Text Area
output_text = scrolledtext.ScrolledText(window, width=70, height=15, wrap=tk.WORD, font=("Arial", 10), bg="#333", fg="white")
output_text.pack(pady=10)
output_text.configure(state='disabled')

def display_text(text):
    output_text.configure(state='normal')
    output_text.insert(tk.END, text + "\n")
    output_text.configure(state='disabled')
    output_text.yview(tk.END)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    display_text("Assistant: " + text)

def take_command():
    with sr.Microphone() as source:
        display_text("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
        try:
            display_text("Recognizing...")
            command = recognizer.recognize_google(audio)
            display_text(f"User said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            display_text("Could not understand audio")
            return "None"
        except sr.RequestError as e:
            display_text(f"Service Error: {e}")
            return "None"

def assistant():
    speak("How can I assist you today?")
    while True:
        command = take_command()
        if command == "None":
            continue

        if 'youtube' in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
        elif 'time' in command:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")
        elif 'google' in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
        elif 'sap' in command:
            os.system("\"C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplogon.exe\"")
            speak("Opening SAP")
        elif 'open notepad' in command:
            os.system("notepad")
            speak("Opening Notepad")
        elif 'exit' in command:
            speak("Goodbye!")
            break
        else:
            speak("Sorry, I didn't catch that.")

def listen_for_activation():
    while True:
        command = take_command()
        if 'fb' in command:  # Check for the activation word
            assistant()  # Start the assistant if "Aliza" is detected

# Run the activation listener in a separate thread
import threading
activation_thread = threading.Thread(target=listen_for_activation, daemon=True)
activation_thread.start()

# Start Button
start_button = tk.Button(window, text="Start Assistant", command=assistant, bg="#3498db", fg="white", font=("Arial", 12), width=15)
start_button.pack(pady=15)

# About Button
def show_info():
    messagebox.showinfo("About", "AI Voice Assistant\nVersion 1.0\nDeveloped by Faizan Ahmed")

info_button = tk.Button(window, text="About", command=show_info, bg="#2ecc71", fg="white", font=("Arial", 10), width=10)
info_button.pack(pady=5)
# Run the GUI
window.mainloop()
