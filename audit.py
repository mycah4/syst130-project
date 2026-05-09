from datetime
import datetime

def create_audit_log(event_type, details):
    timestamp = datatime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("audit_log.txt", "a") as log_file:
        log_file.write(f"[{timestamp}] {event_type}: {details}\n")
