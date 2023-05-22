import pyaudio
import wave
import os
    
def menu_change_parameters():
    
    print("Picked option -> 2. Set audio parameters\n")
    user_choice = input(" - Set [Frames per buffer]: ")
    user_choice = input(" - Set [Sampling rate]: ")
    user_choice = input(" - Set [Number of channels]: ")
    user_choice = input(" - Set [Format]: ")
    
def menu_record_audio():

    print("Picked option -> 2. Record audio file\n")
    user_choice = input(" - Set [Record time]: ")

def menu_play_audio():

    print("Picked option -> 2. Play audio file")
    user_choice = input(" - Set [.wav filepath]: ")

def quit():
    print("Quitting application...")
    return False
    
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def audio_parameters_string(audio_setup: tuple[int, int, int, int]):
    chunk, input_format, channel_number, rate = audio_setup
    return f"Frames Per Buffer: {chunk}\n" + \
           f"Format: {input_format}\n" + \
           f"Number of channels: {channel_number}\n" + \
           f"Sampling rate: {rate}"
    
def main():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    audio_setup = (CHUNK, FORMAT, CHANNELS, RATE)
    is_main_loop: bool = True

    while is_main_loop:
    
        cls()
        
        #print(, "\n")
    
        print(
            "\n"
            "Hello D/A - A/D - Converter! Choose:\n\n",
            audio_parameters_string(audio_setup),
            "\n\n"
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
                is_main_loop = quit()
            case other:
                is_main_loop = quit()
    

if __name__ == "__main__":
    main()