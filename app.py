import streamlit as st
import os
from modules.notes_generator import generate_notes
from modules.audio_extractor import extract_audio
from modules.transcriber import transcribe_audio
from modules.translator import translate_text
from modules.summarizer import generate_summary

# --------------------------------------------------
# Create Required Folders
# --------------------------------------------------
os.makedirs("data/videos", exist_ok=True)
os.makedirs("data/audio", exist_ok=True)
os.makedirs("data/transcripts", exist_ok=True)
os.makedirs("data/summaries", exist_ok=True)

# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------
st.set_page_config(page_title="VideoMentor AI")

st.title("🎥 VideoMentor AI")
st.write("AI-Powered Video Learning Assistant")

# --------------------------------------------------
# Language Mapping
# --------------------------------------------------
languages = {
    "English": "en",
    "Malayalam": "ml",
    "Hindi": "hi",
    "Tamil": "ta",
    "Arabic": "ar",
    "French": "fr"
}

# --------------------------------------------------
# Video Upload Section
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "Upload a Video",
    type=["mp4", "mov", "avi"]
)

if uploaded_file:

    # Save uploaded video
    video_path = os.path.join(
        "data/videos",
        uploaded_file.name
    )

    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("✅ Video uploaded successfully!")

    # Display video
    st.video(uploaded_file)

    # Language Selection
    selected_language = st.selectbox(
        "🌍 Select Translation Language",
        list(languages.keys())
    )

    if st.button("Generate Transcript"):

        # Audio file path
        audio_path = os.path.join(
            "data/audio",
            "audio.wav"
        )

        # ------------------------------------------
        # Step 1: Extract Audio
        # ------------------------------------------
        with st.spinner("🎵 Extracting audio..."):
            extract_audio(video_path, audio_path)

        # ------------------------------------------
        # Step 2: Generate Transcript
        # ------------------------------------------
        with st.spinner("📝 Generating transcript..."):
            transcript = transcribe_audio(audio_path)

        st.subheader("📄 Transcript")

        st.text_area(
            "Transcript",
            transcript,
            height=300
        )

        # Save Transcript
        with open(
            "data/transcripts/transcript.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(transcript)

        # ------------------------------------------
        # Step 3: Translate Transcript
        # ------------------------------------------
        with st.spinner("🌍 Translating transcript..."):
            translated_text = translate_text(
                transcript,
                languages[selected_language]
            )

        st.subheader(
            f"🌐 Translated Transcript ({selected_language})"
        )

        st.text_area(
            "Translation",
            translated_text,
            height=300
        )

        # Save Translation
        with open(
            "data/transcripts/translated.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(translated_text)

        # ------------------------------------------
        # Step 4: Generate AI Summary
        # ------------------------------------------
        with st.spinner("🧠 Generating summary..."):

            # Limit transcript size for now
            summary = generate_summary(
                transcript[:5000]
            )

        st.subheader("📝 Video Summary")

        st.text_area(
            "Summary",
            summary,
            height=250
        )
        #Generating study notes
        with st.spinner("📚 Generating study notes..."):
            notes = generate_notes(
                transcript[:5000]
        )
        # Save Summary
        with open(
            "data/summaries/summary.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(summary)
        #Display study notes    
        st.subheader("📚 Study Notes")
        st.text_area(
            "Notes",
            notes,
            height=400
        )
        #Save study notes
        with open(
            "data/notes/notes.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(notes)
        # ------------------------------------------
        # Completed
        # ------------------------------------------
        st.success(
            "✅ Transcript, Translation, and Summary generated successfully!"
        )