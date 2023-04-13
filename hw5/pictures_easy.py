import asyncio
import random
from io import BytesIO
from PIL import Image
import aiohttp
import aiofiles


async def save_image(filename, image):
    async with aiofiles.open(f'artifacts/easy/{filename}.jpeg', 'wb') as f:
        return await f.write(image)


async def get_image(num, size, session):
    url = f"https://picsum.photos/{size}/{size}"
    response = await session.get(url)
    image_content = await response.content.read()

    img = Image.open(BytesIO(image_content))
    buffer = BytesIO()
    img.save(buffer, format="JPEG")

    await save_image(str(num), buffer.getbuffer())


async def main(n):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *(get_image(i, random.randrange(100, 1001, 100), session) for i in range(n))
        )


if __name__ == "__main__":
    n = 5
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main(n))
