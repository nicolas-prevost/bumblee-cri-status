import requests
import json
from pythonping import ping

def main():
    r = requests.get("https://devou.ps/api/v1/endpoints/statuses?page=1")
    parsed = json.loads(r.text)

    last_status = parsed[28]["results"][-1]
    ret = last_status["success"]
    print(json.dumps(ret, indent=4))
    return ret

main()
