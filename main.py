from api_client import (
    login,
    get_controls,
    toggle_device
)

from log_stream import stream_logs



PORTAL_URL = "https://logs-portal-blond.vercel.app"



username = input("Username: ")
password = input("Password: ")



token = login(
    PORTAL_URL,
    username,
    password
)


print("\nLogin successful")



while True:

    print("\nMenu")
    print("1. Stream Logs")
    print("2. Toggle Device")
    print("3. Exit")


    choice = input(
        "Choose option: "
    )


    if choice == "1":

        stream_logs(
            PORTAL_URL,
            token
        )


    elif choice == "2":


        devices = get_controls(
            PORTAL_URL,
            token
        )


        print("\nAllowed Devices:")


        for device in devices:

            if device["canControl"]:

                print(
                    device["id"]
                )


        device_id = input(
            "Enter device id: "
        )


        result = toggle_device(
            PORTAL_URL,
            token,
            device_id
        )


        print(result)



    elif choice == "3":

        print("Exiting...")
        break


    else:

        print("Invalid choice")