import requests
import json
from pythonping import ping

def main():
    r = requests.get("https://devou.ps/api/v1/endpoints/statuses?page=1")
    parsed = json.loads(r.text)

    last_status = parsed[28]["results"][-1]
    print(json.dumps(last_status, indent=4))

main()
