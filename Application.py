import streamlit as st
from googletrans import Translator

# Title
st.title("🌍 AI Language Translation Tool")

# Translator object
translator = Translator()

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Japanese": "ja",
    "Chinese": "zh-cn",
    "Portuguese": "pt",
    "Russian": "ru",
    "Urdu": "ur",
    "Bengali": "bn"
}

# Input text
text = st.text_area("Enter text to translate")

# Source language
source_lang = st.selectbox("Select Source Language", list(languages.keys()))

# Target language
target_lang = st.selectbox("Select Target Language", list(languages.keys()))

# Translate button
if st.button("Translate"):

    if text != "":
        translated = translator.translate(
            text,
            src=languages[source_lang],
            dest=languages[target_lang]
        )

        st.success("Translated Text:")
        st.write(translated.text)

        # Copy feature
        st.code(translated.text)

    else:
        st.warning("Please enter some text.")