import psutil
import datetime

def get_server_uptime():
    """
    Retrieves the server uptime in a human-readable format.
    """
    boot_time_timestamp = psutil.boot_time()
    boot_time_datetime = datetime.datetime.fromtimestamp(boot_time_timestamp)
    current_time = datetime.datetime.now()
    uptime_duration = current_time - boot_time_datetime

    days = uptime_duration.days
    seconds = uptime_duration.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    uptime_string = f"Uptime: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    return uptime_string

if __name__ == "__main__":
    uptime = get_server_uptime()
    print(uptime)
