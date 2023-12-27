import asyncio
import edge_tts

async def run(text, voice, file_name) -> None:
    communicate = edge_tts.Communicate(text, voice)
    await communicate.save(file_name)
