# YouTube Video Summarizer

## Overview

YouTube Video Summarizer is a web application that generates concise summaries of YouTube videos using AI. It's powered by Google's Gemini AI and deployed on Streamlit.

Live demo: [https://youtube-summaryy.streamlit.app/](https://youtube-summaryy.streamlit.app/)

## Features

- Accepts YouTube video URLs (including shortened URLs)
- Fetches video transcripts automatically
- Generates AI-powered summaries using Google's Gemini model
- User-friendly interface built with Streamlit

## How to Use

1. Visit [https://youtube-summaryy.streamlit.app/](https://youtube-summaryy.streamlit.app/)
2. Enter a YouTube video URL in the provided text input
3. Click the "Summarize" button
4. Wait for the AI to generate a summary
5. Read the concise summary of the video content

## Technology Stack

- Python
- Streamlit
- Google Gemini AI
- YouTube Transcript API

## Local Development

To run this project locally:

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your Gemini API key: `GEMINI_API_KEY=your_api_key_here`
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## About the Developer

Developed by Gnk Bhuvan. Connect with me on [X (Twitter)](https://x.com/gnkbhuvan).

## License

[MIT License](LICENSE)
