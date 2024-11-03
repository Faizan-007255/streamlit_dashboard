import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import playsound
import os
import random
import speech_recognition as sr

# Initialize the speech recognizer
recognizer = sr.Recognizer()


def speak(text=None, lang='en', custom_audio=None):
    """Speaks the given text in the specified language (default is English)."""
    try:
        if custom_audio:
            playsound.playsound(custom_audio)
        else:
            output_dir = "D:\\KBC"
            os.makedirs(output_dir, exist_ok=True)  # Ensure directory exists
            file_name = f"output_{random.randint(1000, 9999)}.mp3"
            file_path = os.path.join(output_dir, file_name)
            tts = gTTS(text=text, lang=lang)
            tts.save(file_path)           # Save the audio file
            playsound.playsound(file_path)  # Play the audio file
            os.remove(file_path)          # Optional: delete after playing
    except Exception as e:
        print(f"An error occurred while trying to speak: {e}")

def listen():
    """Uses SpeechRecognition to capture voice input from the user."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text.upper()  # Convert to uppercase for comparison
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return None
    except sr.RequestError:
        print("Error with the recognition service")
        return None

def start_game():
    """Starts the quiz game."""
    speak(custom_audio="D:\\KBC\\kbc_5_newest.mp3")
    speak("Please say the question number as Q1, Q2, or Q3.")
    Eq = listen()
    valid_answers = ["Q1", "Q2", "Q3"]
    if Eq not in valid_answers:
        Eq = input( ":" )
    else:
         Eq = "Q1"

    # Display the question number in the GUI
    question_label.config(text=f"You selected: {Eq}")  # Display the question number

    questions = {
        "Q1": {
            "en": '''Q1: Which Pakistan Province is the largest by area?
A: Sindh
B: Punjab
C: Khyber Pakhtunkhwa
D: Balochistan''',
            "ur": '''سوال 1: پاکستان کا سب سے بڑا صوبہ کون سا ہے؟
A: سندھ
B: پنجاب
C: خیبر پختونخوا
D: بلوچستان'''
        },
        "Q2": {
            "en": '''Q2: Who is the founder of Pakistan?
A: Muhammad Ali Jinnah
B: Liaquat Ali Khan
C: Allama Iqbal
D: Sir Syed Ahmed Khan''',
            "ur": '''سوال 2: پاکستان کے بانی کون ہیں؟
A: محمد علی جناح
B: لیاقت علی خان
C: علامہ اقبال
D: سر سید احمد خان'''
        },
        "Q3": {
            "en": '''Q3: What is the national language of Pakistan?
A: Urdu
B: English
C: Punjabi
D: Sindhi''',
            "ur": '''سوال 3: پاکستان کی قومی زبان کیا ہے؟
A: اردو
B: انگریزی
C: پنجابی
D: سندھی'''
        },
    }

    if Eq in questions:
        question_en = questions[Eq]["en"]
        question_ur = questions[Eq]["ur"]

        # Display question in GUI before speaking
        question_label.config(text=f"Question: {question_en}\n{question_ur}")
        #window.mainloop()
        
        # Speak the question after displaying
        speak(question_en, lang='en')
        speak(question_ur, lang='ur')

        
        

        # Ask for answer
        speak("Please say your answer.")
        window.mainloop()
        speak(custom_audio="D:\\KBC\\clock.mp3")
        answer = listen()
        
        # Check answers and respond
        if (Eq == "Q1" and answer == "D") or (Eq == "Q2" and answer == "A") or (Eq == "Q3" and answer == "A"):
            response = "This is the Correct Answer."
            response_ur = "یہ صحیح جواب ہے۔"
            print(answer)
        else:
            response = "This is the Wrong Answer."
            response_ur = "یہ غلط جواب ہے۔"
            print(answer)

        # Display the response in the GUI first
       # question_label.config(text=f"Question: {question_en}\n{question_ur}")
       # response_label.config(text=f"Response: {response}\n{response_ur}")

        # Speak the response in English first
        speak(response, lang='en')
        
        # Speak the response in Urdu after English
        speak(response_ur, lang='ur')
    else:
        messagebox.showinfo("Error", "Invalid question number. Please enter 'Q1', 'Q2', or 'Q3'.")
        


# GUI Setup
window = tk.Tk()
window.title("KBC Quiz Game")
window.geometry("400x300")

window.configure(bg="lightblue")

frame = tk.Frame(window, bg="lightblue")
frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

text_label = tk.Label(frame, text="Welcome to KBC Quiz Game!", bg="lightblue", fg="black", font=("Arial", 14))
text_label.pack(pady=20)

# Question Display
question_label = tk.Label(window, text="", font=("Arial", 12), wraplength=350, justify="left")
question_label.pack(pady=10)

# Response Display
response_label = tk.Label(window, text="", font=("Arial", 12), wraplength=350, justify="left")
response_label.pack(pady=10)

# Start Button
start_button = tk.Button(window, text="Start Quiz", command=start_game, font=("Arial", 14), bg="#4CAF50", fg="white")
start_button.pack(pady=50)

# Run the GUI
window.mainloop()
