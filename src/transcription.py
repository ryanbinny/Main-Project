import os
import whisper
from rich.console import Console

console = Console()

# Load the Whisper model (base, small, medium, or large)
model = whisper.load_model("large")

def transcribe(audio, is_file=True, language_code="en") -> str:
    try:
        # Load audio data
        if is_file:
            audio_path = audio
        else:
            # Save the raw audio content to a temporary file if not a file
            audio_path = "temp_audio.wav"
            with open(audio_path, "wb") as temp_file:
                temp_file.write(audio)

        # Perform the transcription
        result = model.transcribe(audio_path, language=language_code)

        # Extract and return the transcription text
        text = result.get("text", "").strip()
        if text:
            return text
        else:
            console.print("[yellow]No transcription results were returned.")
            return ""
    except Exception as e:
        console.print(f"[red]Failed to transcribe audio: {str(e)}")
        return ""
    finally:
        # Cleanup the temporary file if created
        if not is_file and os.path.exists(audio_path):
            os.remove(audio_path)

