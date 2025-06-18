import time
from samsara import Samsara

client = Samsara()
round = 0
types = "gps,ecuSpeedMph"

while True:
  for vehicle in client.vehicles.stats.list(types=types):
      print(vehicle.id)
      print(vehicle.gps.latitude, vehicle.gps.longitude)
      print(vehicle.ecu_speed_mph.value)

  round += 1
  print(f"Done with round #{round}. Waiting 10 seconds...")
  time.sleep(10)