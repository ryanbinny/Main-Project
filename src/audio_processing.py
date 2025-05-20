import librosa
import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import wave

def record_audio(file_name: str, duration: int = 10, sampling_rate: int = 16000):
    audio_data = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1, dtype='int16')
    sd.wait()
    with wave.open(file_name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sampling_rate)
        wf.writeframes(audio_data.tobytes())

def preprocess_audio(file, target_sr=16000):
    audio_array, original_sr = librosa.load(file, sr=None)
    if original_sr != target_sr:
        audio_array = librosa.resample(audio_array, orig_sr=original_sr, target_sr=target_sr)
    audio_array = librosa.util.normalize(audio_array)
    return audio_array, target_sr

def save_processed_audio(audio_array, sr, output_path="processed_audio.wav"):
    write(output_path, sr, (audio_array * 32767).astype(np.int16))
