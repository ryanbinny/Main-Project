import streamlit as st
from src.audio_processing import record_audio, preprocess_audio, save_processed_audio
from src.transcription import transcribe
from src.entity_extraction import extract_entities
from src.map_utils import get_location_data, find_nearest_places, generate_folium_map
from src.emotion_detection import detect_emotion
from streamlit_folium import st_folium


def main():
    # Set page configuration
    st.set_page_config(page_title="Help Line AI", page_icon="🎙️", layout="wide")

    # Page title
    st.title("🚨 Help Line AI: Audio Analysis and Assistance")

    # Sidebar
    st.sidebar.title("Navigation")
    st.sidebar.markdown("Use the sections below to interact with the app:")
    options = ["Home", "Audio Input", "Emotion & Transcription", "Map Assistance"]
    choice = st.sidebar.radio("Go to:", options)

    # Initialize session state variables
    if "uploaded_file" not in st.session_state:
        st.session_state.uploaded_file = None
    if "entities" not in st.session_state:
        st.session_state.entities = {}

    if choice == "Home":
        st.header("Welcome to Help Line AI!")
        st.write(
            """
            This app analyzes audio input to detect emotions, transcribe speech, and provide assistance based on detected locations. 
            Here's what you can do:
            - Record or upload audio to analyze.
            - Detect emotions and assign priority levels.
            - Transcribe speech for further insights.
            - Locate nearby facilities (e.g., hospitals) based on extracted locations.
            """
        )
        st.info("Use the sidebar to navigate between sections.")

    elif choice == "Audio Input":
        st.header("🎤 Audio Input")
        st.write("Record live audio or upload a file for analysis.")

        # Record Audio
        if st.button("Record Live Audio"):
            record_audio("recorded_audio.wav")
            st.session_state.uploaded_file = "recorded_audio.wav"
            st.success("Recording complete. File saved as `recorded_audio.wav`.")

        # Upload Audio File
        uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "flac", "m4a"])
        if uploaded_file:
            st.session_state.uploaded_file = uploaded_file
            st.success("Audio file uploaded successfully.")

        # Display uploaded audio
        if st.session_state.uploaded_file:
            st.audio(st.session_state.uploaded_file, format="audio/wav")
            audio_array, sampling_rate = preprocess_audio(st.session_state.uploaded_file)
            save_processed_audio(audio_array, sampling_rate, "temp_audio.wav")
            st.info("Audio file preprocessed and ready for analysis.")

    elif choice == "Emotion & Transcription":
        st.header("📋 Emotion Detection & Transcription")
        st.write("Analyze the uploaded or recorded audio for emotion and transcription.")

        if st.session_state.uploaded_file:
            # Emotion Detection
            emotion, priority = detect_emotion("temp_audio.wav")
            st.subheader("🎭 Detected Emotion:")
            st.write(f"**Emotion:** {emotion}")
            st.write(f"**Priority Level:** {priority}")

            # Transcription
            transcription = transcribe("temp_audio.wav", is_file=True)
            st.subheader("📝 Transcription:")
            st.text_area("Transcription:", transcription, height=200)

            # Entity Extraction
            entities = extract_entities(transcription)
            st.session_state.entities = entities
            st.subheader("🔍 Extracted Entities:")
            st.write(entities)
        else:
            st.warning("Please upload or record an audio file in the 'Audio Input' section.")

    elif choice == "Map Assistance":
        st.header("📍 Map Assistance")
        st.write("Find nearby facilities based on extracted locations.")

        if st.session_state.entities and "Location" in st.session_state.entities:
            location_name = ", ".join(st.session_state.entities.get("Location", []))
            st.info(f"Extracted location(s): {location_name}")

            location_data = get_location_data(location_name)
            if location_data.get("results"):
                lat = location_data["results"][0]["geometry"]["location"]["lat"]
                lon = location_data["results"][0]["geometry"]["location"]["lng"]

                # Find Nearby Places
                places = find_nearest_places(lat, lon, "hospital")
                st.subheader("Nearby Facilities:")
                if places:
                    for place in places:
                        st.write(f"- **{place['name']}**: {place.get('vicinity', 'Address not available')}")
                else:
                    st.warning("No nearby facilities found.")

                # Display Map
                fmap = generate_folium_map(lat, lon, places)
                st_folium(fmap, width=800, height=600)
            else:
                st.error("No location data found for the extracted entities.")
        else:
            st.warning("No location entities detected. Please analyze audio in the 'Emotion & Transcription' section.")


if __name__ == "__main__":
    main()
