import requests
from bs4 import BeautifulSoup
import json
import time
from urllib.parse import urlparse, urljoin

json_count = 0
beginner_count = 0
intermediate_count = 0
advanced_count = 0

def fetch_html(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def extract_links_with_data_selector(soup, base_url, data_selector):
    links = []
    div_elements = soup.find_all('div', attrs={'data-selector': data_selector})
    for div_element in div_elements:
        for a_tag in div_element.find_all('a', href=True):
            link = urljoin(base_url, a_tag['href'])
            parsed_base_url = urlparse(base_url)
            parsed_link = urlparse(link)
            parsed_authorized_link = urlparse("https://raw.githubusercontent.com/sanderland/tsumego/master/problems/1a.%20Tsumego%20Beginner/Cho%20Chikun%20Encyclopedia%20Life%20And%20Death%20-%20Elementary/Prob0001.json")
            
            if parsed_base_url.netloc == parsed_link.netloc or parsed_link.netloc == parsed_authorized_link.netloc : # 'raw.githubusercontent.com':
                links.append(link)
    return links

def fetch_json(url):
    try:
        response = requests.get(url, timeout=10)
        #time.sleep(2)
        response.raise_for_status()
        print(response.json())
        return response.json()
    except (requests.RequestException, json.JSONDecodeError) as e:
        print(f"Failed to fetch or parse JSON from {url}: {e}")
        return None

def crawl_and_extract(url, visited_urls=set(), json_contents=[], data_selector='repos-split-pane-content'):
    global json_count, beginner_count, intermediate_count, advanced_count
    if json_count >= 90:
        return
    if 'commits' in url or 'Tesuji' in url:
        return
    if beginner_count >= 30 and 'Beginner' in url:
        return
    if intermediate_count >= 30 and 'Intermediate' in url:
        return
    if advanced_count >= 30 and 'Advanced' in url:
        return
    
    if url in visited_urls:
        return
    
    visited_urls.add(url)
    print(f"Visiting: {url}")
    
    html = fetch_html(url)
    time.sleep(3)
    if html is None:
        return

    soup = BeautifulSoup(html, 'html.parser')
    links = extract_links_with_data_selector(soup, url, data_selector)

    # Trie les liens pour assurer un ordre déterministe
    links.sort()
    
    for link in links:
        if link.endswith('.json') and 'raw' in link:
            if json_count < 90:
                json_data = fetch_json(link)
                time.sleep(3)
                if json_data:
                    if 'Beginner' in link:
                        json_data['difficulty'] = "BEG"
                        beginner_count += 1
                    if 'Intermediate' in link:
                        json_data['difficulty'] = "INT"
                        intermediate_count += 1
                    if 'Advanced' in link:
                        json_data['difficulty'] = "ADV"
                        advanced_count += 1
                    json_contents.append(json_data)
                    json_count += 1
                    if json_count >= 90 or (beginner_count >= 30 and intermediate_count >= 30 and advanced_count >= 30):
                        break
            else:
                break
        else:
            crawl_and_extract(link, visited_urls, json_contents, data_selector)
        
        # Pour éviter de surcharger le serveur avec des requêtes rapides
        #time.sleep(1)
    print(beginner_count, intermediate_count, advanced_count, json_count)
    return json_contents

def save_json_to_file(json_data, filename):
    with open(filename, 'w') as f:
        json.dump(json_data, f, indent=4)
    print(f"JSON data saved to {filename}")

# URL de départ pour l'exploration
start_url = 'https://github.com/sanderland/tsumego/tree/master/problems'

# Démarrer le processus de crawl
json_results = crawl_and_extract(start_url, data_selector='repos-split-pane-content')

# Enregistrer les contenus JSON récupérés dans un fichier
save_json_to_file(json_results, 'tsumegos.json')

#https://raw.githubusercontent.com/sanderland/tsumego/master/problems/1a.%20Tsumego%20Beginner/Cho%20Chikun%20Encyclopedia%20Life%20And%20Death%20-%20Elementary/Prob0001.json

#https://github.com/sanderland/tsumego/blob/master/problems/1a.%20Tsumego%20Beginner/Cho%20Chikun%20Encyclopedia%20Life%20And%20Death%20-%20Elementary/Prob0001.json

#https://github.com/sanderland/tsumego/raw/master/problems/1a.%20Tsumego%20Beginner/Cho%20Chikun%20Encyclopedia%20Life%20And%20Death%20-%20Elementary/Prob0001.json