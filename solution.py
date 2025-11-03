#liblary import

import sys
#pyttsx3 — offline text-to-speech engine
import pyttsx3
#for pitch and tempo manipulation.
import librosa
#to save processed audio back to .wav.
import soundfile as sf
import os

def convert_speech(text, result, emotion):
    # handle empty input
    if not text.strip():
        print("Error: Input text is empty.")
        return
    # handle other output except .wav
    if not result.endswith(".wav"):
        print("Error: Output file must end with .wav")
        return

    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, result)
        engine.runAndWait()
        print(f"Convert success and audio saved: {result}")

        # Apply simple emotional effects
        if emotion.lower() != "neutral":
            y, sr = librosa.load(result)
            print(f"Check input voice emotion: {emotion.lower()}")

            if emotion.lower() == "happy":
                # Faster tempo, higher pitch
                print(f"Convert to happy voice")
                y = librosa.effects.time_stretch(y=y, rate=1.15)
                y = librosa.effects.pitch_shift(y, sr=sr, n_steps=2)
            elif emotion.lower() == "sad":
                # Slower tempo, lower pitch
                print(f"Convert to sad voice")
                y = librosa.effects.time_stretch(y=y, rate=0.8)
                y = librosa.effects.pitch_shift(y, sr=sr, n_steps=-2)
            elif emotion.lower() == "angry":
                # Slower tempo, lower pitch
                print(f"Convert to angry voice")
                y = librosa.effects.time_stretch(y=y, rate=1.1)
                y = librosa.effects.pitch_shift(y, sr=sr, n_steps=2)
            elif emotion.lower() == "serious":
                # Slower tempo, lower pitch
                print(f"Convert to serious voice")
                y = librosa.effects.time_stretch(y=y, rate=0.95)
                y = librosa.effects.pitch_shift(y, sr=sr, n_steps=1)


            sf.write(result, y, sr)
            print(f"Applied '{emotion}' style effect")

    except Exception as e:
        print(f"Error Message: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python solution.py \"<text>\" <output.wav> [emotion]")
    else:
        # handle input command line
        text = sys.argv[1]
        result = sys.argv[2]
        emotion = sys.argv[3] if len(sys.argv) > 3 else "neutral"
        convert_speech(text, result, emotion)
