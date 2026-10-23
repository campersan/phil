import json
with open('journal/ledger.jsonl') as f:
    for line in f:
        d = json.loads(line)
        if d.get('closed') == False:
            print(f"{d['id']} | {d['market_id']} | {d['outcome']} | stake={d['stake']} | est={d['est_prob']} | edge_class={d.get('edge_class')} | category={d.get('category')}")