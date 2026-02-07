import streamlit as st
import yt_dlp

st.set_page_config(page_title="YouTube Downloader", page_icon="📥")

st.title("📥 YouTube Video Downloader")

url = st.text_input("YouTube URL")

download_type = st.radio("Choose format", ["Video (MP4)", "Audio Only"])

if st.button("Download"):
    if not url:
        st.error("Please enter a valid URL.")
    else:
        st.info("Downloading... Please wait.")

        try:
            if download_type == "Video (MP4)":
                ydl_opts = {
                    "format": "bv*+ba/b",
                    "outtmpl": "video.%(ext)s",
                    "merge_output_format": "mp4",
                }
                file_name = "video.mp4"

            else:
                ydl_opts = {
                    "format": "bestaudio/best",
                    "outtmpl": "audio.%(ext)s",
                }
                file_name = "audio.webm"

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

            with open(file_name, "rb") as f:
                st.download_button(
                    label="Download File",
                    data=f,
                    file_name=file_name,
                )

            st.success("Download ready!")

        except Exception as e:
            st.error(f"Error: {e}")
