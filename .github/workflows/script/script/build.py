import yaml

data = yaml.safe_load(open("raw/proxies.yaml"))

out = {
    "proxies": data.get("proxies", []),
    "mode": "rule",
    "port": 7890
}

yaml.dump(out, open("output/clash.yaml","w"), allow_unicode=True)
