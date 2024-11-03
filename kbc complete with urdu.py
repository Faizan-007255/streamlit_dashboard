from gtts import gTTS
import playsound
import os
import random

def speak(text=None, lang='en', custom_audio=None):
    """Speaks the given text in the specified language (default is English)."""
    try:
        if custom_audio:
            # Play the custom audio file if provided
            playsound.playsound(custom_audio)
        else:
            # Use gTTS to generate and play text if no custom audio is given
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

# Play KBC start sound at the beginning of the game
speak(custom_audio="D:\\KBC\\kbc_5_newest.mp3")
speak(custom_audio="D:\\KBC\\KBCS.mp3")

# Example usage
Eq = input("Question List NO (Enter 'Q1', 'Q2', or 'Q3'): ")

# Define the questions in English and Urdu
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

# Check the question selected by the user
if Eq in questions:
    print(questions[Eq]["en"])
    speak(questions[Eq]["en"], lang='en')  # Voice feedback in English
    
    print(questions[Eq]["ur"])
    speak(questions[Eq]["ur"], lang='ur')  # Voice feedback in Urdu
    speak(custom_audio="D:\\KBC\\clock.mp3")
    # Get the answer
    a = input("Your Answer: ")

    # Example for checking answers
    if (Eq == "Q1" and a.upper() == "D"):  # Question 1 correct answer check
        response = "This is the Correct Answer. You win 10000 PKR."
        response_ur = "یہ صحیح جواب ہے۔ آپ 10000 PKR جیت گئے ہیں۔"
        print(response)
        print(response_ur)

        speak(response, lang='en')
        speak(response_ur, lang='ur')
    elif (Eq == "Q2" and a.upper() == "A"):  # Question 2 correct answer check
        response = "This is the Correct Answer. You win 25000 PKR."
        response_ur = "2یہ صحیح جواب ہے۔ آپ 5000 PKR جیت گئے ہیں۔"
        print(response)
        print(response_ur)
        speak(response, lang='en')
        speak(response_ur, lang='ur')
    elif (Eq == "Q3" and a.upper() == "A"):  # Question 3 correct answer check
        response = "This is the Correct Answer. You win 50000 PKR."
        response_ur = "یہ صحیح جواب ہے۔ آپ 50000 PKR جیت گئے ہیں۔"
        print(response)
        print(response_ur)
        speak(response, lang='en')
        speak(response_ur, lang='ur')
    else:
        response = "This is the Wrong Answer."
        response_ur = "یہ غلط جواب ہے۔"
        print(response)
        print(response_ur)
        speak(response, lang='en')
        speak(response_ur, lang='ur')
else:
    response = "Invalid question number. Please enter 'Q1', 'Q2', or 'Q3'."
    print(response)
    speak(response, lang='en')
