from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2Processor
import librosa
import torch
import numpy as np
import streamlit as st

# Load model and processor
MODEL_PATH = "emotion_model"
processor = Wav2Vec2Processor.from_pretrained(MODEL_PATH)
model = Wav2Vec2ForSequenceClassification.from_pretrained(MODEL_PATH, ignore_mismatched_sizes=True)

# Manually set label mappings
model.config.id2label = {
    0: "Happy",
    1: "Neutral",
    2: "Sad",
    3: "Angry",
    4: "Fearful",
}
model.config.label2id = {v: k for k, v in model.config.id2label.items()}

# Emotion to priority mapping
EMOTION_PRIORITY = {
    "Happy": "Low",
    "Neutral": "Moderate",
    "Sad": "High",
    "Angry": "Serious",
    "Fearful": "Critical",
}


def detect_emotion(audio_path: str) -> (str, str):
    """
    Detects the emotion from an audio file and assigns a priority level.

    Args:
        audio_path (str): Path to the audio file.

    Returns:
        (emotion, priority): Detected emotion and its priority level.
    """
    try:
        # Load and preprocess audio
        audio_array, sampling_rate = librosa.load(audio_path, sr=16000)
        input_values = processor(audio_array, sampling_rate=16000, return_tensors="pt", padding=True).input_values

        # Perform inference
        with torch.no_grad():
            logits = model(input_values).logits
            probabilities = torch.nn.functional.softmax(logits, dim=-1).numpy()
            emotion_idx = np.argmax(probabilities)
            emotion = model.config.id2label.get(emotion_idx, f"LABEL_{emotion_idx}")

        # Determine priority level
        priority = EMOTION_PRIORITY.get(emotion, "Unknown")
        return emotion, priority
    except Exception as e:
        st.error(f"Error in emotion detection: {str(e)}")
        return "Error", "Unknown"
