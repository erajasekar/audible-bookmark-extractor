import whisper

model = whisper.load_model("medium")
result = model.transcribe("clips/the_art_of_thinking_clearly-bak/clip11.flac")
print(result["text"])
