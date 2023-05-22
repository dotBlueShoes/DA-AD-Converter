import pyaudio
import wave

def record(audio_parameters: tuple[int, int, int, int],seconds):
    chunk, input_format, channel_number, rate = audio_parameters
    p = pyaudio.PyAudio()

    stream = p.open(
        format = input_format,
        channels = channel_number,
        rate = rate,
        input = True,
        frames_per_buffer = chunk
    )

    print("start recording")

    frames = []
    for i in range(0, int(rate / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("recording stopped")

    stream.stop_stream()
    stream.close()
    p.terminate()
    name = input("Name of file[.wav]: ")
    name = name + ".wav"
    wf = wave.open(name, "wb")
    wf.setnchannels(channel_number)
    wf.setsampwidth(p.get_sample_size(input_format))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()
