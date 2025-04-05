# asyncio (Programação assíncrona)
async def fetch_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


# multiprocessing (CPU-bound tasks)
with Pool(4) as p:
    results = p.map(process_data, large_dataset)
