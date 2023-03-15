import asyncio
import sys

from dynmod import backend


async def main():
    print(sys.modules["dynmod.backend"].__class__, backend.NAME)
    await backend.sleep(1.1)


if __name__ == "__main__":
    asyncio.run(main())
