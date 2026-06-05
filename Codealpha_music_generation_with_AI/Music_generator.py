import streamlit as st
import os

st.set_page_config(
    page_title="AI Music Generator",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 AI Music Generation System")
st.markdown("Generate original music using a trained LSTM neural network.")


num_notes = st.slider(
    "Number of Notes",
    100,
    200,
    150
)

creativity = st.selectbox(
        "Creativity Level",
        ["Low", "Medium", "High"]
)

st.divider()

if st.button("🎼 Generate Music"):

    with st.spinner("Generating music..."):
        os.system("python generate.py")

    st.success("Music Generated Successfully!")

    if os.path.exists("generated_music.mid"):

        st.download_button(
            "⬇ Download MIDI",
            open("generated_music.mid", "rb"),
            file_name="generated_music.mid"
        )

        st.subheader("Generate Original Music with AI")

st.info(
    "This project uses LSTM Neural Networks trained on MIDI datasets."
)
