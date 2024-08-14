from flask import Flask, request, jsonify, render_template
from PIL import Image
import pytesseract
from transformers import pipeline

app = Flask(__name__)

# Initialize the summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Home route with file upload form
@app.route('/')
def home():
    return render_template('upload.html')

# Route to handle file upload and processing
@app.route('/summarize', methods=['POST'])
def summarize_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Extract text from the image
        img = Image.open(file)
        text = pytesseract.image_to_string(img)

        # Summarize the extracted text
        summary = summarizer(text, max_length=200, min_length=30, do_sample=False)

        return jsonify({'summary': summary[0]['summary_text']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
