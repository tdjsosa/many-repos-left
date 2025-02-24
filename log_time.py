from datetime import datetime

with open("log.txt", "a") as file:
    file.write(f"Log entry at: {datetime.now()}\n")

print("Log entry added!")
