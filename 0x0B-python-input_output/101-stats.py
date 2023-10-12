#!/usr/bin/python3
"""
    IMPORT SYS MOUDLE
"""
import sys
"""
    IMPORT SIGNAL MODULE
"""
import signal

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

line_count = 0

# Define a handler for keyboard interruption (Ctrl+C)
def interrupt_handler(signum, frame):
    print("Total file size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f"{code}: {count}")
    sys.exit(0)

# Set up the signal handler
signal.signal(signal.SIGINT, interrupt_handler)

try:
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        if len(parts) == 7:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_file_size += file_size
            status_code_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f"{code}: {count}")

except KeyboardInterrupt:
    pass
