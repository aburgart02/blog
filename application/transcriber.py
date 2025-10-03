import torch
from faster_whisper import WhisperModel

device = "cuda" if torch.cuda.is_available() else "cpu"
compute_type = "int8_float16" if device == "cuda" else "int8"
model_size = "large-v3"

try:
    print(f"Loading model '{model_size}' on device '{device}' with compute_type '{compute_type}'...")
    model = WhisperModel(model_size, device=device, compute_type=compute_type)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None


def transcribe_audio_file(audio_file_path):
    if model is None:
        raise RuntimeError("Whisper model is not loaded.")

    segments, info = model.transcribe(audio_file_path, beam_size=5, language='ru')

    full_text = []
    for segment in segments:
        full_text.append(segment.text)

    return "".join(full_text).strip()