import json
import re

with open("extracted_reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

reviews_json = json.dumps(reviews, ensure_ascii=False, indent=12)

# Find the start and end of the reviews array
start_marker = "const reviews = ["
end_marker = "];\n\n        let visibleCount = 9;"

start_idx = html.find(start_marker)
end_idx = html.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + f"const reviews = {reviews_json};" + html[end_idx:]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Updated index.html successfully")
else:
    print("Could not find the reviews array markers in index.html")
