import urllib.request, json
url = 'https://gamma-api.polymarket.com/markets/1193094'
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    resp = urllib.request.urlopen(req, timeout=10)
    data = json.load(resp)
    print('gamma OK:', resp.status, data.get('question','')[:60])
except Exception as e:
    print('gamma FAIL:', type(e).__name__, str(e)[:100])