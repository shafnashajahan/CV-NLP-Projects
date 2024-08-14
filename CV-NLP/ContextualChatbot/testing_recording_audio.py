#to create audio for our program testing
import pyaudio
import wave

# Parameters for audio recording
FORMAT = pyaudio.paInt16  # Format of sampling, paInt16 is used for 16-bit resolution
CHANNELS = 1  # Number of channels, 1 for mono, 2 for stereo
RATE = 44100  # Sampling rate, 44100 samples per second
CHUNK = 1024  # Number of audio samples per frame
RECORD_SECONDS = 10  # Duration of recording in seconds
OUTPUT_FILENAME = "output.wav"  # Name of the output file

# Create an interface to PortAudio
audio = pyaudio.PyAudio()

# Open a new stream for recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []

# Loop through stream and append audio data to frames
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("Finished recording.")

# Stop and close the stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save the recorded data as a .wav file
wf = wave.open(OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(audio.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

print(f"Audio saved as {OUTPUT_FILENAME}")
