import json

with open('journal/ledger.jsonl') as f:
    lines = f.readlines()

open_positions = [json.loads(l) for l in lines if json.loads(l).get('closed') == False]
print(f'Open positions: {len(open_positions)}')

cash = 1000.0  # approximate starting
for l in lines:
    d = json.loads(l)
    if d.get('status') == 'won':
        cash += d.get('pnl_usd', 0)
    elif d.get('status') == 'lost':
        cash += d.get('pnl_usd', 0)
    elif d.get('status') == 'open':
        pass
print(f'Approx cash: ${cash:.2f}')
for op in open_positions:
    print(f'  {op["id"]} | {op["market_id"]} | {op["outcome"]} | stake={op["stake_usd"]}')