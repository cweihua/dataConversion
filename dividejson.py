import json
import random
import os

# Read the train2.json file on the desktop and convert it to a list of dictionaries
with open(os.path.expanduser("~/Desktop/train2.json"), "r", encoding='utf-8') as f:
    data = json.load(f)

# Shuffle the data randomly
random.shuffle(data)

# Calculate the index to split the data into train and dev sets
split_index = int(len(data) * 0.7)

# Split the data into train and dev sets
train_data = data[:split_index]
dev_data = data[split_index:]

# Write the train and dev sets to separate json files on the desktop
with open(os.path.expanduser("~/Desktop/train.json"), "w", encoding='utf-8') as f:
    json.dump(train_data, f, ensure_ascii=False, indent=4)

with open(os.path.expanduser("~/Desktop/dev.json"), "w", encoding='utf-8') as f:
    json.dump(dev_data, f, ensure_ascii=False, indent=4)

