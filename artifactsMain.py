import requests
import time
import sys

server = "https://api.artifactsmmo.com"
token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Imd3aXp6bGU2NTFAcHJvdG9uLm1lIiwicGFzc3dvcmRfY2hhbmdlZCI6bnVsbH0.xYCN6dSw-w8YytEbNZ9tBuuTCNfH8mz8uE9DJVlbX_E"
character = "gwizzler"
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Authorization": f"Bearer {token}",
}

def customQuit():
    print("\nStopping the program.\n")
    sys.exit(0)

def jsonDataPostAndGet(url, headers, data):
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        json_data = response.json()
        print(f"{json_data.get("data")}\n")
    except requests.exceptions.RequestException as error:
        print(f"{error}\n")

def movement(server, character, headers):
    url = f"{server}/my/{character}/action/move"
    data = {"x": 2, "y": 1}

    jsonDataPostAndGet(url, headers, data)

def fight(server, character, headers):
    url = f"{server}/my/{character}/action/fight"
    data = {"x": 0, "y": 1}

    jsonDataPostAndGet(url, headers, data)

def gather(server, character, headers):
    url = f"{server}/my/{character}/action/gathering"
    data = {"x": 0, "y": 1}

    jsonDataPostAndGet(url, headers, data)

def heal(server, character, headers):
    url = f"{server}/my/{character}/action/rest"
    data = {"x": 0, "y": 1}

    jsonDataPostAndGet(url, headers, data)

def craft(server, character, headers):
    url = f"{server}/my/{character}/action/crafting"
    data = {"code": "wooden_staff", "quantity": 1}

    jsonDataPostAndGet(url, headers, data)

if __name__ == "__main__":
    while True:
        print("[0] Quit\n[1] Move\n[2] Fight\n[3] Gather\n[4] Heal\n")
        actionToTake = input(">")
        print("\n\n")

        if actionToTake == "0":
            customQuit()
        elif actionToTake == "1":
            movement(server, character, headers)
        elif actionToTake == "2":
            fight(server, character, headers)
        elif actionToTake == "3":
            gather(server, character, headers)
        elif actionToTake == "4":
            heal(server, character, headers)
        elif actionToTake == "5":
            craft(server, character, headers)
        else:
            print("An error occurred.\n")

