import whisper

def transcribe_audio(file_path, model_size="small"):
    model = whisper.load_model(model_size)
    result = model.transcribe(file_path)
    return result["text"]

# Usage
print(transcribe_audio("./sample speech audio/sample2.mp3"))

# | Model  | Speed    | Accuracy  |
# | ------ | -------- | --------- |
# | tiny   | Fastest  | Low       |
# | base   | Fast     | Decent    |
# | small  | Balanced | Good      |
# | medium | Slower   | Very Good |
# | large  | Slowest  | Best      |