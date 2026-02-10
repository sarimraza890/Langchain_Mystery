from stage1_audio.pipeline import transcribe
from stage2_docs.pipeline import load_docs, extract_fact, merge_facts
from stage3_reasoning.pipeline import reason


print("Running Stage 1: Audio Transcription")
transcript = transcribe("story_audio.mp3", "story_case")
print("Transcript created successfully")

print("Running Stage 2: Document Extraction")
docs = load_docs("mystery_story.pdf")
facts = [extract_fact(doc) for doc in docs]
merged_facts = merge_facts(facts)
print("Facts extracted successfully")

print("Running Stage 3: Reasoning")
final_answer = reason(merged_facts)

print("\n===== FINAL OUTPUT =====")
print(final_answer)
