# API Performance Monitoring System

##  Overview
A Python-based system that benchmarks API performance by measuring response time, success rate, and failure rate across multiple endpoints.

---

##  Features
- Measures API response time (ms)
- Calculates success and failure rates
- Handles API timeouts and errors
- Compares multiple endpoints
- Performs repeated request benchmarking

---

## Tech Stack
- Python
- Requests library
- Time module

---

##  How It Works
1. Sends multiple requests to each API
2. Measures response latency
3. Tracks success and failures
4. Computes:
   - Average response time
   - Success rate
   - Failure rate

---

## Run Project
```bash
pip install -r requirements.txt
python src/main.py
