import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_headers(url):
    try:
        response = requests.get(url)
        return response.headers
    except requests.RequestException as e:
        print(f"Error fetching headers for {url}: {e}")
        return {}

def check_security_headers(headers):
    required_headers = [
        "X-Content-Type-Options",
        "Strict-Transport-Security",
        "Content-Security-Policy",
        "X-Frame-Options"
    ]
    
    missing_headers = [header for header in required_headers if header not in headers]
    if missing_headers:
        print(f"Missing security headers: {', '.join(missing_headers)}")

def check_outdated_apache(url, headers):
    if "Server" in headers:
        server_info = headers["Server"]
        if "Apache/2.4.29" in server_info:
            print(f"Outdated Apache version detected on {url}: {server_info}")
        elif "Apache/2.2.34" in server_info:
            print(f"Outdated Apache version detected on {url}: {server_info}")
        elif "Apache/2.4.18" in server_info:
            print(f"Outdated Apache version detected on {url}: {server_info}")

def check_forms(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for form in soup.find_all("form"):
            action = form.get("action")
            method = form.get("method", "GET").upper()
            
            if not action:
                print(f"Form on {url} has no action attribute.")
            if method == "GET":
                print(f"Form on {url} uses GET instead of POST.")
    except requests.RequestException as e:
        print(f"Error scanning forms on {url}: {e}")

def crawl(url, visited=set()):
    if url in visited:
        return
    
    visited.add(url)
    print(f"Scanning {url}...")
    
    headers = get_headers(url)
    check_security_headers(headers)
    
    check_outdated_apache(url, headers)
    
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        
        check_forms(url)

        for link in soup.find_all("a", href=True):
            full_url = urljoin(url, link["href"])
            if full_url.startswith(url):
                crawl(full_url, visited)
    except requests.RequestException as e:
        print(f"Error crawling {url}: {e}")

if __name__ == "__main__":
    start_url = input("Enter the URL to scan: ")
    crawl(start_url)
