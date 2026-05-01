import re, sys

def analyze(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n=== {path} ===")
    
    # SVG root attributes
    m = re.search(r'<svg[^>]*>', content[:2000])
    if m:
        tag = m.group(0)
        for attr in ['width', 'height', 'viewBox', 'preserveAspectRatio']:
            am = re.search(rf'{attr}="([^"]*)"', tag)
            if am:
                print(f"  {attr}: {am.group(1)}")
    
    # Image positions
    for m in re.finditer(r'<image[^>]*>', content):
        tag = m.group(0)[:500]
        x = re.search(r'\bx="([^"]*)"', tag)
        y = re.search(r'\by="([^"]*)"', tag)
        w = re.search(r'\bwidth="([^"]*)"', tag)
        h = re.search(r'\bheight="([^"]*)"', tag)
        t = re.search(r'transform="([^"]*)"', tag)
        if x or y or t:
            print(f"  image: x={x and x.group(1)} y={y and y.group(1)} w={w and w.group(1)} h={h and h.group(1)} transform={t and t.group(1)}")
    
    # Group transforms
    for m in re.finditer(r'<g[^>]*transform="([^"]*)"', content):
        print(f"  g transform: {m.group(1)}")
    
    # Path starting coordinates
    for m in re.finditer(r'd="([^"]{0,200})', content):
        d = m.group(1)
        # Extract first M/m command coordinates
        mc = re.match(r'[Mm]\s*([-\d.]+)[,\s]+([-\d.]+)', d)
        if mc:
            print(f"  path start: ({mc.group(1)}, {mc.group(2)})")

    # Text elements
    for m in re.finditer(r'<text[^>]*>', content):
        tag = m.group(0)
        x = re.search(r'\bx="([^"]*)"', tag)
        y = re.search(r'\by="([^"]*)"', tag)
        t = re.search(r'transform="([^"]*)"', tag)
        if x or y or t:
            print(f"  text: x={x and x.group(1)} y={y and y.group(1)} transform={t and t.group(1)}")

for path in [
    '.demo/assets/steve-yegges-levels.svg',
    '.demo/assets/kubler-ross-change-curve.svg',
    '.demo/assets/models-and-tools-1.svg',
    '.demo/assets/quebec-bridge.svg',
]:
    analyze(path)
