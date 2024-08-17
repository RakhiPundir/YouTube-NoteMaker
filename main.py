import streamlit as st
import os
import subprocess
from pathlib import Path
import time
from docx import Document
from docx.shared import Inches
from PIL import Image
import io

import save_frames
import save_transcript
import delete_duplicates
import merge_notes


# Streamlit GUI
st.title("YouTube NoteMaker")
st.subheader("You just focus on understanding, we will create the Notes for you 😉")

# Input field for YouTube URL
youtube_url = st.text_input("Enter the YouTube video URL:", "")

# Button to start processing
if st.button("Start Processing"):
    if youtube_url.strip() == "":
        st.error("Please enter a valid YouTube URL.")
    else:
        # Display progress bar
        progress_bar = st.progress(0)

        # Run the scripts sequentially
        try:
            # Step 1: Download video and save frames
            progress_bar.progress(10)
            save_frames.main(youtube_url)
            
            # Step 2: Extract transcript with timestamps
            progress_bar.progress(40)
            save_transcript.main(youtube_url)
            
            # Step 3: Delete duplicate frames
            progress_bar.progress(60)
            delete_duplicates.delete_duplicates()
            
            # Step 4: Merge frames and transcript into a docx file
            progress_bar.progress(90)
            merge_notes.main()

            # Final step: Progress bar completes
            progress_bar.progress(100)
            st.success("Processing complete!")

            # Locate the output file
            output_file = Path("output.docx")

            if output_file.exists():
                # Provide option to read or download the file
                with open(output_file, "rb") as file:
                    btn = st.download_button(
                        label="Download the generated Notes",
                        data=file,
                        file_name="YouTube_Notes.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )

                st.write("Or you can read the file below:")

                # Display the document content in the Streamlit app
                doc = Document(output_file)
                doc_text = []
                for para in doc.paragraphs:
                    doc_text.append(para.text)
                st.text("\n".join(doc_text))

                # with open(output_file, "rb") as file:
                #     st.download_button(label="Read the file", data=file, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

        except subprocess.CalledProcessError as e:
            st.error(f"An error occurred while processing the video: {e}")

