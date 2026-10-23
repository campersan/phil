import subprocess
import sys

market_ids = [
    ("2941849", "No", 0.88, "econ-rates"),
    ("682708", "No", 0.65, "politics-general"),
    ("1194643", "No", 0.25, "politics-general"),
    ("608547", "No", 0.55, "awards"),
    ("5774489", "TheMongolz", 0.48, "esports"),
    ("1892487", "No", 0.75, "wnba-futures"),
    ("4881660", "No", 0.28, "politics-general"),
    ("5534122", "No", 0.38, "soccer"),
    ("3358720", "Yes", 0.35, "news"),
    ("5929769", "No", 0.58, "say-the-word"),
    ("3554659", "No", 0.30, "ai-leaderboard"),
    ("5774522", "Nemiga", 0.45, "esports"),
    ("4881547", "Yes", 0.25, "politics-general"),
    ("4881548", "No", 0.22, "politics-general"),
    ("4881659", "No", 0.78, "politics-general"),
    ("5523020", "Merab Dvalishvili", 0.58, "mma"),
    ("5167211", "No", 0.85, "geopolitics"),
    ("5167210", "No", 0.85, "geopolitics"),
]

strategy_rev = "dab5e74"

for market_id, outcome, est_prob, category in market_ids:
    cmd = [
        sys.executable, "core/forecast.py", "record",
        "--market-id", market_id,
        "--outcome", outcome,
        "--est-prob", str(est_prob),
        "--category", category,
        "--skip-reason", "no-edge",
        "--strategy-rev", strategy_rev
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print(f"OK: {market_id} {outcome} {est_prob}")
            if result.stdout.strip():
                print(f"  -> {result.stdout.strip()}")
        else:
            print(f"FAIL: {market_id} {outcome} {est_prob}")
            if result.stderr.strip():
                print(f"  -> {result.stderr.strip()[:200]}")
    except Exception as e:
        print(f"ERROR: {market_id} - {e}")