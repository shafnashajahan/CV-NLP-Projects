#Speech-to-Text with Vosk
import vosk
import wave
import json

def transcribe_audio_vosk(audio_file_path):
    """
    Transcribes an audio file into text using the Vosk speech-to-text model.
    
    :param audio_file_path: Path to the audio file to be transcribed.
    :return: The transcribed text.
    """
    # Load the pre-trained Vosk model
    model = vosk.Model("/swades.ai/ContextualChatbot/models/vosk-model-en-us-0.22")  # Specify the correct path to your Vosk model
    wf = wave.open(audio_file_path, "rb")
    recognizer = vosk.KaldiRecognizer(model, wf.getframerate())
    transcript = ""
    
    # Process audio in chunks and accumulate the transcription
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_json = json.loads(result)
            transcript += result_json.get('text', '') + " "
    
    return transcript.strip()

# Example usage
if __name__ == "__main__":
    transcript = transcribe_audio_vosk("output.mp3")
    print(transcript)


# import vosk
# import pyaudio
# import json

# def transcribe_audio_vosk_real_time():
#     """
#     Transcribes real-time audio input from the microphone using the Vosk speech-to-text model.
    
#     :return: The transcribed text.
#     """
#     model = vosk.Model("/content/drive/MyDrive/swades.ai/ContextualChatbot/models/vosk-model-en-us-0.22")
#     recognizer = vosk.KaldiRecognizer(model, 16000)

#     # Initialize PyAudio for real-time audio input
#     p = pyaudio.PyAudio()
#     stream = p.open(format=pyaudio.paInt16,
#                     channels=1,
#                     rate=16000,
#                     input=True,
#                     frames_per_buffer=4096)
#     stream.start_stream()

#     transcript = ""
#     print("Listening...")

#     try:
#         while True:
#             data = stream.read(4096)
#             if recognizer.AcceptWaveform(data):
#                 result = recognizer.Result()
#                 result_json = json.loads(result)
#                 transcript += result_json.get('text', '') + " "
#                 print(result_json.get('text', ''))  # Print the transcript in real-time

#     except KeyboardInterrupt:
#         # Stop the stream and PyAudio when interrupted
#         stream.stop_stream()
#         stream.close()
#         p.terminate()

#     return transcript.strip()

# # Example usage for real-time transcription
# if __name__ == "__main__":
#     transcript = transcribe_audio_vosk_real_time()
#     print("\nFinal Transcript:", transcript)

