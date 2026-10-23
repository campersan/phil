import json
with open('journal/ledger.jsonl') as f:
    lines = f.readlines()
    settled = [l for l in lines if json.loads(l).get('status') in ('won', 'lost')]
    print(f'Total settled bets: {len(settled)}')
    open_pos = [l for l in lines if json.loads(l).get('status') == 'open']
    print(f'Open positions: {len(open_pos)}')
    for op in open_pos:
        d = json.loads(op)
        print(f'  {d["id"][:8]} market={d["market_id"]} outcome={d["outcome"]} est={d["est_prob"]} cat={d["category"]}')