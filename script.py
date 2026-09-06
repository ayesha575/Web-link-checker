import requests

def check_links(filename):
    with open(filename, 'r') as file:
        urls = file.readlines()
        
    for url in urls:
        url = url.strip()
        if not url:
            continue
        try:
            response = requests.get(url, timeout=5)
            print(f"[{response.status_code}] {url}")
        except requests.exceptions.RequestException:
            print(f"[FAILED] {url}")

if __name__ == "__main__":
    check_links("urls.txt")