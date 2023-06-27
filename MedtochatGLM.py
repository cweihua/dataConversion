

import os

with open(os.path.expanduser("~/Desktop/train.txt"), "r", encoding='utf-8') as f:
    lines = f.readlines()
    modified_lines = []
    for line in lines:
        modified_line = line.replace("问题：", "")
        modified_line = modified_line.replace("\\n回答: ", "")
        modified_line = modified_line.replace("context", "content")
        modified_line = modified_line.replace("target", "summary")
        modified_lines.append(modified_line)
    with open(os.path.expanduser("~/Desktop/train2.txt"), "w", encoding='utf-8') as f2:
        f2.writelines(modified_lines)

