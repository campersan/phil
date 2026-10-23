import json
with open('journal/screener.jsonl') as f:
    for line in f:
        if line.startswith('{"ts": "2026-10-23T11:27:52Z"'):
            d = json.loads(line)
            if d.get('divergence') and d['divergence'] > 0.1:
                print(f"{d['market_id']} | div={d['divergence']:.4f} | {d['question'][:100]}")