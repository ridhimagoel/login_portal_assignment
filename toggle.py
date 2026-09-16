import requests


# -----------------------------
# Configuration
# -----------------------------

PORTAL_URL = "https://logs-portal-blond.vercel.app"

USERNAME = "test"
PASSWORD = "12345"


# -----------------------------
# 1. Login
# -----------------------------

login_url = PORTAL_URL + "/api/login"

login_data = {
    "username": USERNAME,
    "password": PASSWORD
}


print("Logging in...")

login_response = requests.post(
    login_url,
    json=login_data
)


print("Login Status:", login_response.status_code)


if login_response.status_code != 200:
    print("Login failed")
    print(login_response.text)
    exit()


login_data_response = login_response.json()

token = login_data_response["token"]


print("Login successful")
print("Token received")


# -----------------------------
# 2. Authorization Header
# -----------------------------

headers = {
    "Authorization": f"Bearer {token}"
}


# -----------------------------
# 3. Fetch Devices / Controls
# -----------------------------

controls_url = PORTAL_URL + "/api/controls"


print("\nFetching devices...")


controls_response = requests.get(
    controls_url,
    headers=headers
)


print("Controls Status:",
      controls_response.status_code)


if controls_response.status_code != 200:
    print("Unable to fetch devices")
    print(controls_response.text)
    exit()


controls_data = controls_response.json()


# -----------------------------
# 4. Extract Devices
# -----------------------------

if "devices" in controls_data:

    devices = controls_data["devices"]

else:

    print("Devices list not found")
    print(controls_data)
    exit()


# -----------------------------
# 5. Show allowed devices
# -----------------------------

allowed_devices = []


print("\nDevices you can control:")


for device in devices:

    if device["canControl"]:

        allowed_devices.append(device)

        print(
            "-",
            device["id"],
            "| State:",
            device["state"]
        )


if len(allowed_devices) == 0:

    print("No controllable devices found")
    exit()



# -----------------------------
# 6. Select Device
# -----------------------------

device_id = input(
    "\nEnter device id to turn OFF: "
)


# Check whether user selected allowed device

valid = False


for device in allowed_devices:

    if device["id"] == device_id:

        valid = True
        break


if not valid:

    print("You are not allowed to control this device")
    exit()



# -----------------------------
# 7. Toggle Device OFF
# -----------------------------

toggle_url = (
    PORTAL_URL
    + f"/api/devices/{device_id}/toggle"
)


print("\nSending toggle request...")


toggle_response = requests.post(
    toggle_url,
    headers=headers
)


print(
    "Toggle Status:",
    toggle_response.status_code
)


print("\nServer Response:")


print(toggle_response.text)