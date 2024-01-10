import asyncio
import edge_tts

async def run(text, voice, rate, file_name, pitch="+0Hz") -> None:
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(file_name)
