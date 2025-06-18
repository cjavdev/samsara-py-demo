import time
from samsara import Samsara

client = Samsara()

while True:
  for driver in client.drivers.list():
      # Check for changes to the driver in the DB
      print(driver.id, driver.name, driver.eld_exempt)
      print("are we there, yet?")

  time.sleep(10)