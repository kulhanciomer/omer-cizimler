import os
import json
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(base_dir, "assets", "images")
index_html_path = os.path.join(base_dir, "index.html")

valid_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.gif')

# Known personal photo filenames
known_photos = [
    "assets/images/posts/17880326874513014.jpg",
    "assets/images/posts/202308/17933116184722426.webp",
    "assets/images/posts/17887721037521191.jpg",
    "assets/images/posts/18057252041355413.jpg"
]

drawings = []
photos = []

for root, dirs, files in os.walk(images_dir):
    for file in files:
        if file.lower().endswith(valid_extensions):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir).replace("\\", "/")
            
            # Check if it's in a photos subfolder or matches known photo list
            if "photos" in rel_path.lower() or rel_path in known_photos:
                photos.append(rel_path)
            else:
                drawings.append(rel_path)

drawings.sort()
photos.sort()

with open(index_html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace drawings array
new_drawings_json = json.dumps(drawings, indent=12)
content = re.sub(r'const drawingList = \[[\s\S]*?\];', f'const drawingList = {new_drawings_json};', content)

# Replace photos array
new_photos_json = json.dumps(photos, indent=12)
content = re.sub(r'const photoList = \[[\s\S]*?\];', f'const photoList = {new_photos_json};', content)

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Guncellendi! {len(drawings)} Cizim, {len(photos)} Fotograf eklendi.")
