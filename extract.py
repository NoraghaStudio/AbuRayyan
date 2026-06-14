import json
from bs4 import BeautifulSoup

with open("0 تقييم - ابوريان خبير فحص سيارات _ موقع حراج.html", "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

# Haraj typically uses articles or specific divs for comments
# Let's just dump some potential elements to see their structure
# Or we can look at the text of the known reviews
known_review_text = "تعاملت مع ابوريان خبير فحص سيارات والرجال صادق وأمين"
el = soup.find(string=lambda t: t and known_review_text in t)
if el:
    parent = el.parent
    for _ in range(5):
        print(parent.name, parent.get("class"))
        parent = parent.parent
