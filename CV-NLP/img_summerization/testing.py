#testing code without Flask
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
from transformers import pipeline

# Function to extract text from an image
def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

# Function to summarize text
def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=200, min_length=30, do_sample=False)
    return summary[0]['summary_text']

# Function to handle file upload and process the image
def upload_image():
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.jpg *.jpeg *.png")]
    )
    if not file_path:
        return

    try:
        # Extract text from the image
        text = extract_text_from_image(file_path)
        print("Extracted Text:\n", text)

        # Summarize the extracted text
        summary = summarize_text(text)
        print("\nSummary:\n", summary)

        # Display the summary in a messagebox
        messagebox.showinfo("Summary", summary)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main GUI window
root = tk.Tk()
root.title("Image Text Extractor and Summarizer")

# Add a button to upload an image
upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
