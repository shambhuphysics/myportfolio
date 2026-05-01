import os
import re
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed

targets = {
    "Research": "projects",
    "Awards": "awards",
    "Gallery": "gallery",
    "Wellbeing": "wellbeing",
    "Machine Learning": "machine_learning",
    "Quantum Alg": "quantum",
    "Physics and Chem": "physics",
}

def get_target_key(title):
    if not title: return None
    title = title.lower()
    if 'research' in title: return 'projects'
    if 'award' in title: return 'awards'
    if 'gallery' in title: return 'gallery'
    if 'wellbeing' in title: return 'wellbeing'
    if 'machine learning' in title: return 'machine_learning'
    if 'quantum' in title: return 'quantum'
    if 'physics' in title: return 'physics'
    return None

def download_image(url, save_path):
    # Skip if exists and not empty
    if os.path.exists(save_path) and os.path.getsize(save_path) > 0:
        return True
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response, open(save_path, 'wb') as out_file:
            out_file.write(response.read())
        return True
    except Exception as e:
        print(f"Failed {url}: {e}")
        return False

if not os.path.exists("images"): os.makedirs("images")
if not os.path.exists("extracted"): os.makedirs("extracted")

tree = ET.parse('Blogger/Blogs/My research portfolio/feed.atom')
root = tree.getroot()
namespaces = {'atom': 'http://www.w3.org/2005/Atom'}

downloads = []

for entry in root.findall('atom:entry', namespaces):
    title_elem = entry.find('atom:title', namespaces)
    title = title_elem.text if title_elem is not None else ''
    content_elem = entry.find('atom:content', namespaces)
    content = content_elem.text if content_elem is not None else ''
    
    key = get_target_key(title)
    if key and content:
        print(f"Extracting {title} -> {key}")
        img_folder = os.path.join("images", key)
        if not os.path.exists(img_folder): os.makedirs(img_folder)
            
        imgs = re.findall(r'<img[^>]+src=["\'](.*?)["\']', content)
        for i, img_url in enumerate(imgs):
            ext = ".jpg"
            if ".png" in img_url.lower(): ext = ".png"
            if ".gif" in img_url.lower(): ext = ".gif"
            
            img_filename = f"{key}_{i+1}{ext}"
            img_path = os.path.join(img_folder, img_filename)
            rel_path = f"images/{key}/{img_filename}"
            
            downloads.append((img_url, img_path))
            content = content.replace(img_url, rel_path)
        
        with open(f"extracted/{key}.html", "w") as f:
            f.write(content)

print(f"Starting {len(downloads)} downloads...")
with ThreadPoolExecutor(max_workers=20) as executor:
    futures = [executor.submit(download_image, u, p) for u, p in downloads]
    for i, fut in enumerate(as_completed(futures)):
        pass
print("Done extracting sections.")
