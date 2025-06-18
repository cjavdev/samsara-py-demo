import asyncio
import os
import time
from samsara import AsyncSamsara

client = AsyncSamsara(token=os.getenv("SAMSARA_KEY"))

async def main() -> None:
    round = 0
    types = "gps,ecuSpeedMph"

    while True:
      response = await client.vehicles.stats.list(types=types)
      async for vehicle in response:
          print(vehicle.id)
          print(vehicle.gps.latitude, vehicle.gps.longitude)
          print(vehicle.ecu_speed_mph.value)

      round += 1
      print(f"Done with round #{round}. Waiting 10 seconds...")
      time.sleep(10)


asyncio.run(main())