import os

from samsara import Samsara

client = Samsara(token=os.getenv("SAMSARA_KEY"))

vehicles = client.vehicles.list()

for vehicle in vehicles:
    print(vehicle.id)
    print(vehicle.name)
    print(vehicle.vin)
    print(vehicle.make)
    print(vehicle.model)
    print(vehicle.year)


for driver in client.drivers.list():
    print(driver.name)
