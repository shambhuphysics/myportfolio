import os
import bs4

with open('index.html', 'r', encoding='utf-8') as f:
    soup = bs4.BeautifulSoup(f, 'html.parser')

items = [
    ("Research Projects", "projects"),
    ("Awards", "awards"),
    ("Gallery", "gallery"),
    ("Wellbeing", "wellbeing"),
    ("Machine Learning", "machine_learning"),
    ("Quantum Alg", "quantum"),
    ("Physics & Chem", "physics")
]

# 1. Update navigation menu
menu = soup.find('ul', class_='menu')
for title, key in items:
    if not menu.find('a', href=f"#{key}"):
        li = soup.new_tag('li')
        a = soup.new_tag('a', href=f"#{key}", class_="menu-btn")
        a.string = title
        li.append(a)
        menu.append(li)

# 2. Insert sections
# Find the contact section or script footer to insert before
insert_before = soup.find('section', class_='contact')
if not insert_before:
    insert_before = soup.find('footer')

for title, key in items:
    # Remove existing section if we ran this script multiple times
    existing = soup.find('section', id=key)
    if existing:
        existing.decompose()
        
    path = f"extracted/{key}.html"
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content_html = f.read()
        
        # Create section wrapper
        sec = soup.new_tag('section', id=key, **{'class': f'blogger-section {key}'})
        
        container = soup.new_tag('div', **{'class': 'max-width'})
        
        title_h2 = soup.new_tag('h2', **{'class': 'title'})
        title_h2.string = title
        container.append(title_h2)
        
        content_div = soup.new_tag('div', **{'class': 'blogger-content'})
        
        # Parse content as html to append nicely
        content_soup = bs4.BeautifulSoup(content_html, 'html.parser')
        
        content_div.append(content_soup)
        container.append(content_div)
        sec.append(container)
        
        if insert_before:
            insert_before.insert_before(sec)
        else:
            soup.append(sec)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Successfully injected new sections!")
