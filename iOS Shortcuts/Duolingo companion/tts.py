'''
1. convert text to audio
2. save audio to file
3. open audio file 
4. trim audio
5. save audio to file
'''

import asyncio
import edge_tts
from concurrent.futures import ThreadPoolExecutor
from pydub import AudioSegment

executor = ThreadPoolExecutor(max_workers=2)

# trimming function
async def async_trim_mp3(file_input, time_start_ms, time_end_ms):
    loop = asyncio.get_running_loop()
    
    def trim_and_save():
        audio = AudioSegment.from_file(file_input, format="mp3")
        audio_trimmed = audio[time_start_ms:-time_end_ms]  # Fix slicing here
        audio_trimmed.export(file_input, format="mp3")  # Overwrite the original file

    # Run the trimming and saving operation in a separate thread
    await loop.run_in_executor(executor, trim_and_save)

# main async function
async def run(text, voice, rate, file_name):
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(file_name)
    await async_trim_mp3(file_name, 100, 860)  # time_start_ms = 100, time_end_ms = 860):
