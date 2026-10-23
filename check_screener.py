import json
with open('journal/screener.jsonl') as f:
    lines = f.readlines()
today = [json.loads(l) for l in lines if l.startswith('{"ts": "2026-10-23T')]
today_sorted = sorted([t for t in today if t.get('divergence') is not None], key=lambda x: x['divergence'], reverse=True)
for t in today_sorted[:20]:
    print(f'{t["market_id"]} | div={t["divergence"]:.4f} | conf={t["confidence"]} | {t["question"][:80]}')