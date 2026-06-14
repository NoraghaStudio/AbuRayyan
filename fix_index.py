import json

with open("extracted_reviews.json", "r", encoding="utf-8") as f:
    reviews = json.load(f)

reviews_json = json.dumps(reviews, ensure_ascii=False, indent=12)

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Instead of regex, we can just find the start and end of the reviews array.
start_idx = html.find("const reviews = [")
end_idx = html.find("];\n\n        let visibleCount")

if start_idx != -1 and end_idx != -1:
    new_html = html[:start_idx] + f"const reviews = {reviews_json};\n\n        let visibleCount" + html[end_idx + len("];\n\n        let visibleCount"):]
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
    print("Fixed index.html")
else:
    print("Could not find the injection markers")
