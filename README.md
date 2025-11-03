Emotional Speech Generation Prototype


Setup instruction:
Installed Python 3.9+ is recommended.

Requirements:
pip install pyttsx3 librosa soundfile

Liblary Notes:
pyttsx3 — offline text-to-speech engine (uses system voices).
librosa — for pitch and tempo manipulation.
soundfile — to save processed audio back to .wav.


How to run:
python solution.py "<text>" <output.wav> [emotion]

Example:
Default: Neutral
python solution.py "Hello world" neutral.wav 

Happy:
python solution.py "Hello world" happy.wav happy

Sad: 
python solution.py "Hello world" sad.wav sad

Angri:
python solution.py "Hello world" angri.wav angri

Serious:
python solution.py "Hello world" serious.wav serious


Output:
Output file .wav will create on the same directory solution.py