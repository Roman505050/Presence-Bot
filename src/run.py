import asyncio
import logging
import sys

from src.index import start

async def main():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    await start()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('KeyboardInterrupt')