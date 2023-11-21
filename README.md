# OpenAI Image Recognition Chat

This Streamlit app allows you to interact with OpenAI's GPT-4 Vision model to recognize the content of an image. You can upload an image, and the app will use the OpenAI API to generate a description of the image.

## Prerequisites

Before running the app, make sure you have the required dependencies installed. You can install them using the following command:

```bash
pip install streamlit requests
```

Additionally, you need to obtain an API key from OpenAI. Replace the placeholder `api_key` variable in the `main.py` file with your actual API key.

## How to Run

To run the app, use the following command in your terminal:

```bash
streamlit run main.py
```

This will start a local development server, and you can access the app in your web browser at `http://localhost:8501`.

## Usage

1. Launch the app using the instructions above.
2. Upload an image using the file uploader.
3. The app will display the uploaded image and send a request to the OpenAI API to generate a description.
4. The OpenAI response will be displayed below the image.

## File Structure

- `main.py`: Contains the Streamlit app code.
- `requirements.txt`: Lists the Python dependencies for the project.

## Acknowledgments

- This app uses Streamlit for the web interface.
- Powered by OpenAI's GPT-4 Vision model.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

Make sure to replace the placeholder in the `requirements.txt` file with the correct version numbers if needed. Additionally, if you want to include a license file (e.g., `LICENSE`), you can customize the license section accordingly.
