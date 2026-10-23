import sys, json
lines = sys.stdin.readlines()
data = [json.loads(l) for l in lines if 'divergence' in l and 'null' not in l]
data.sort(key=lambda x: x['divergence'], reverse=True)
for d in data[:20]:
    print(f'{d["market_id"]} | div={d["divergence"]:.4f} | conf={d["confidence"]} | {d["question"][:80]}')