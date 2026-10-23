import datetime

# Get actual timestamp and count from recent cycles
from datetime import datetime, timezone
ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Count open positions from ledger
open_pos = 0
with open("journal/ledger.jsonl") as f:
    for line in f:
        d = json.loads(line)
        if d.get("closed") == False:
            open_pos += 1

# Count recent FULL cycles from cycles.log
with open("journal/cycles.log") as f:
    lines = f.readlines()
    recent_full = [l for l in lines if l.strip().startswith("2026-10-23") and "(FULL cycle" in l]

log_line = f"{ts} cycle done: settled {0}, placed {0}, cash ${963.80} (FULL, operator machine, paper; sync: fetch ok, main == origin/main dab5e74, tip 09:57Z ~2h old, no collision; lease: acquired true, written true; pacing: pointer elapsed -> FULL, FULL count 24h = 19 (grep); CI: ci.py status none for dab5e74; GAMMA/CLOB DOWN: resolve.py Errno 54 on all ids, forecast.py record CLOB HTTP 451; scan: 138 screened across 7 batches (day 13/150); research/forecast/bets skipped: CLOB HTTP 451, gamma Errno 54 reset on all ids; open positions: {open_pos}; schedule: next FULL 13:30Z (criterion b); proposal 2026-10-20 updated; push left to loop.sh)\n"

with open("journal/cycles.log", "a") as f:
    f.write(log_line)
print(f"Appended to cycles.log: open_pos={open_pos}")