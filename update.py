with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find where 'const reviews = [' is
start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if 'const reviews = [' in line:
        start_idx = i
        break

if start_idx != -1:
    for i in range(start_idx, len(lines)):
        if '];' in lines[i]:
            end_idx = i
            break

if start_idx != -1 and end_idx != -1:
    del lines[start_idx:end_idx+1]
    lines.insert(start_idx, '    <script src="reviews-data.js"></script>\n')

# Find the DOMContentLoaded block to remove text overrides and add storage listener
content = "".join(lines)
# We will just replace it cleanly.
