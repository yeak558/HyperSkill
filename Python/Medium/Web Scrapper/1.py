import requests

url = input("Input the URL:\n> ")
response = requests.get(url)
if "content" in response.json().keys():
    print(response.json()["content"])
else:
    print("Invalid quote resource!")
