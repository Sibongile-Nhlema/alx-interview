#!/usr/bin/python3
'''
script that reads stdin line by line and computes metrics
Input format: <IP Address> - [<date>]
"GET /projects/260 HTTP/1.1" <status code> <file size>

(if the format is not this one, the line must be skipped)

After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
format: <status code>: <number>
status codes should be printed in ascending order
'''
import sys
import re

# Regular expression to match the expected log line format
log_line_regex = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)'

total_size = 0
status_code_counts = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        line = line.strip()
        
        # Match the line against the regex expression
        match = re.match(log_line_regex, line)
        if match:
            status_code = int(match.group(3))
            file_size = int(match.group(4))
            # Update total file size
            total_size += file_size
            
            # Update status code count
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            else:
                status_code_counts[status_code] = 1
            
            # Print statistics for every 10 lines
            if line_count % 10 == 0:
                print(f"File size: {total_size}")
                for code in sorted(status_code_counts.keys()):
                    print(f"{code}: {status_code_counts[code]}")
                print()

except KeyboardInterrupt:
    # Print final statistics on keyboard interruptions
    print(f"File size: {total_size}")
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")
    sys.exit(0)
