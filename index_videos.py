import os
import glob
import whisper
from pathlib import Path
import json

model = whisper.load_model("base")
audio_path = "audio"
transcript_path = "transcripts"

for file in sorted(glob.glob(f"audio/**/*.mp3", recursive=True)):
    file_name = os.path.basename(file)
    out_dir = os.path.join(transcript_path, os.path.dirname(file))
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    out_path = os.path.join(out_dir, file_name.replace(".mp3", ".json"))

    if os.path.exists(out_path):
        print(f"Skipping {file_name}")
        continue
    
    print(f"Transcribing {file_name}")
    result = model.transcribe(file, verbose=True)
    with open(out_path, "w") as f:
        f.write(json.dumps(result, indent=4))