import os
from deepgram import DeepgramClient

dg = DeepgramClient(api_key=os.getenv("DEEPGRAM_API_KEY"))

def transcribe(audio_path: str, case_id: str):
    with open(audio_path, "rb") as audio:
        buffer_data = audio.read()

    response = dg.listen.v1.media.transcribe_file(
        request=buffer_data,
        model="nova-2",
        smart_format=True
    )

    transcript = response.results.channels[0].alternatives[0].transcript

    os.makedirs("outputs", exist_ok=True)
    out_path = f"outputs/{case_id}_transcript.txt"

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(transcript)

    return transcript
