import re
sample = "url('https://images.unsplash.com/photo-1528740561666-dc2479dc08ab?q=80&w=1800') center/cover no-repeat;"
pattern = re.compile(r"https://images\.unsplash\.com/[^\"')\s]+")
print('pattern', pattern.pattern)
print('matches', pattern.findall(sample))
