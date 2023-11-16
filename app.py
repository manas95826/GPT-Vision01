import streamlit as st
import base64
import requests

# OpenAI API Key
api_key = "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"

# Function to encode the image
def encode_image(image_file):
    return base64.b64encode(image_file.read()).decode('utf-8')

# Streamlit app
def main():
    st.title("OpenAI Image Recognition Chat")

    # File uploader
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Getting the base64 string
        base64_image = encode_image(uploaded_file)

        # Display the image
        st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        # OpenAI API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

        payload = {
            "model": "gpt-4-vision-preview",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What’s in this image?"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        # Display OpenAI response
        st.subheader("OpenAI Response:")
        st.json(response.json())

if __name__ == "__main__":
    main()
