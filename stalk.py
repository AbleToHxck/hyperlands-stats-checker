import aiohttp, asyncio, json
from rich import print


async def req():
    username = input("Username: ")
    stats = None
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.hyperlandsmc.net/stats/{username}") as r:
            stats = json.loads(await r.read())
    if "error" in stats:
        print(stats["error"])
        return
    newStats = {}
    for key, value in stats["stats"].items():
        newStats[key.capitalize()] = value
    for key, value in newStats.items():
        if type(value) is dict:
            newStats[key] = {key.capitalize(): value for key, value in value.items()}
    for key, value in newStats.items():
        if type(value) is dict:
            print(f"{key}:")
            for key2, value2 in value.items():
                print(f"    {key2} - {value2}")


asyncio.run(req())
