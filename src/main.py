import pyaudio
import wave
import os

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


    
def menu_change_parameters():
    
    print("Picked option -> 2. Set audio parameters\n")
    user_choice = input(" - Set [Frames per buffer]: ")
    user_choice = input(" - Set [Sampling rate]: ")
    user_choice = input(" - Set [Number of channels]: ")
    user_choice = input(" - Set [Format]: ")
    
def menu_record_audio():

    print("Picked option -> 2. Record audio file\n")
    user_choice = input(" - Set [Record time]: ")
    
    user_choice_record_time = input()

def menu_play_audio():
    print(
        "Picked option -> 2. Play audio file"
    )

def quit():
    print("Quitting application...")
    return False
    
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main():

    is_main_loop: bool = True

    while is_main_loop:
    
        cls()
    
        print(
            "\n"
            "Hello D/A - A/D - Converter! Choose:\n\n"
            "1. Set audio parameters.\n"
            "2. Record audio file.\n"
            "3. Play audio file.\n"
            "q. QUIT\n"
        )
    
        user_choice = input("> ")
        match user_choice:
            case "1":
                menu_change_parameters()
            case "2":
                menu_record_audio()
            case "3":
                menu_play_audio()
            case "q":
                is_main_loop=quit()
            case other:
                is_main_loop=quit()
    

if __name__ == "__main__":
    main()