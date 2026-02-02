import time
from plyer import notification

while True:
    print("Please drink water!")
    notification.notify(
        title="Water Reminder",
        message="It's time to drink water and stay hydrated!",
        timeout=10
    )
    time.sleep(60 * 60)
