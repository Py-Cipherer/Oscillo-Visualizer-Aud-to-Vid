Firstly Download FFmpeg before hitting *requirements.txt*

Go to:
👉 https://www.gyan.dev/ffmpeg/builds/

Download “ffmpeg-release-essentials.zip”

Extract it to:

C:\ffmpeg

You should now have:

C:\ffmpeg\bin\ffmpeg.exe

✅ Add FFmpeg to PATH

Press Win + R → type sysdm.cpl

Advanced → Environment Variables

Under System Variables

Select Path → Edit → New

Add:

C:\ffmpeg\bin


OK → OK → OK

RESTART CMD (very important)

✅ Verify: Open new command prompt:

*ffmpeg -version*

⚠️ Notes (important)


* Do NOT add ffmpeg in requiements.txt (pip installation) → system-level only
* torch is required by Whisper
* This works with Python 3.10
* Stable on Windows
* Works fine in your oculus-env venv



📦 Install command



pip install -r requirements.txt

🛹 Steps

* Place the audio file as "input.m4a" (audio formats- .wav , .m4a , .mp3 , etc) in the audio folder.
* run the "transcribe.py" -> will create a transcript file.
* run the "audio_energy.py" -> will generate an  energy.npy file.
* finally run the "main.py" to start the generation.
* Upon completion you will get a "generation.mp4" file in same folder as the main.py
* *Make sure all the folders and directories are as is in this repository. Maintain the file structure.*
