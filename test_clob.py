import urllib.request, json
try:
    req = urllib.request.Request('https://clob.polymarket.com/time', headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req, timeout=10)
    print('CLOB time:', json.load(resp))
except Exception as e:
    print('CLOB time FAIL:', type(e).__name__, str(e)[:200])