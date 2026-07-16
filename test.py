import httpx

try:
    r = httpx.get("https://openrouter.ai", verify=False)
    print(r.status_code)
except Exception as e:
    print(e)