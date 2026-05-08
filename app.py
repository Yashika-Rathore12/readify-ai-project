import streamlit as st
from PIL import Image
import pytesseract
from gtts import gTTS
import os

st.title("📖 Readify AI: OCR to Speech")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image", use_column_width=True)

    extracted_text = pytesseract.image_to_string(image)

    st.subheader("Extracted Text")
    st.write(extracted_text)

    if extracted_text.strip() != "":
        tts = gTTS(text=extracted_text, lang='en')
        tts.save("output.mp3")

        audio_file = open("output.mp3", "rb")
        audio_bytes = audio_file.read()

        st.subheader("Audio Output")
        st.audio(audio_bytes, format='audio/mp3')
