import os

from samsara import Samsara

client = Samsara(token=os.getenv("SAMSARA_KEY"))

vehicles = client.vehicles.list().data

for vehicle in vehicles:
    print(vehicle.id)
    print(vehicle.name)
    print(vehicle.vin)
    print(vehicle.make)
    print(vehicle.model)
    print(vehicle.year)
