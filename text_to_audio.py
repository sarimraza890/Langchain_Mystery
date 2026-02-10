from gtts import gTTS

with open("transcript.txt", "r", encoding="utf-8") as f:
    text = f.read()

tts = gTTS(text=text, lang="en")
tts.save("story_audio.mp3")

print("Audio saved as story_audio.mp3")
