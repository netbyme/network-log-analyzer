# network-log-analyzer

A Python tool that reads network device log files, extracts errors and warnings, and generates a clean dated report automatically.

## What it does

- Reads router and switch log files automatically
- Extracts only errors and warnings — ignores INFO lines
- Displays issues in the terminal in real time
- Saves a full analysis report to a dated file
- Replaces manual log searching completely

## Why this matters

Network devices generate thousands of log lines daily. Engineers waste hours searching manually for errors. This tool reads the entire log in seconds and shows only what matters — errors and warnings that need attention.

## How to run

```bash
python3 log_analyzer.py
```

## Output example