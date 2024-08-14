# single script that transcribes audio, generates embeddings, retrieves context, and generates a response.
from transcribe import transcribe_audio_vosk
from embedding import embed_and_store, retrieve_context
from response_generator import generate_response

def process_audio_and_respond(audio_file_path):
    """
    Processes an audio file to generate a contextual response by:
    1. Transcribing the audio to text.
    2. Embedding the text and storing it.
    3. Retrieving relevant context.
    4. Generating a response based on the context.
    
    :param audio_file_path: Path to the audio file to be processed.
    :return: The chatbot's response.
    """
    # Step 1: Transcribe audio to text
    transcript = transcribe_audio_vosk(audio_file_path)
    
    # Step 2: Embed and store the transcript
    embed_and_store([transcript])
    
    # Step 3: Retrieve relevant context (for simplicity, using the transcript itself)
    context_indices = retrieve_context(transcript)
    # In a practical scenario, map indices to actual context texts
    context = [transcript]  # Replace with actual context retrieval logic
    context_str = " ".join(context)
    
    # Step 4: Generate a response based on the context
    prompt = f"Based on the following context, answer the question: {context_str}\nQuestion: {transcript}"
    response = generate_response(prompt)
    print("Chatbot Response:", response)

# Example usage
if __name__ == "__main__":
    process_audio_and_respond("path/to/audio/file.wav")
