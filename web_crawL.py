import sys
import requests
from bs4 import BeautifulSoup

# Defina a string com o ASCII art
ascii_art = """
  ::::::::  :::::::::      :::     :::       ::: :::        ::::::::::: ::::    :::  :::::::: 
    :+:    :+: :+:    :+:   :+: :+:   :+:       :+: :+:            :+:     :+:+:   :+: :+:    :+: 
   +:+        +:+    +:+  +:+   +:+  +:+       +:+ +:+            +:+     :+:+:+  +:+ +:+         
  +#+        +#++:++#:  +#++:++#++: +#+  +:+  +#+ +#+            +#+     +#+ +:+ +#+ :#:          
 +#+        +#+    +#+ +#+     +#+ +#+ +#+#+ +#+ +#+            +#+     +#+  +#+#+# +#+   +#+#    
#+#    #+# #+#    #+# #+#     #+#  #+#+# #+#+#  #+#            #+#     #+#   #+#+# #+#    #+#     
########  ###    ### ###     ###   ###   ###   ########## ########### ###    ####  ########        
"""

# Imprima o ASCII art
print(ascii_art)
print("=====================dev-rdidcdadrddodadzdedv.v1======================")

# Códigos ANSI para cores
GREEN = '\033[92m'
RESET = '\033[0m'

to_crawl = []
crawled = set()

def make_request(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Levanta uma exceção para status de erro HTTP
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def get_links(html):
    links = []
    try:
        soup = BeautifulSoup(html, "html.parser")
        tags_a = soup.find_all("a", href=True)
        for tag in tags_a:
            link = tag["href"]
            if link.startswith("http"):
                links.append(link)
    except Exception as error:
        print(f"Error parsing HTML: {error}")
    return links

def crawl():
    while to_crawl:
        url = to_crawl.pop()
        if url in crawled:
            continue
        print(f"crawling {GREEN}{url}{RESET}")
        html = make_request(url)
        if html:
            links = get_links(html)
            for link in links:
                if link not in crawled and link not in to_crawl:
                    to_crawl.append(link)
            crawled.add(url)
        else:
            crawled.add(url)
    print("Done")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        url = sys.argv[1]
        to_crawl.append(url)
        crawl()
    else:
        print("Usage: python web_CrawL.py <url>")
