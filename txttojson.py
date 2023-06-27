import os
import json

# Read the train2.txt file on the desktop and convert it to a list of dictionaries
with open(os.path.expanduser("~/Desktop/train2.txt"), "r", encoding='utf-8') as f:
    lines = f.readlines()
    data = []
    for line in lines:
        if "\", \"summary\": \"" in line:
            content, summary = line.split("\", \"summary\": \"")
            modified_content = content.replace("{\"content\": \"", "")
            modified_summary = summary.replace("\"}", "")
            data.append({"content": modified_content.strip(), "summary": modified_summary.strip()})
        else:
            print(line)

# Write the list of dictionaries to a json file on the desktop
with open(os.path.expanduser("~/Desktop/train2.json"), "w", encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

