import asyncio
import edge_tts

async def run(text, voice, rate, pitch, file_name) -> None:
    communicate = edge_tts.Communicate(text, voice, rate=rate, pitch=pitch)
    await communicate.save(file_name)
