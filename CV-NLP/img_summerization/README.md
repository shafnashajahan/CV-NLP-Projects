# Image Summarization API

## Overview

This Flask-based API allows users to upload image files (such as photos of text documents) and returns a summary of the text content in those images. The API uses Tesseract OCR to extract text and a pre-trained model from Hugging Face's `transformers` library to summarize the extracted text.

## Features

- **Image Upload**: Users can upload images in formats like JPG, PNG, etc.
- **Text Extraction**: Extracts text from the uploaded images using Tesseract OCR.
- **Text Summarization**: Summarizes the extracted text using a state-of-the-art NLP model.
- **Responsive Web Interface**: A user-friendly web interface for easy interaction.
- **API Endpoints**: Easily integrable API endpoints for use in other applications.

## Getting Started

### Prerequisites

- **Python 3.x**: Ensure you have Python installed.
- **Pip**: Python package installer.
- **Virtual Environment** (optional but recommended).

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/shafnashajahan/CV-NLP-Projects.git
   cd image-summarization-api
