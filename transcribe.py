import whisper
import json

model = whisper.load_model("base")

result = model.transcribe(
    "audio/input.m4a",
    task="transcribe",
    fp16=False)

with open("captions/transcript.json", "w", encoding="utf-8") as f:
    json.dump(result["segments"], f, ensure_ascii=False, indent=2)

print("Transcription done")
