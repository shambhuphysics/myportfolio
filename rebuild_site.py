import os
import bs4
import xml.etree.ElementTree as ET

# Info about the pages
items = [
    ("Research", "projects"),
    ("Awards & Certs", "awards"),
    ("Gallery", "gallery"),
    ("Wellbeing", "wellbeing"),
    ("Machine Learning", "machine_learning"),
    ("Quantum Computing", "quantum"),
    ("Physics & Chemistry", "physics")
]

# Get titles and snippets from feed.atom
tree = ET.parse('Blogger/Blogs/My research portfolio/feed.atom')
root = tree.getroot()
namespaces = {'atom': 'http://www.w3.org/2005/Atom'}

snippets = {}
for entry in root.findall('atom:entry', namespaces):
    title_elem = entry.find('atom:title', namespaces)
    title = title_elem.text.strip() if (title_elem is not None and title_elem.text is not None) else ''
    content_elem = entry.find('atom:content', namespaces)
    content = content_elem.text if (content_elem is not None and content_elem.text is not None) else ''
    
    # Strip HTML tags naively for snippet
    import re
    text = re.sub('<[^<]+>', ' ', content).strip()
    text = re.sub('\\s+', ' ', text)
    snippet = text[:150] + "..." if len(text) > 150 else text
    
    tl = title.lower()
    key = None
    if 'research' in tl: key = 'projects'
    elif 'award' in tl: key = 'awards'
    elif 'gallery' in tl: key = 'gallery'
    elif 'wellbeing' in tl: key = 'wellbeing'
    elif 'machine learning' in tl: key = 'machine_learning'
    elif 'quantum' in tl: key = 'quantum'
    elif 'physics' in tl: key = 'physics'
    
    if key:
        snippets[key] = {
            "title": title.replace('🔬', '').replace('📑', '').replace('🖼', '').replace('🏃', '').replace('ℚ⟨ψ|', '').replace('⚛', '').replace('ൎȰȱ', '').strip(), 
            "snippet": snippet
        }

# 1. Clean index.html
with open('index.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

for display_name, key in items:
    sec = soup.find('section', id=key)
    if sec:
        # Clear it up and rebuild as a Card
        sec.clear()
        
        container = soup.new_tag('div', **{'class': 'max-width'})
        title_h2 = soup.new_tag('h2', **{'class': 'title'})
        title_h2.string = display_name
        container.append(title_h2)
        
        card_grid = soup.new_tag('div', **{'class': 'card-grid'})
        
        card = soup.new_tag('div', **{'class': 'card'})
        
        # Look for first image
        img_url = f"images/{key}/{key}_1.jpg"
        if not os.path.exists(img_url): img_url = f"images/{key}/{key}_1.png"
        if not os.path.exists(img_url): img_url = "images/profile-1.jpeg" # fallback
        
        card_img = soup.new_tag('div', **{'class': 'card-img'})
        card_img['style'] = f"background-image: url('{img_url}');"
        card.append(card_img)
        
        card_content = soup.new_tag('div', **{'class': 'card-content'})
        c_title = soup.new_tag('h3')
        c_title.string = snippets.get(key, {}).get("title", display_name)
        card_content.append(c_title)
        
        c_p = soup.new_tag('p')
        c_p.string = snippets.get(key, {}).get("snippet", "Explore the interactive insights here...")
        card_content.append(c_p)
        
        c_a = soup.new_tag('a', href=f"{key}.html", **{'class': 'read-more-btn'})
        c_a.string = "Read Full Post "
        
        i_tag = soup.new_tag('i', **{'class': 'fas fa-arrow-right'})
        c_a.append(i_tag)
        card_content.append(c_a)
        
        card.append(card_content)
        card_grid.append(card)
        container.append(card_grid)
        sec.append(container)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))

# 2. Build sub-pages
template = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Shambhu Bhandari Sharma</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&family=Ubuntu:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {{ background: #111; color: #fff; line-height: 1.6; font-family: 'Poppins', sans-serif; }}
        .header {{ padding: 30px 10%; background: #000; border-bottom: 2px solid crimson; display: flex; justify-content: space-between; align-items: center; }}
        .header a {{ color: #fff; font-size: 18px; font-weight: 500; transition: color 0.3s; text-decoration: none; }}
        .header a:hover {{ color: crimson; }}
        .content-container {{ max-width: 1000px; margin: 50px auto; padding: 0 20px; background: #1e1e2d; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); padding-bottom: 50px; overflow: hidden; }}
        .content-container .post-header {{ padding: 40px; background: linear-gradient(135deg, #111, #1a1a2e); border-bottom: 3px solid crimson; margin: 0 -20px 40px -20px; }}
        .content-container .post-header h1 {{ font-family: 'Ubuntu', sans-serif; font-size: 36px; text-align: center; color: #fff; margin:0;}}
        .content-container img {{ max-width: 100%; border-radius: 8px; margin: 20px 0; box-shadow: 0 5px 15px rgba(0,0,0,0.3); }}
        .content-container a {{ color: crimson; text-decoration: underline; }}
        .content-container h2, h3 {{ margin-top: 30px; margin-bottom: 15px; color: crimson; font-family: 'Ubuntu', sans-serif; }}
    </style>
</head>
<body>
    <div class="header">
        <div class="logo"><a href="index.html">Portfo<span>lio.</span></a></div>
        <a href="index.html"><i class="fas fa-home"></i> Back to Home</a>
    </div>
    <div class="content-container">
        <div class="post-header">
            <h1>{title}</h1>
        </div>
        <div class="actual-content">
            {content}
        </div>
    </div>
</body>
</html>
"""

for display_name, key in items:
    path = f"extracted/{key}.html"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content_html = f.read()
        
        full_html = template.format(
            title=snippets.get(key, {}).get("title", display_name),
            content=content_html
        )
        
        with open(f"{key}.html", "w", encoding='utf-8') as f:
            f.write(full_html)

print("Hub restructuring complete.")
