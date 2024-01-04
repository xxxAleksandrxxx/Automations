import asyncio
import edge_tts
from pydub import AudioSegment
from io import BytesIO

async def run(text, voice, rate, file_name) -> None:
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    print(type(communicate))
    # Trim received audio from start and from end
    try:
        audio_stream = BytesIO(communicate)
        audio = AudioSegment.from_file(audio_stream)
        audio_trimmed = audio[100:-960]
        await audio_trimmed.export(file_name, format="mp3")
    except:
        print("Audio didn't trimmed")
        await communicate.save(file_name)
    # await communicate.save(file_name)
