import sys
import datetime


log_file = sys.argv[1]

with open(log_file, "a") as f:
    while True:
        try:
            log_message = input().strip()
            if log_message == "QUIT":
                break
            
            parts = log_message.split(maxsplit=1)


            action, message = parts[0], parts[1]
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            log_entry = f"{timestamp} [{action}] {message}\n"
            f.write(log_entry)
        except EOFError:
            break

