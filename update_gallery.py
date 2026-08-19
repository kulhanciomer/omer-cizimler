import os
import json
import re

base_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(base_dir, "assets", "images")
index_html_path = os.path.join(base_dir, "index.html")

valid_extensions = ('.png', '.jpg', '.jpeg', '.webp', '.gif')

image_paths = []
for root, dirs, files in os.walk(images_dir):
    for file in files:
        if file.lower().endswith(valid_extensions):
            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_dir).replace("\\", "/")
            image_paths.append(rel_path)

image_paths.sort()

with open(index_html_path, "r", encoding="utf-8") as f:
    content = f.read()

new_array_json = json.dumps(image_paths, indent=12)
pattern = r'const imageList = \[[\s\S]*?\];'
replacement = f'const imageList = {new_array_json};'

new_content = re.sub(pattern, replacement, content)

with open(index_html_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"Guncellendi! Toplam {len(image_paths)} adet gorsel eklendi.")
