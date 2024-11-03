import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import tkinter as tk
from tkinter import scrolledtext, messagebox
from PIL import Image, ImageTk
import threading

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
profile_photo = None
profile_image_path = r"C:\Users\3TEE\Pictures\Screenshots\fz.jpg"

try:
    profile_image = Image.open(profile_image_path)
    profile_image = profile_image.resize((100, 80), Image.LANCZOS)
    profile_photo = ImageTk.PhotoImage(profile_image)
    image_label = tk.Label(window, image=profile_photo, bg="#1c1c1c")
    image_label.pack(pady=10)
except FileNotFoundError:
    print("Error: The image file was not found.")
    placeholder_image = Image.new("RGB", (100, 100), "gray")
    profile_photo = ImageTk.PhotoImage(placeholder_image)
    image_label = tk.Label(window, image=profile_photo, bg="#1c1c1c")
    image_label.pack(pady=10)
except Exception as e:
    print(f"Image loading error: {e}")

# Display User Name
user_name = tk.Label(window, text="Faizan Ahmed", font=("Arial", 16, "bold"), bg="#1c1c1c", fg="white")
tk.Label(window, text="Created by", font=("Arial", 8, "bold"), bg="#1c1c1c", fg="white")
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
            display_text("User: " + command)
        except sr.UnknownValueError:
            display_text("Could not understand audio")
            speak("Sorry, I couldn't understand. Please repeat.")
            return "None"
        except sr.RequestError as e:
            display_text(f"Service Error: {e}")
            speak("There seems to be a connection issue.")
            return "None"
        return command.lower()

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

        elif 'open notepad' in command:
            os.system("notepad")
            speak("Opening Notepad")
       
        elif 'sap' in command:
            os.system("\"C:\\Program Files (x86)\\SAP\\FrontEnd\\SAPgui\\saplogon.exe\"")
            speak("Opening SAP")

        elif 'exit' in command:
            speak("Goodbye!")
            window.quit()
            break

def listen_for_activation():
    while True:
        command = take_command()
        if 'aliza' in command:
            assistant()

# Start a thread to listen for activation command
thread = threading.Thread(target=listen_for_activation, daemon=True)
thread.start()

# About Button
def show_info():
    messagebox.showinfo("About", "AI Voice Assistant\nVersion 1.0\nDeveloped by Faizan Ahmed")

info_button = tk.Button(window, text="About", command=show_info, bg="#2ecc71", fg="white", font=("Arial", 10), width=10)
info_button.pack(pady=5)

# Run the GUI
window.mainloop()
