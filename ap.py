import requests


url = "https://corona.lmao.ninja/v2/all?yesterday"

resp = requests.get(url)

# print(resp.status_code)
print(resp.text)