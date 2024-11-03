from gtts import gTTS
import playsound
import os
import random

def speak(text, lang='en', custom_audio=None):
    """Speaks the given text in the specified language, or plays a custom audio file if provided."""
    try:
        if custom_audio:
            # Play the custom audio file
            playsound.playsound(custom_audio)
        else:
            # Use gTTS to generate and play text if no custom audio is given
            output_dir = "D:\\KBC"
            os.makedirs(output_dir, exist_ok=True)
            file_name = f"output_{random.randint(1000, 9999)}.mp3"
            file_path = os.path.join(output_dir, file_name)
            tts = gTTS(text=text, lang=lang)
            tts.save(file_path)
            playsound.playsound(file_path)
            os.remove(file_path)  # Optional: delete after playing
    except Exception as e:
        print(f"An error occurred while trying to speak: {e}")

# Example usage
Eq = input("Question List NO (Enter 'Q1', 'Q2', or 'Q3'): ")

# Define questions
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
    # Add other questions as needed
}

# Check selected question
if Eq in questions:
    print(questions[Eq]["en"])
    speak(questions[Eq]["en"], lang='en')

    print(questions[Eq]["ur"])
    speak(questions[Eq]["ur"], lang='ur')

    # Get the answer
    a = input("Your Answer: ")

    # Check answers with custom audio responses
    if Eq == "Q1" and a.upper() == "D":
        print("This is the Correct Answer. You win 5000 PKR.")
        speak(None, custom_audio="D:/KBC/correct_answer.mp3")
    else:
        print("This is the Wrong Answer.")
        speak(None, custom_audio="D:/KBC/wrong_answer.mp3")
else:
    print("Invalid question number. Please enter 'Q1', 'Q2', or 'Q3'.")
    speak(None, custom_audio="D:/KBC/invalid_question.mp3")
