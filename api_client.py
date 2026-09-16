import requests


# -----------------------------
# Login API
# -----------------------------

def login(portal_url, username, password):

    url = portal_url + "/api/login"

    response = requests.post(
        url,
        json={
            "username": username,
            "password": password
        }
    )

    print("Login Status:", response.status_code)

    if response.status_code != 200:
        print(response.text)
        raise Exception("Login failed")

    return response.json()["token"]



# -----------------------------
# Fetch Logs API
# -----------------------------

def get_logs(portal_url, token):

    url = portal_url + "/api/logs"

    headers = {
        "Authorization": f"Bearer {token}"
    }


    response = requests.get(
        url,
        headers=headers
    )


    if response.status_code != 200:
        print("Logs Error:")
        print(response.text)
        raise Exception("Could not fetch logs")


    return response.json()



# -----------------------------
# Fetch Controls / Devices API
# -----------------------------

def get_controls(portal_url, token):

    url = portal_url + "/api/controls"


    headers = {
        "Authorization": f"Bearer {token}"
    }


    response = requests.get(
        url,
        headers=headers
    )


    # Debugging
    print("\nControls URL:", url)
    print("Controls Status:", response.status_code)


    if response.status_code != 200:
        print("Controls Response:")
        print(response.text)
        raise Exception("Could not fetch controls")


    data = response.json()


    # API returns:
    # {
    #   "devices":[...],
    #   "profile":{...}
    # }

    return data["devices"]



# -----------------------------
# Toggle Device API
# -----------------------------

def toggle_device(portal_url, token, device_id):


    url = (
        portal_url
        + f"/api/controls/{device_id}/toggle"
    )


    headers = {
        "Authorization": f"Bearer {token}"
    }


    response = requests.post(
        url,
        headers=headers
    )


    print("\nToggle URL:", url)
    print("Toggle Status:", response.status_code)


    if response.status_code != 200:
        print(response.text)
        raise Exception("Toggle failed")


    return response.json()