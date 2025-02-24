import streamlit as st
import requests
import base64

def main():
    st.set_page_config(
        page_title="Kalika FM Streamer",
        page_icon="🎵",
        layout="centered"
    )

    # Header
    st.title("Kalika FM - Live Stream")
    st.markdown("### Bharatpur-10, Chitwan, Nepal")

    # Stream URL
    STREAM_URL = "https://streaming.softnep.net:10828/;stream.nsv&type=mp3&volume=70"

    # Audio player
    st.markdown(
        f"""
        <audio controls style="width: 100%;">
            <source src="{STREAM_URL}" type="audio/mpeg">
            Your browser does not support the audio element.
        </audio>
        """,
        unsafe_allow_html=True
    )

    # Additional Information
    with st.expander("About Kalika FM"):
        st.write("""
        Kalika FM is a radio station broadcasting from Bharatpur, Chitwan, Nepal. 
        Listen to live news, music, and entertainment programming.
        """)

    # Stream Status
    if st.button("Check Stream Status"):
        try:
            response = requests.head(STREAM_URL, timeout=5)
            if response.status_code == 200:
                st.success("Stream is active and running! 🎵")
            else:
                st.error("Stream might be experiencing issues. Please try again later.")
        except requests.RequestException:
            st.error("Unable to connect to the stream. Please check your internet connection.")

    # Footer
    st.markdown("---")
    st.markdown("© 2025 Kalika FM. All rights reserved.")

if __name__ == "__main__":
    main()