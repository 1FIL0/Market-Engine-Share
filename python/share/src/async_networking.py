from pathlib import Path
from typing import Callable
import aiohttp
import logger

async def fetchCacheContents(url: str, cachePath: Path, callbackCachedPath: Callable[[Path], None]):
    try:
        data = await fetchContents(url)
        cachePath.write_bytes(data)
    except Exception as e:
        logger.sendMessage(f"{e}")
    callbackCachedPath(cachePath)

async def fetchContents(url: str) -> bytes:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            return await resp.read()