import time
from api_client import get_logs
def stream_logs(portal_url, token):
    while True:
        logs = get_logs(
            portal_url,
            token
        )
        print("\n------ Logs ------")


        for log in logs:
            print(log)


        time.sleep(4)