import os
import requests
import time

BASE_URL = "https://api.samsara.com/fleet/vehicles/stats"
HEADERS = {
    "Authorization": f"Bearer {os.getenv('SAMSARA_KEY')}",
    "Accept": "application/json"
}

def poll_vehicles():
    round = 0

    while True:
        params = {}
        has_next_page = True

        while has_next_page:
            response = requests.get(
              f"{BASE_URL}?types=gps,ecuSpeedMph",
              headers=HEADERS,
              params=params
            )
            response_json = response.json()

            for vehicle in response_json.get("data", []):
                print(vehicle.get("id"))
                gps = vehicle.get("gps")
                print(gps.get("latitude"), gps.get("longitude"))
                print(vehicle.get("ecuSpeedMph").get("value"))

            pagination = response_json.get("pagination", {})
            has_next_page = pagination.get("hasNextPage", False)
            if has_next_page:
                params["after"] = pagination.get("endCursor")

        # Wait 10 seconds and do it again...
        round += 1
        has_next_page = True
        print(f"Done with round #{round}. Waiting 10 seconds...")
        time.sleep(10)

poll_vehicles()
