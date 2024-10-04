import time

current_time = time.time()

total_seconds = int(current_time)

seconds = total_seconds % 60

total_minutes = seconds // 60

print(total_minutes)