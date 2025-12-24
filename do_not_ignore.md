⚠️ Notes (important)



* Do NOT add ffmpeg in requiements.txt (pip installation) → system-level only
* torch is required by Whisper
* This works with Python 3.10
* Stable on Windows
* Works fine in your oculus-env venv



📦 Install command



pip install -r requirements.txt

Steps:-

* Place the audio file as "input.m4a" (audio formats- .wav , .m4a , .mp3 , etc) in the audio folder.
* run the "transcribe.py" -> will create a transcript file.
* run the "audio_energy.py" -> will generate an  energy.npy file.
* finally run the "main.py" to start the generation.
Upon completion you will get a "generation.mp4" file in same folder as the main.py
