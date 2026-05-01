import xml.etree.ElementTree as ET

tree = ET.parse('Blogger/Blogs/My research portfolio/feed.atom')
root = tree.getroot()
namespaces = {'atom': 'http://www.w3.org/2005/Atom'}

for entry in root.findall('atom:entry', namespaces):
    title_elem = entry.find('atom:title', namespaces)
    title = title_elem.text if title_elem is not None else 'No Title'
    
    content_elem = entry.find('atom:content', namespaces)
    content = content_elem.text if content_elem is not None else 'No Content'
    
    print(f'TITLE: {title}')
    print(f'BODY LENGTH: {len(content) if content else 0}')
    print(f'SNIPPET: {content[:200] if content else ""}')
    print('-' * 40)
