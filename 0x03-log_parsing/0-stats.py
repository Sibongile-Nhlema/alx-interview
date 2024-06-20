#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics
"""

import sys
import re

# Regular expression to match the expected log line format
log_line_regex = (
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] '
    r'"GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'
)

total_size = 0
status_code_counts = {}


def print_statistics():
    '''
    script that defines the print stats method
    '''
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")


try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()
        # Match the line against the regex
        match = re.match(log_line_regex, line)
        if match:
            line_count += 1
            status_code = int(match.group(3))
            file_size = int(match.group(4))
            # Update total file size
            total_size += file_size
            # Update status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1
            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics()

except KeyboardInterrupt:
    pass

finally:
    # Print final statistics on keyboard interrupt
    print_statistics()
