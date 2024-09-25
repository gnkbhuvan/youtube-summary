import os
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
from urllib.parse import unquote
import requests
import requests
from PIL import Image
from io import BytesIO

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create the model
generation_config = {
    "temperature": 0.55,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH",
    },
]

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-exp-0827",
    safety_settings=safety_settings,
    generation_config=generation_config,
)

# Function to fetch the transcript of a YouTube video
def fetch_transcript(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        transcript = " ".join([d['text'] for d in transcript_list])
        return transcript
    except Exception as e:
        return None
    
def get_final_url(shortened_url):
    try:
        # Send a GET request to the shortened URL
        response = requests.get(shortened_url, allow_redirects=True)
        
        # Get the final URL after all redirects
        final_url = response.url
        
        return final_url
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# Function to summarize text using Gemini API
def summarize_text_with_gemini(text):
    chat_session = model.start_chat(history=[])
    response = chat_session.send_message(f"""Generate a concise and coherent summary from the given Context. 

        Condense the context into a well-written summary that captures the main ideas, key points, and insights presented in the context. 

        Prioritize clarity and brevity while retaining the essential information. 

        Aim to convey the context's core message and any supporting details that contribute to a comprehensive understanding. 

        Craft the summary to be self-contained, ensuring that readers can grasp the content even if they haven't read the context. 

        Provide context where necessary and avoid excessive technical jargon or verbosity.

        The goal is to create a summary that effectively communicates the context's content while being easily digestible and engaging: {text}""")
    return response.text

# Streamlit UI
st.title("YouTube Video Summarizer")
st.info("Developed by Gnk Bhuvan - Ask me any queries, here! :wave: [X Link](https://x.com/gnkbhuvan)")
url = st.text_input("Enter YouTube Video URL here:")
video_url = get_final_url(url)
print(video_url)

if st.button("Summarize"):
    if video_url:
        try:
            video_id = video_url.split("v=")[1]
            video_id = video_id.split("&")[0] 
            transcript = fetch_transcript(video_id)
            if transcript:
                with st.spinner("Magic is happening... Please wait."):
                    summary = summarize_text_with_gemini(transcript)
                st.info("Voila !! Here's your summary")
                st.write(summary)
            else:
                st.error('Oops! Looks like the YouTube video is shy and didn\'t want to share its secrets with me. Please try again later.')

        except Exception as e:
            print(f"An error occurred: {e}")
            st.error("Uh-oh! It looks like our magic didn't quite work this time. Try again, and maybe we'll get it right next time!")
    else:
        st.error("Please enter a valid YouTube video URL.")
