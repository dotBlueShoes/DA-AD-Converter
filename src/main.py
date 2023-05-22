import pyaudio
import wave

#CHUNK = 1024
#FORMAT = pyaudio.paInt16
#CHANNELS = 1
#RATE = 44100
#
#p = pyaudio.PyAudio()
#
#stream = p.open(
#    format = FORMAT,
#    channels = CHANNELS,
#    rate = RATE,
#    input = True,
#    frames_per_buffer = CHUNK
#)
#    
#print("start recording")
#
#frames = []
#seconds = 3
#for i in range(0, int(RATE / CHUNK * seconds)):
#    data = stream.read(CHUNK)
#    frames.append(data)
#    
#print("recording stopped")
#
#stream.stop_stream()
#stream.close()
#p.terminate()
#
#wf = wave.open("output.wav", "wb")
#wf.setnchannels(CHANNELS)
#wf.setsampwidth(p.get_sample_size(FORMAT)) 
#wf.setframerate(RATE)
#wf.writeframes(b''.join(frames))
#wf.close()


is_main_loop = True
    
    
def menu_change_parameters():
    print("a")
    
def menu_record_audio():
    print("b")

def menu_play_audio():
    print("c")

def quit():
    print("Quitting application...")
    is_main_loop = False
    
def main():

    print(
        "\n"
        "Hello D/A - A/D - Converter! Choose:\n\n"
        "1. Set audio parameters.\n"
        "2. Record audio file.\n"
        "3. Play audio file.\n"
        "q. QUIT\n"
    )
    
    while(is_main_loop):
    
        user_choice = input("> ")
    
        match user_choice:
            case "1":
                menu_change_parameters()
            case "2":
                menu_record_audio()
            case "3":
                menu_play_audio()
            case "q":
                quit()
            case other:
                quit()
    

if __name__ == "__main__":
    main()