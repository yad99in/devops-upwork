import psutil
import smtplib
from email.message import EmailMessage

def check_server_health():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    if cpu > 80 or mem > 80 or disk > 80:
        send_alert(cpu, mem, disk)

def send_alert(cpu, mem, disk):
    msg = EmailMessage()
    msg.set_content(f"ALERT! High Usage: CPU={cpu}%, Memory={mem}%, Disk={disk}%")
    msg["Subject"] = "Server Health Alert"
    msg["From"] = "alert@example.com"
    msg["To"] = "admin@example.com"

    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("user", "password")
        server.send_message(msg)

if __name__ == "__main__":
    check_server_health()
