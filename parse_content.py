from bs4 import BeautifulSoup as bs
import re, json

files = {
    "my_project": "/home/sam/Downloads/my_project_files/my_project.html",
    "awards": "/home/sam/Downloads/Awarts_and_certificates_files/Awarts_and_certificates.html",
    "physics": "/home/sam/Downloads/Physics_and_Chemistry_files/Physics_and_Chemistry.html",
    "quantum": "/home/sam/Downloads/ℚ⟨ψ|  Quantum Algorithm_files/ℚ⟨ψ|  Quantum Algorithm.html",
    "useful": "/home/sam/Downloads/Useful_sites_files/Useful_sites.html",
    "scholar": "/home/sam/Downloads/_Shambhu Bhandari Sharma_ - _Google Scholar__files/_Shambhu Bhandari Sharma_ - _Google Scholar_.html",
    "wellbeing": "/home/sam/Downloads/wellbeing_files/wellbeing.html",
    "gallery": "/home/sam/Downloads/Gallery_files/Gallery.html",
    "routine": "/home/sam/Downloads/Routine_files/Routine.html",
}

def dec(s):
    return (s.replace('\\u003c','<').replace('\\u003e','>')
             .replace('\\u003d','=').replace('\\u0022','"')
             .replace('\\u0026amp;','&').replace('\\u0026','&')
             .replace('\\u0027',"'").replace('\\"','"').replace('\\\\"', '"')
             .replace('\\n', '\n'))

for name, path in files.items():
    try:
        with open(path,'r',errors='ignore') as f:
            raw = f.read()
            raw = dec(raw)
        soup = bs(raw, 'html.parser')
        bodies = soup.find_all(class_='post-body')
        print(f"\n{name.upper()}: Found {len(bodies)} post bodies")
        if bodies:
            # show snippet
            txt = bodies[0].get_text(separator=' ', strip=True)
            print(f"Content format preview: {txt[:200]}")
    except Exception as e:
        print(f"{name}: error {e}")
