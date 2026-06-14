import streamlit as st
import os

from modules.audio_extractor import extract_audio
from modules.transcriber import transcribe_audio

st.set_page_config(page_title="VideoMentor AI")

st.title("🎥 VideoMentor AI")
st.write("AI-Powered Video Learning Assistant")

uploaded_file = st.file_uploader(
    "Upload a Video",
    type=["mp4", "mov", "avi"]
)

if uploaded_file:

    video_path = os.path.join(
        "data/videos",
        uploaded_file.name
    )

    with open(video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Video uploaded successfully!")

    if st.button("Generate Transcript"):

        audio_path = os.path.join(
            "data/audio",
            "audio.wav"
        )

        with st.spinner("Extracting audio..."):
            extract_audio(video_path, audio_path)

        with st.spinner("Transcribing..."):
            transcript = transcribe_audio(audio_path)

        st.subheader("Transcript")

        st.write(transcript)

        with open(
            "data/transcripts/transcript.txt",
            "w",
            encoding="utf-8"
        ) as f:
            f.write(transcript)