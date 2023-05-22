import pyaudio
import wave
import os

import play as p
    
def menu_change_parameters(audio_parameters: tuple[int, int, int, int]):
    chunk, audio_format, channel_number, rate = audio_parameters
    
    # Exsisting formats. flag system !
    # PAINT32 = 2
    # PAINT24 = 4
    # PAINT16 = 8
    # PAINT8 = 16
    
    print("\nPicked option -> 1. Set audio parameters\n")
    chunk = int(input(" - Set [Frames per buffer]: "))
    rate = int(input(" - Set [Sampling rate]: "))
    channel_number = int(input(" - Set [Number of channels]: "))
    user_choice = int(input(" - Set [Format]: "))
    
    match user_choice:
        case 32:
            audio_format = pyaudio.paInt32
        case 24:
            audio_format = pyaudio.paInt24
        case 16:
            audio_format = pyaudio.paInt16
        case 8:
            audio_format = pyaudio.paInt8
            
    return chunk, audio_format, channel_number, rate
    
def menu_record_audio(audio_parameters: tuple[int, int, int, int]):
    chunk, input_format, channel_number, rate = audio_parameters

    print("\nPicked option -> 2. Record audio file\n")
    seconds_number = int(input(" - Set [Record time (in seconds)]: "))
    
    return "" # return the filepath

def menu_play_audio(audio_parameters: tuple[int, int, int, int]):
    chunk, input_format, channel_number, rate = audio_parameters

    print("\nPicked option -> 3. Play audio file")
    filepath = input(" - Set [.wav filepath]: ")
    
    p.play(filepath)

def quit():

    print(
        "\nPicked option -> q. QUIT\n"
        "Quitting application..."
    )
    
    return False
    
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def audio_parameters_string(audio_parameters: tuple[int, int, int, int]):
    chunk, input_format, channel_number, rate = audio_parameters
    return f"Frames Per Buffer: {chunk}\n" + \
           f" Sampling rate: {rate}\n" + \
           f" Number of channels: {channel_number}\n" + \
           f" Format: {input_format}"
    
def main():

    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100

    audio_parameters = (CHUNK, FORMAT, CHANNELS, RATE)
    is_main_loop: bool = True

    while is_main_loop:
    
        cls()
    
        print(
            "\n"
            "Hello D/A - A/D - Converter! Choose:\n\n",
            audio_parameters_string(audio_parameters),
            "\n\n"
            "1. Set audio parameters.\n"
            "2. Record audio file.\n"
            "3. Play audio file.\n"
            "q. QUIT\n"
        )
    
        user_choice = input("> ")
        match user_choice:
            case "1":
                audio_parameters = menu_change_parameters(audio_parameters)
            case "2":
                menu_record_audio(audio_parameters)
            case "3":
                menu_play_audio(audio_parameters)
            case "q":
                is_main_loop = quit()
            case other:
                is_main_loop = quit()
    

if __name__ == "__main__":
    main()