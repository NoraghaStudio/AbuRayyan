import re
import json

with open("0 تقييم - ابوريان خبير فحص سيارات _ موقع حراج.html", "r", encoding="utf-8") as f:
    html = f.read()

# Pattern to find blocks
# <div class="bg-background-card relative grid rounded-2xl p-4 shadow"> ... </div>
blocks = html.split('bg-background-card relative grid rounded-2xl p-4 shadow')

reviews = []
for block in blocks[1:]:
    name_match = re.search(r'<span class="mt-1 text-sm">([^<]+)</span>', block)
    date_match = re.search(r'<div class="text-em-4 mt-1 border-\[#a9bdd5\]">([^<]+)</div>', block)
    text_match = re.search(r'<div class="text-em-2 m-0 max-w-full self-start overflow-hidden break-words px-1 py-4"[^>]*>([^<]+)</div>', block)
    
    if name_match and date_match and text_match:
        reviews.append({
            "name": name_match.group(1).strip(),
            "date": date_match.group(1).strip(),
            "text": text_match.group(1).strip(),
            "rating": "positive"
        })

print(f"Extracted {len(reviews)} reviews.")

with open("extracted_reviews.json", "w", encoding="utf-8") as f:
    json.dump(reviews, f, ensure_ascii=False, indent=4)

