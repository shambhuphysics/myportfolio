from bs4 import BeautifulSoup as bs
import sys

def dec(s):
    return (s.replace('\\u003c','<').replace('\\u003e','>')
             .replace('\\u003d','=').replace('\\u0022','"')
             .replace('\\u0026amp;','&').replace('\\u0026','&')
             .replace('\\u0027',"'").replace('\\"','"').replace('\\\\"', '"')
             .replace('\\n', '\n'))

path = "/home/sam/Downloads/Awarts_and_certificates_files/Awarts_and_certificates.html"
with open(path,'r',errors='ignore') as f:
    raw = f.read()
    raw = dec(raw)

soup = bs(raw, 'html.parser')
with open('/tmp/pretty.html', 'w') as out:
    out.write(soup.prettify())
print("Wrote to /tmp/pretty.html")
