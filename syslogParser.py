
#! /usr/bin/env/python
import os
import re
#Change to and print correct file path
os.chdir('/Users/MacUser/Desktop/regExPython')
print(os.getcwd())

#iterate and read from syslogexample.txt then print results
line_number = 0
with open('syslogexample.txt', 'r') as syslog:
    log_lines = syslog.readlines()
    for line in log_lines:
        line_number += 1
        print('{:>4} {}'.format(line_number, line.rstrip()))


#Build regex to parse through the data
DATE_RE = r'(\w{3}\s+\d{2})'
TIME_RE = r'(\d{2}:\d{2}:\d{2})'
DEVICE_RE = r'(\S+)'
PROCESS_RE = r'(\S+\s+\S+:)'
MESSAGE_RE = r'(.*)'
CD_RE = r'(\s+)'

Syslog_RE = DATE_RE + CD_RE + \
            TIME_RE + CD_RE + \
            DEVICE_RE + CD_RE + \
            PROCESS_RE + CD_RE + \
            MESSAGE_RE

#Use regex to parse through the data
for line in log_lines:
    m = re.match(Syslog_RE, line)
    if m:
        print(m.groups())


for line in log lines:
	m = re.match(SYSLOG_RE, line)

