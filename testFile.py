# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests",
# ]
# ///
import requests

# pip install requests

def get_json(url, params=None, headers=None, timeout=10):
    try:
        resp = requests.get(url, params=params, headers=headers, timeout=timeout)
        resp.raise_for_status()
        return resp.json()  # use resp.text for raw string
    except requests.RequestException as e:
        print("Request failed:", e)
        return None

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = get_json(url)
    print(data)