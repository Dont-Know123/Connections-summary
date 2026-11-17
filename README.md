# Connection Summarizer

A Python script that reads a network connection log, counts connections
per destination port, labels each port with its usual service, and flags
repeated connections to remote-access ports (SSH, RDP).

## How to run
python3 summarizer.py

## Detection rule
Alert when port 22 or 3389 has 3 or more connections in the log.

## What I learned
Counting with dictionaries, port-to-service lookups, and combining
conditions with and/or (parentheses matter).