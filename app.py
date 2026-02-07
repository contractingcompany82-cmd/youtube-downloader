import streamlit as st
import yt_dlp

st.set_page_config(page_title="YouTube Video Downloader", page_icon="📥")

st.title("📥 YouTube Video Downloader")
st.write("Paste any YouTube link below and download the video or audio.")

url = st.text_input("YouTube Video URL")

download_type = st.radio("Select Format", ["Video (MP4)", "Audio (MP3)"])

if st.button("Download"):
    if url.strip() == "":
        st.error("Please enter a valid YouTube URL.")
    else:
        st.info("Downloading... Please wait.")

        try:
            ydl_opts = {}

            if download_type == "Video (MP4)":
                ydl_opts = {
                    "format": "bestvideo+bestaudio/best",
                    "outtmpl": "downloaded_video.%(ext)s",
                }
            else:
                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": "downloaded_audio.%(ext)s",
                    "postprocessors": [{
                        "key": "FFmpegExtractAudio",
                        "preferredcodec": "mp3",
                        "preferredquality": "192",
                    }],
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            file_name = "downloaded_video.mp4" if download_type == "Video (MP4)" else "downloaded_audio.mp3"

            with open(file_name, "rb") as f:
                st.download_button(
                    label="Click to Download",
                    data=f,
                    file_name=file_name,
                    mime="video/mp4" if download_type == "Video (MP4)" else "audio/mp3"
                )

            st.success("Download ready!")

        except Exception as e:
            st.error(f"Error: {e}")
