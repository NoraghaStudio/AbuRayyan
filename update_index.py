import json
import re

with open("extracted_reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

reviews_json = json.dumps(reviews, ensure_ascii=False, indent=12)

# Replace the reviews array in the javascript
pattern = r"const reviews = \[\n(.*?)\n        \];"
replacement = f"const reviews = {reviews_json};"

new_html = re.sub(pattern, replacement, html, flags=re.DOTALL)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(new_html)

print("Updated index.html")
