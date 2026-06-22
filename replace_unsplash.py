import re
from pathlib import Path

pattern = re.compile(r"https://images\.unsplash\.com/[^\"')\s]+")
root = Path('.')
total = 0
for path in root.rglob('*'):
    if path.suffix.lower() in {'.html', '.js', '.css'}:
        text = path.read_text(encoding='utf-8')
        found = pattern.findall(text)
        if found:
            replacement = 'Pics/1.jpeg'
            new = pattern.sub(replacement, text)
            path.write_text(new, encoding='utf-8')
            print(f'Updated {path}: {len(found)} replacements')
            total += len(found)
print('TOTAL', total)
