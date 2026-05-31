import requests, yaml

urls = open("sources.txt").read().splitlines()

proxies = []

for url in urls:
    try:
        data = yaml.safe_load(requests.get(url, timeout=15).text)
        if isinstance(data, dict) and "proxies" in data:
            proxies += data["proxies"]
    except:
        pass

yaml.dump({"proxies": proxies}, open("raw/proxies.yaml","w"))
