import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--url")
args = parser.parse_args()

url = args.url
print("GET method test")
response = requests.get(url)
assert response.status_code == 200
print("success")
print(response.text)

print("POST method test")
params = {"src":"hogehoge","ref":"fugafuga"}
response = requests.get(url,json.dump(params),header={'Content-Type': 'application/json'})
print(response.status_code)
print(response.text)

